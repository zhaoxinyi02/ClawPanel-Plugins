import type { ResolvedQQBotAccount, QQBotAccountConfig } from "./types.js";
interface MoltbotConfig {
    channels?: {
        qqbot?: QQBotChannelConfig;
        [key: string]: unknown;
    };
    [key: string]: unknown;
}
interface QQBotChannelConfig extends QQBotAccountConfig {
    accounts?: Record<string, QQBotAccountConfig>;
}
/**
 * 列出所有 QQBot 账户 ID
 */
export declare function listQQBotAccountIds(cfg: MoltbotConfig): string[];
/**
 * 解析 QQBot 账户配置
 */
export declare function resolveQQBotAccount(cfg: MoltbotConfig, accountId?: string | null): ResolvedQQBotAccount;
/**
 * 应用账户配置
 */
export declare function applyQQBotAccountConfig(cfg: MoltbotConfig, accountId: string, input: {
    appId?: string;
    clientSecret?: string;
    clientSecretFile?: string;
    name?: string;
    imageServerBaseUrl?: string;
}): MoltbotConfig;
export {};
