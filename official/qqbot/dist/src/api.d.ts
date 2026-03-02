/**
 * QQ Bot API 鉴权和请求封装
 */
/**
 * 获取 AccessToken（带缓存）
 */
export declare function getAccessToken(appId: string, clientSecret: string): Promise<string>;
/**
 * 清除 Token 缓存
 */
export declare function clearTokenCache(): void;
/**
 * 获取并递增消息序号
 * 返回的 seq 会基于时间戳，避免进程重启后重复
 */
export declare function getNextMsgSeq(msgId: string): number;
/**
 * API 请求封装
 */
export declare function apiRequest<T = unknown>(accessToken: string, method: string, path: string, body?: unknown): Promise<T>;
/**
 * 获取 WebSocket Gateway URL
 */
export declare function getGatewayUrl(accessToken: string): Promise<string>;
/**
 * 发送 C2C 单聊消息
 */
export declare function sendC2CMessage(accessToken: string, openid: string, content: string, msgId?: string): Promise<{
    id: string;
    timestamp: number;
}>;
/**
 * 发送频道消息
 */
export declare function sendChannelMessage(accessToken: string, channelId: string, content: string, msgId?: string): Promise<{
    id: string;
    timestamp: string;
}>;
/**
 * 发送群聊消息
 */
export declare function sendGroupMessage(accessToken: string, groupOpenid: string, content: string, msgId?: string): Promise<{
    id: string;
    timestamp: string;
}>;
/**
 * 主动发送 C2C 单聊消息（不需要 msg_id，每月限 4 条/用户）
 */
export declare function sendProactiveC2CMessage(accessToken: string, openid: string, content: string): Promise<{
    id: string;
    timestamp: number;
}>;
/**
 * 主动发送群聊消息（不需要 msg_id，每月限 4 条/群）
 */
export declare function sendProactiveGroupMessage(accessToken: string, groupOpenid: string, content: string): Promise<{
    id: string;
    timestamp: string;
}>;
/**
 * 媒体文件类型
 */
export declare enum MediaFileType {
    IMAGE = 1,
    VIDEO = 2,
    VOICE = 3,
    FILE = 4
}
/**
 * 上传富媒体文件的响应
 */
export interface UploadMediaResponse {
    file_uuid: string;
    file_info: string;
    ttl: number;
    id?: string;
}
/**
 * 上传富媒体文件到 C2C 单聊
 * @param accessToken 访问令牌
 * @param openid 用户 openid
 * @param fileType 文件类型
 * @param url 媒体资源 URL
 * @param srvSendMsg 是否直接发送（推荐 false，获取 file_info 后再发送）
 */
export declare function uploadC2CMedia(accessToken: string, openid: string, fileType: MediaFileType, url: string, srvSendMsg?: boolean): Promise<UploadMediaResponse>;
/**
 * 上传富媒体文件到群聊
 * @param accessToken 访问令牌
 * @param groupOpenid 群 openid
 * @param fileType 文件类型
 * @param url 媒体资源 URL
 * @param srvSendMsg 是否直接发送（推荐 false，获取 file_info 后再发送）
 */
export declare function uploadGroupMedia(accessToken: string, groupOpenid: string, fileType: MediaFileType, url: string, srvSendMsg?: boolean): Promise<UploadMediaResponse>;
/**
 * 发送 C2C 单聊富媒体消息
 * @param accessToken 访问令牌
 * @param openid 用户 openid
 * @param fileInfo 从 uploadC2CMedia 获取的 file_info
 * @param msgId 被动回复时需要的消息 ID
 * @param content 可选的文字内容
 */
export declare function sendC2CMediaMessage(accessToken: string, openid: string, fileInfo: string, msgId?: string, content?: string): Promise<{
    id: string;
    timestamp: number;
}>;
/**
 * 发送群聊富媒体消息
 * @param accessToken 访问令牌
 * @param groupOpenid 群 openid
 * @param fileInfo 从 uploadGroupMedia 获取的 file_info
 * @param msgId 被动回复时需要的消息 ID
 * @param content 可选的文字内容
 */
export declare function sendGroupMediaMessage(accessToken: string, groupOpenid: string, fileInfo: string, msgId?: string, content?: string): Promise<{
    id: string;
    timestamp: string;
}>;
/**
 * 发送带图片的 C2C 单聊消息（封装上传+发送）
 * @param accessToken 访问令牌
 * @param openid 用户 openid
 * @param imageUrl 图片 URL
 * @param msgId 被动回复时需要的消息 ID
 * @param content 可选的文字内容
 */
export declare function sendC2CImageMessage(accessToken: string, openid: string, imageUrl: string, msgId?: string, content?: string): Promise<{
    id: string;
    timestamp: number;
}>;
/**
 * 发送带图片的群聊消息（封装上传+发送）
 * @param accessToken 访问令牌
 * @param groupOpenid 群 openid
 * @param imageUrl 图片 URL
 * @param msgId 被动回复时需要的消息 ID
 * @param content 可选的文字内容
 */
export declare function sendGroupImageMessage(accessToken: string, groupOpenid: string, imageUrl: string, msgId?: string, content?: string): Promise<{
    id: string;
    timestamp: string;
}>;
