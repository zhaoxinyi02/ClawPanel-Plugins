# 34AI API Examples

这些示例按真实文档的方法和路径整理，调用时请把 API Key 从技能配置中读取。

## 小程序获取access_token
```text
请调用 34AI API 套件
- 接口：小程序获取access_token
- 方法：POST
- 路径：/cgi-bin/token
- 参数：
  - grant_type（可选）= ...
  - appid（可选）= ...
  - secret（可选）= ...
- 返回：请提取关键字段并简述结果
```

## 获取小程序跳转URL
```text
请调用 34AI API 套件
- 接口：获取小程序跳转URL
- 方法：POST
- 路径：/wxa/generatescheme
- 参数：
  - access_token（可选）= ...
  - jump_wxa（可选）= ...
- 返回：请提取关键字段并简述结果
```

## 抖音采集关键词文章(30s)
```text
请调用 34AI API 套件
- 接口：抖音采集关键词文章(30s)
- 方法：POST
- 路径：/index.php/api/Addons/douyin_search_articles
- 参数：
  - cookie（可选）= ...
  - keyword（必填）= ...
  - publish_time（必填）= ...
  - sort_type（必填）= ...
  - search_count（必填）= ...
  - token（可选）= ...
- 返回：请提取关键字段并简述结果
```

## 抖音采集文章评论
```text
请调用 34AI API 套件
- 接口：抖音采集文章评论
- 方法：POST
- 路径：/index.php/api/Addons/douyin_get_comments
- 参数：
  - video_url（可选）= ...
  - cookie（可选）= ...
  - token（可选）= ...
- 返回：请提取关键字段并简述结果
```

## 小红书采集关键词文章
```text
请调用 34AI API 套件
- 接口：小红书采集关键词文章
- 方法：POST
- 路径：/index.php/api/Addons/xhs_searchwenzhang
- 参数：
  - keyword（可选）= ...
  - page_count（可选）= ...
  - cookie（可选）= ...
  - token（可选）= ...
- 返回：请提取关键字段并简述结果
```

## 豆包文字生语音
```text
请调用 34AI API 套件
- 接口：豆包文字生语音
- 方法：POST
- 路径：/index.php/api/modelai/doubao_voice
- 参数：
  - token（可选）= ...
  - text（可选）= ...
  - type（可选）= ...
  - 音色列表（可选）= ...
- 返回：请提取关键字段并简述结果
```

## 创建草稿 /create_draft
```text
请调用 34AI API 套件
- 接口：创建草稿 /create_draft
- 方法：POST
- 路径：/create_draft
- 参数：
  - X-API-Key（必填）= ...
- 返回：请提取关键字段并简述结果
```

## 生成短视频（更新中）
```text
请调用 34AI API 套件
- 接口：生成短视频（更新中）
- 方法：POST
- 路径：/index.php/api/VideoGenerator/zhixing
- 参数：
  - content（可选）= ...
- 返回：请提取关键字段并简述结果
```

## 发送消息
```text
请调用 34AI API 套件
- 接口：发送消息
- 方法：POST
- 路径：/index.php/api/wss/onsend
- 参数：
  - uid（可选）= ...
  - content（可选）= ...
- 返回：请提取关键字段并简述结果
```

## RPA发送指令(采集)
```text
请调用 34AI API 套件
- 接口：RPA发送指令(采集)
- 方法：POST
- 路径：/index.php/api/wss/fiveai_to_send
- 参数：
  - phone（可选）= ...
  - password（可选）= ...
- 返回：请提取关键字段并简述结果
```
