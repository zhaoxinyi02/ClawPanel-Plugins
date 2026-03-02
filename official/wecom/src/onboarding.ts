import type { ChannelOnboardingAdapter, OpenclawConfig, WizardPrompter } from "./compat.js";
import { DEFAULT_ACCOUNT_ID, normalizeAccountId } from "./compat.js";

import { listWecomAccountIds, resolveDefaultWecomAccountId, resolveWecomAccount } from "./accounts.js";

const channel = "wecom" as const;

async function noteWecomConfigHelp(prompter: WizardPrompter): Promise<void> {
  await prompter.note(
    [
      "1) 登录企业微信管理后台 → 应用管理 → 创建智能机器人",
      "2) 配置回调 URL",
      "3) 获取 Token 和 EncodingAESKey",
      "4) 你也可以使用环境变量 WECOM_TOKEN 和 WECOM_ENCODING_AES_KEY",
    ].join("\n"),
    "WeCom 配置说明",
  );
}

export const wecomOnboardingAdapter: ChannelOnboardingAdapter = {
  channel,
  getStatus: async ({ cfg }) => {
    const configured = listWecomAccountIds(cfg as OpenclawConfig).some((accountId) => {
      const account = resolveWecomAccount({ cfg: cfg as OpenclawConfig, accountId });
      return account.configured;
    });
    return {
      channel,
      configured,
      statusLines: [`WeCom: ${configured ? "configured" : "needs token + encodingAESKey"}`],
      selectionHint: configured ? "configured" : undefined,
      quickstartScore: configured ? 1 : 5,
    };
  },
  configure: async ({ cfg, prompter, accountOverrides, shouldPromptAccountIds }) => {
    const wecomOverride = accountOverrides.wecom?.trim();
    const defaultWecomAccountId = resolveDefaultWecomAccountId(cfg as OpenclawConfig);
    let wecomAccountId = wecomOverride
      ? (normalizeAccountId(wecomOverride) ?? DEFAULT_ACCOUNT_ID)
      : defaultWecomAccountId;

    if (shouldPromptAccountIds && !wecomOverride) {
      const accountIds = listWecomAccountIds(cfg as OpenclawConfig);
      if (accountIds.length > 1) {
        const selected = await prompter.select({
          message: "选择 WeCom 账户",
          options: accountIds.map((id) => ({ value: id, label: id })),
          initialValue: wecomAccountId,
        });
        wecomAccountId = String(selected);
      }
    }

    let next = cfg as OpenclawConfig;
    const resolvedAccount = resolveWecomAccount({ cfg: next, accountId: wecomAccountId });
    const accountConfigured = resolvedAccount.configured;

    if (!accountConfigured) {
      await noteWecomConfigHelp(prompter);
    }

    // Prompt for Token
    let token = resolvedAccount.token;
    if (!token) {
      token = String(
        await prompter.text({
          message: "输入 WeCom Token",
          validate: (value) => (value?.trim() ? undefined : "必填"),
        }),
      ).trim();
    } else {
      const keep = await prompter.confirm({
        message: "Token 已配置，是否保留？",
        initialValue: true,
      });
      if (!keep) {
        token = String(
          await prompter.text({
            message: "输入新的 WeCom Token",
            validate: (value) => (value?.trim() ? undefined : "必填"),
          }),
        ).trim();
      }
    }

    // Prompt for EncodingAESKey
    let encodingAESKey = resolvedAccount.encodingAESKey;
    if (!encodingAESKey) {
      encodingAESKey = String(
        await prompter.text({
          message: "输入 WeCom EncodingAESKey（43位）",
          validate: (value) => {
            if (!value?.trim()) return "必填";
            if (value.trim().length !== 43) return "EncodingAESKey 必须是 43 位";
            return undefined;
          },
        }),
      ).trim();
    } else {
      const keep = await prompter.confirm({
        message: "EncodingAESKey 已配置，是否保留？",
        initialValue: true,
      });
      if (!keep) {
        encodingAESKey = String(
          await prompter.text({
            message: "输入新的 WeCom EncodingAESKey（43位）",
            validate: (value) => {
              if (!value?.trim()) return "必填";
              if (value.trim().length !== 43) return "EncodingAESKey 必须是 43 位";
              return undefined;
            },
          }),
        ).trim();
      }
    }

    // Prompt for webhook path
    let webhookPath = String(
      await prompter.text({
        message: "Webhook 路径(用于接收消息回调)",
        initialValue: "/wecom",
        validate: (value) => (value?.trim() ? undefined : "必填"),
      }),
    ).trim();
    if (!webhookPath.startsWith("/")) {
      webhookPath = `/${webhookPath}`;
    }

    // Apply config
    if (wecomAccountId === DEFAULT_ACCOUNT_ID) {
      next = {
        ...next,
        channels: {
          ...next.channels,
          wecom: {
            ...next.channels?.wecom,
            enabled: true,
            token,
            encodingAESKey,
            webhookPath,
          },
        },
      };
    } else {
      next = {
        ...next,
        channels: {
          ...next.channels,
          wecom: {
            ...next.channels?.wecom,
            enabled: true,
            accounts: {
              ...((next.channels?.wecom as any)?.accounts ?? {}),
              [wecomAccountId]: {
                ...((next.channels?.wecom as any)?.accounts?.[wecomAccountId] ?? {}),
          enabled: true,
          token,
          encodingAESKey,
          webhookPath,
              },
            },
          },
        },
      };
    }

    // WeCom 需要接收外部 webhook，自动设置 gateway.bind = lan
    if ((next as any).gateway?.bind !== "lan") {
      next = {
        ...next,
        gateway: {
          ...(next as any).gateway,
          bind: "lan",
        },
      } as OpenclawConfig;
    }

    return { cfg: next, accountId: wecomAccountId };
  },
  disable: (cfg) => ({
    ...cfg,
    channels: {
      ...cfg.channels,
      wecom: { ...(cfg.channels?.wecom as any), enabled: false },
    },
  }),
};
