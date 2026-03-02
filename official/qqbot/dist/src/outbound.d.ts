import type { ResolvedQQBotAccount } from "./types.js";
export interface OutboundContext {
    to: string;
    text: string;
    accountId?: string | null;
    replyToId?: string | null;
    account: ResolvedQQBotAccount;
}
export interface OutboundResult {
    channel: string;
    messageId?: string;
    timestamp?: string | number;
    error?: string;
}
/**
 * 发送文本消息（被动回复，需要 replyToId）
 */
export declare function sendText(ctx: OutboundContext): Promise<OutboundResult>;
/**
 * 主动发送消息（不需要 replyToId，有配额限制：每月 4 条/用户/群）
 *
 * @param account - 账户配置
 * @param to - 目标地址，格式：openid（单聊）或 group:xxx（群聊）
 * @param text - 消息内容
 */
export declare function sendProactiveMessage(account: ResolvedQQBotAccount, to: string, text: string): Promise<OutboundResult>;
