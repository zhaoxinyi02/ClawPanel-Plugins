/**
 * DingTalk Onboarding Adapter - handles initial setup and configuration
 */
import { listDingTalkAccountIds, resolveDingTalkAccount, resolveDefaultDingTalkAccountId, isDingTalkAccountConfigured, } from "./accounts.js";
import { DEFAULT_ACCOUNT_ID } from "./config-schema.js";

const channel = "dingtalk";

/**
 * Display help note for obtaining DingTalk credentials
 */
async function noteDingTalkCredentialsHelp(prompter) {
    await prompter.note([
        "获取钉钉机器人凭证：",
        "1) 登录钉钉开放平台 → 应用开发 → 企业内部应用 → 创建应用",
        "2) 在应用信息页面获取 ClientID (AppKey) 和 ClientSecret (AppSecret)",
        "3) 在机器人配置中启用机器人功能",
        "4) 确保机器人已被添加到目标群聊",
        "",
        "文档: https://open.dingtalk.com/document/orgapp/create-an-enterprise-internal-bot",
    ].join("\n"), "钉钉机器人配置");
}

/**
 * Set DingTalk credentials in config
 */
function setDingTalkCredentials(cfg, accountId, clientId, clientSecret) {
    if (accountId === DEFAULT_ACCOUNT_ID) {
        return {
            ...cfg,
            channels: {
                ...cfg.channels,
                dingtalk: {
                    ...cfg.channels?.dingtalk,
                    enabled: true,
                    clientId,
                    clientSecret,
                },
            },
        };
    }
    return {
        ...cfg,
        channels: {
            ...cfg.channels,
            dingtalk: {
                ...cfg.channels?.dingtalk,
                enabled: true,
                accounts: {
                    ...cfg.channels?.dingtalk?.accounts,
                    [accountId]: {
                        ...cfg.channels?.dingtalk?.accounts?.[accountId],
                        enabled: true,
                        clientId,
                        clientSecret,
                    },
                },
            },
        },
    };
}

/**
 * DingTalk onboarding adapter - handles initial setup and configuration
 */
export const dingtalkOnboardingAdapter = {
    channel,

    /**
     * Get current configuration status for DingTalk
     */
    getStatus: async (ctx) => {
        const { cfg } = ctx;
        const accountIds = listDingTalkAccountIds(cfg);
        const configured = accountIds.some((accountId) => {
            const account = resolveDingTalkAccount({ cfg, accountId });
            return isDingTalkAccountConfigured(account);
        });

        return {
            channel,
            configured,
            statusLines: [`DingTalk: ${configured ? "configured" : "needs credentials"}`],
            selectionHint: configured ? "configured" : "needs credentials",
        };
    },

    /**
     * Interactive configuration wizard for DingTalk
     */
    configure: async (ctx) => {
        const { cfg, prompter } = ctx;

        // Determine account ID
        const defaultAccountId = resolveDefaultDingTalkAccountId(cfg);
        const dingtalkAccountId = defaultAccountId;

        let next = cfg;
        const resolvedAccount = resolveDingTalkAccount({
            cfg: next,
            accountId: dingtalkAccountId,
        });
        const accountConfigured = isDingTalkAccountConfigured(resolvedAccount);

        // Check for environment variables
        const allowEnv = dingtalkAccountId === DEFAULT_ACCOUNT_ID;
        const envClientId = process.env.DINGTALK_CLIENT_ID?.trim();
        const envClientSecret = process.env.DINGTALK_CLIENT_SECRET?.trim();
        const canUseEnv = allowEnv && Boolean(envClientId && envClientSecret);
        const hasConfigCredentials = Boolean(resolvedAccount.clientId && resolvedAccount.clientSecret);

        let clientId = null;
        let clientSecret = null;

        // Show help if not configured
        if (!accountConfigured) {
            await noteDingTalkCredentialsHelp(prompter);
        }

        // Handle credential input
        if (canUseEnv && resolvedAccount.credentialSource !== "config") {
            // Environment variables detected
            const keepEnv = await prompter.confirm({
                message: "检测到 DINGTALK_CLIENT_ID/DINGTALK_CLIENT_SECRET 环境变量，是否使用？",
                initialValue: true,
            });
            if (keepEnv) {
                next = {
                    ...next,
                    channels: {
                        ...next.channels,
                        dingtalk: { ...next.channels?.dingtalk, enabled: true },
                    },
                };
            } else {
                // Prompt for manual input
                clientId = String(
                    await prompter.text({
                        message: "请输入钉钉 ClientID (AppKey)",
                        validate: (value) => (value?.trim() ? undefined : "必填"),
                    }),
                ).trim();
                clientSecret = String(
                    await prompter.text({
                        message: "请输入钉钉 ClientSecret (AppSecret)",
                        validate: (value) => (value?.trim() ? undefined : "必填"),
                    }),
                ).trim();
            }
        } else if (hasConfigCredentials) {
            // Already configured, ask if want to keep
            const keep = await prompter.confirm({
                message: "钉钉凭证已配置，是否保留现有配置？",
                initialValue: true,
            });
            if (!keep) {
                clientId = String(
                    await prompter.text({
                        message: "请输入钉钉 ClientID (AppKey)",
                        validate: (value) => (value?.trim() ? undefined : "必填"),
                    }),
                ).trim();
                clientSecret = String(
                    await prompter.text({
                        message: "请输入钉钉 ClientSecret (AppSecret)",
                        validate: (value) => (value?.trim() ? undefined : "必填"),
                    }),
                ).trim();
            }
        } else {
            // No credentials, prompt for input
            clientId = String(
                await prompter.text({
                    message: "请输入钉钉 ClientID (AppKey)",
                    validate: (value) => (value?.trim() ? undefined : "必填"),
                }),
            ).trim();
            clientSecret = String(
                await prompter.text({
                    message: "请输入钉钉 ClientSecret (AppSecret)",
                    validate: (value) => (value?.trim() ? undefined : "必填"),
                }),
            ).trim();
        }

        // Apply credentials if provided
        if (clientId && clientSecret) {
            next = setDingTalkCredentials(next, dingtalkAccountId, clientId, clientSecret);
        }

        return { cfg: next, accountId: dingtalkAccountId };
    },

    /**
     * Disable DingTalk channel
     */
    disable: (cfg) => ({
        ...cfg,
        channels: {
            ...cfg.channels,
            dingtalk: { ...cfg.channels?.dingtalk, enabled: false },
        },
    }),
};
