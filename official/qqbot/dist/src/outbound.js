import { getAccessToken, sendC2CMessage, sendChannelMessage, sendGroupMessage, sendProactiveC2CMessage, sendProactiveGroupMessage, } from "./api.js";
/**
 * 解析目标地址
 * 格式：
 *   - openid (32位十六进制) -> C2C 单聊
 *   - group:xxx -> 群聊
 *   - channel:xxx -> 频道
 *   - 纯数字 -> 频道
 */
function parseTarget(to) {
    if (to.startsWith("group:")) {
        return { type: "group", id: to.slice(6) };
    }
    if (to.startsWith("channel:")) {
        return { type: "channel", id: to.slice(8) };
    }
    // openid 通常是 32 位十六进制
    if (/^[A-F0-9]{32}$/i.test(to)) {
        return { type: "c2c", id: to };
    }
    // 默认当作频道 ID
    return { type: "channel", id: to };
}
/**
 * 发送文本消息（被动回复，需要 replyToId）
 */
export async function sendText(ctx) {
    const { to, text, replyToId, account } = ctx;
    if (!account.appId || !account.clientSecret) {
        return { channel: "qqbot", error: "QQBot not configured (missing appId or clientSecret)" };
    }
    try {
        const accessToken = await getAccessToken(account.appId, account.clientSecret);
        const target = parseTarget(to);
        if (target.type === "c2c") {
            const result = await sendC2CMessage(accessToken, target.id, text, replyToId ?? undefined);
            return { channel: "qqbot", messageId: result.id, timestamp: result.timestamp };
        }
        else if (target.type === "group") {
            const result = await sendGroupMessage(accessToken, target.id, text, replyToId ?? undefined);
            return { channel: "qqbot", messageId: result.id, timestamp: result.timestamp };
        }
        else {
            const result = await sendChannelMessage(accessToken, target.id, text, replyToId ?? undefined);
            return { channel: "qqbot", messageId: result.id, timestamp: result.timestamp };
        }
    }
    catch (err) {
        const message = err instanceof Error ? err.message : String(err);
        return { channel: "qqbot", error: message };
    }
}
/**
 * 主动发送消息（不需要 replyToId，有配额限制：每月 4 条/用户/群）
 *
 * @param account - 账户配置
 * @param to - 目标地址，格式：openid（单聊）或 group:xxx（群聊）
 * @param text - 消息内容
 */
export async function sendProactiveMessage(account, to, text) {
    if (!account.appId || !account.clientSecret) {
        return { channel: "qqbot", error: "QQBot not configured (missing appId or clientSecret)" };
    }
    try {
        const accessToken = await getAccessToken(account.appId, account.clientSecret);
        const target = parseTarget(to);
        if (target.type === "c2c") {
            const result = await sendProactiveC2CMessage(accessToken, target.id, text);
            return { channel: "qqbot", messageId: result.id, timestamp: result.timestamp };
        }
        else if (target.type === "group") {
            const result = await sendProactiveGroupMessage(accessToken, target.id, text);
            return { channel: "qqbot", messageId: result.id, timestamp: result.timestamp };
        }
        else {
            // 频道暂不支持主动消息，使用普通发送
            const result = await sendChannelMessage(accessToken, target.id, text);
            return { channel: "qqbot", messageId: result.id, timestamp: result.timestamp };
        }
    }
    catch (err) {
        const message = err instanceof Error ? err.message : String(err);
        return { channel: "qqbot", error: message };
    }
}
