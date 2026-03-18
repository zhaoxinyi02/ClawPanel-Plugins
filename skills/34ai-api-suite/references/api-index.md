# 34AI API Index

以下内容逐条根据 Apifox `.md` 文档里的 OpenAPI YAML 解析生成。

## 34AI自动化工具
### coze储存数据
- 方法：`POST`
- 路径：`/index.php/api/Addons/set_coze_data`
- 文档：<https://s.apifox.cn/3cd5a990-f653-4555-9b72-0ac8741ba993/272083292e0.md>
- 参数：
  - `data`（query，可选）：无说明；示例：`{"jh":"fsdsdsf"}`
  - `token`（query，可选）：无说明；示例：`2082b3e87116f4ffa95525e1c034dd53`
  - `flag`（query，可选）：无说明；示例：`18625522203`
  - `type`（query，可选）：无说明；示例：`1`
- 返回：`application/json` / `object`

### Coze获取数据
- 方法：`GET`
- 路径：`/index.php/api/Addons/get_coze_data`
- 文档：<https://s.apifox.cn/3cd5a990-f653-4555-9b72-0ac8741ba993/272096951e0.md>
- 参数：文档未声明或为空
- 返回：`application/json` / `object`

### 转化飞书数据
- 方法：`POST`
- 路径：`/index.php/api/tolink/feishutodata`
- 文档：<https://s.apifox.cn/3cd5a990-f653-4555-9b72-0ac8741ba993/310322928e0.md>
- 参数：
  - `data`（query，可选）：无说明；示例：`[
    {
      "IPlocal": "安徽",
      "colloctnum": 0,
      "comment_content": "`
  - `wenzhangkeyword`（query，可选）：无说明；示例：`Ai`
  - `pinglunkerword`（query，可选）：无说明；示例：`工具,大家,出来,路径`

## AI自动剪辑
### 生成短视频（更新中）
- 方法：`POST`
- 路径：`/index.php/api/VideoGenerator/zhixing`
- 文档：<https://s.apifox.cn/3cd5a990-f653-4555-9b72-0ac8741ba993/230901985e0.md>
- 参数：
  - `content`（query，可选）：无说明；示例：`6362e1bbf249571f5c62a1c0533bd245`
- 返回：`application/json` / `object`
  - 主要字段：code, msg, data

### 高质量剪辑任务查询
- 方法：`POST`
- 路径：`/index.php/api/CutVideo/agent_run_cutvideo`
- 文档：<https://s.apifox.cn/3cd5a990-f653-4555-9b72-0ac8741ba993/402777633e0.md>
- 参数：文档未声明或为空
- 返回：`application/json` / `object`
  - 主要字段：code, msg, data

## AI自动剪辑/关键帧
### 添加视频关键帧 /add_video_keyframe
- 方法：`POST`
- 路径：`/add_video_keyframe`
- 文档：<https://s.apifox.cn/3cd5a990-f653-4555-9b72-0ac8741ba993/357975771e0.md>
- 参数：
  - `X-API-Key`（header，必填）：无说明；示例：`{{apiKey}}`
- Body：`application/json` / `object`
- 返回：`application/json` / `object`

## AI自动剪辑/图像处理
### 添加图片 /add_image
- 方法：`POST`
- 路径：`/add_image`
- 文档：<https://s.apifox.cn/3cd5a990-f653-4555-9b72-0ac8741ba993/357975768e0.md>
- 参数：
  - `X-API-Key`（header，必填）：无说明；示例：`{{apiKey}}`
- Body：`application/json` / `object`
- 返回：`application/json` / `object`

## AI自动剪辑/文本处理
### 添加文本 /add_text
- 方法：`POST`
- 路径：`/add_text`
- 文档：<https://s.apifox.cn/3cd5a990-f653-4555-9b72-0ac8741ba993/357975766e0.md>
- 参数：
  - `X-API-Key`（header，必填）：无说明；示例：`{{apiKey}}`
- Body：`application/json` / `object`
- 返回：`application/json` / `object`

### 添加字幕 /add_subtitle
- 方法：`POST`
- 路径：`/add_subtitle`
- 文档：<https://s.apifox.cn/3cd5a990-f653-4555-9b72-0ac8741ba993/357975767e0.md>
- 参数：
  - `X-API-Key`（header，必填）：无说明；示例：`{{apiKey}}`
- Body：`application/json` / `object`
- 返回：`application/json` / `object`

### 获取字体类型 /get_font_types
- 方法：`GET`
- 路径：`/get_font_types`
- 文档：<https://s.apifox.cn/3cd5a990-f653-4555-9b72-0ac8741ba993/357975778e0.md>
- 参数：
  - `X-API-Key`（header，必填）：无说明；示例：`{{apiKey}}`
- 返回：`application/json` / `object`

### 获取文本入场动画类型 /get_text_intro_types
- 方法：`GET`
- 路径：`/get_text_intro_types`
- 文档：<https://s.apifox.cn/3cd5a990-f653-4555-9b72-0ac8741ba993/357975779e0.md>
- 参数：
  - `X-API-Key`（header，必填）：无说明；示例：`{{apiKey}}`
- 返回：`application/json` / `object`

### 获取文本出场动画类型 /get_text_outro_types
- 方法：`GET`
- 路径：`/get_text_outro_types`
- 文档：<https://s.apifox.cn/3cd5a990-f653-4555-9b72-0ac8741ba993/357975780e0.md>
- 参数：
  - `X-API-Key`（header，必填）：无说明；示例：`{{apiKey}}`
- 返回：`application/json` / `object`

### 获取文本循环动画类型 /get_text_loop_anim_types
- 方法：`GET`
- 路径：`/get_text_loop_anim_types`
- 文档：<https://s.apifox.cn/3cd5a990-f653-4555-9b72-0ac8741ba993/357975781e0.md>
- 参数：
  - `X-API-Key`（header，必填）：无说明；示例：`{{apiKey}}`
- 返回：`application/json` / `object`

## AI自动剪辑/特效系统
### 添加特效 /add_effect
- 方法：`POST`
- 路径：`/add_effect`
- 文档：<https://s.apifox.cn/3cd5a990-f653-4555-9b72-0ac8741ba993/357975770e0.md>
- 参数：
  - `X-API-Key`（header，必填）：无说明；示例：`{{apiKey}}`
- Body：`application/json` / `object`
- 返回：`application/json` / `object`

## AI自动剪辑/草稿管理
### 创建草稿 /create_draft
- 方法：`POST`
- 路径：`/create_draft`
- 文档：<https://s.apifox.cn/3cd5a990-f653-4555-9b72-0ac8741ba993/357975759e0.md>
- 参数：
  - `X-API-Key`（header，必填）：无说明；示例：`{{apiKey}}`
- Body：`application/json` / `object`
- 返回：`application/json` / `object`

### 保存并下载草稿 /save_draft
- 方法：`POST`
- 路径：`/save_draft`
- 文档：<https://s.apifox.cn/3cd5a990-f653-4555-9b72-0ac8741ba993/357975760e0.md>
- 参数：
  - `X-API-Key`（header，必填）：无说明；示例：`{{apiKey}}`
- Body：`application/json` / `object`
- 返回：`application/json` / `object`

### 查询草稿信息 /query_script
- 方法：`POST`
- 路径：`/query_script`
- 文档：<https://s.apifox.cn/3cd5a990-f653-4555-9b72-0ac8741ba993/357975762e0.md>
- 参数：
  - `X-API-Key`（header，必填）：无说明；示例：`{{apiKey}}`
- Body：`application/json` / `object`
- 返回：`application/json` / `object`

## AI自动剪辑/视频处理
### 添加视频 /add_video
- 方法：`POST`
- 路径：`/add_video`
- 文档：<https://s.apifox.cn/3cd5a990-f653-4555-9b72-0ac8741ba993/357975764e0.md>
- 参数：
  - `X-API-Key`（header，必填）：无说明；示例：`{{apiKey}}`
- Body：`application/json` / `object`
- 返回：`application/json` / `object`

### 获取入场动画类型 /get_intro_animation_types
- 方法：`GET`
- 路径：`/get_intro_animation_types`
- 文档：<https://s.apifox.cn/3cd5a990-f653-4555-9b72-0ac8741ba993/357975772e0.md>
- 参数：
  - `X-API-Key`（header，必填）：无说明；示例：`{{apiKey}}`
- 返回：`application/json` / `object`

### 获取出场动画类型 /get_outro_animation_types
- 方法：`GET`
- 路径：`/get_outro_animation_types`
- 文档：<https://s.apifox.cn/3cd5a990-f653-4555-9b72-0ac8741ba993/357975773e0.md>
- 参数：
  - `X-API-Key`（header，必填）：无说明；示例：`{{apiKey}}`
- 返回：`application/json` / `object`

### 获取组合动画类型 /get_combo_animation_types
- 方法：`GET`
- 路径：`/get_combo_animation_types`
- 文档：<https://s.apifox.cn/3cd5a990-f653-4555-9b72-0ac8741ba993/357975774e0.md>
- 参数：
  - `X-API-Key`（header，必填）：无说明；示例：`{{apiKey}}`
- 返回：`application/json` / `object`

### 获取转场类型 /get_transition_types
- 方法：`GET`
- 路径：`/get_transition_types`
- 文档：<https://s.apifox.cn/3cd5a990-f653-4555-9b72-0ac8741ba993/357975775e0.md>
- 参数：
  - `X-API-Key`（header，必填）：无说明；示例：`{{apiKey}}`
- 返回：`application/json` / `object`

### 获取蒙版类型 /get_mask_types
- 方法：`GET`
- 路径：`/get_mask_types`
- 文档：<https://s.apifox.cn/3cd5a990-f653-4555-9b72-0ac8741ba993/357975776e0.md>
- 参数：
  - `X-API-Key`（header，必填）：无说明；示例：`{{apiKey}}`
- 返回：`application/json` / `object`

### 获取视频场景特效类型 /get_video_scene_effect_types
- 方法：`GET`
- 路径：`/get_video_scene_effect_types`
- 文档：<https://s.apifox.cn/3cd5a990-f653-4555-9b72-0ac8741ba993/357975782e0.md>
- 参数：
  - `X-API-Key`（header，必填）：无说明；示例：`{{apiKey}}`
- 返回：`application/json` / `object`

### 获取视频人物特效类型 /get_video_character_effect_types
- 方法：`GET`
- 路径：`/get_video_character_effect_types`
- 文档：<https://s.apifox.cn/3cd5a990-f653-4555-9b72-0ac8741ba993/357975783e0.md>
- 参数：
  - `X-API-Key`（header，必填）：无说明；示例：`{{apiKey}}`
- 返回：`application/json` / `object`

## AI自动剪辑/贴纸系统
### 添加贴纸 /add_sticker
- 方法：`POST`
- 路径：`/add_sticker`
- 文档：<https://s.apifox.cn/3cd5a990-f653-4555-9b72-0ac8741ba993/357975769e0.md>
- 参数：
  - `X-API-Key`（header，必填）：无说明；示例：`{{apiKey}}`
- Body：`application/json` / `object`
- 返回：`application/json` / `object`

## AI自动剪辑/音频处理
### 添加音频 /add_audio
- 方法：`POST`
- 路径：`/add_audio`
- 文档：<https://s.apifox.cn/3cd5a990-f653-4555-9b72-0ac8741ba993/357975765e0.md>
- 参数：
  - `X-API-Key`（header，必填）：无说明；示例：`{{apiKey}}`
- Body：`application/json` / `object`
- 返回：`application/json` / `object`

### 获取音频字幕数据
- 方法：`POST`
- 路径：`/asr_recognize`
- 文档：<https://s.apifox.cn/3cd5a990-f653-4555-9b72-0ac8741ba993/358028808e0.md>
- 参数：
  - `audio_path`（query，可选）：无说明；示例：`https://chat.34ai.cc/aliyun/CosyVoice/tts_5de783d4.mp3`
  - `token`（query，可选）：无说明；示例：`71fc14b820123d323bc14e49cd95fa45`
  - `engine_type`（query，可选）：无说明；示例：`16k_zh`
- Body：`application/json` / `object`

### 获取音频特效类型 /get_audio_effect_types
- 方法：`GET`
- 路径：`/get_audio_effect_types`
- 文档：<https://s.apifox.cn/3cd5a990-f653-4555-9b72-0ac8741ba993/357975777e0.md>
- 参数：
  - `X-API-Key`（header，必填）：无说明；示例：`{{apiKey}}`
- 返回：`application/json` / `object`

## Ai绘图
### 豆包文生图
- 方法：`POST`
- 路径：`/index.php/api/modelai/text_to_image`
- 文档：<https://s.apifox.cn/3cd5a990-f653-4555-9b72-0ac8741ba993/383321445e0.md>
- 参数：
  - `token`（query，可选）：无说明；示例：`88a0bf1afa04176d313604c9f9ac65f8`
  - `prompt`（query，可选）：无说明；示例：`近景画面，新国风写实绘画风格，三分法构图。画面中心是几个坐在石凳上的老人，他们穿着朴素的靛蓝或正红传统服饰，手持蒲扇，一边摇着一边绘声绘色地讲着故事，脸上带着和`
- 返回：`*/*` / `object`

### 豆包图生视频
- 方法：`POST`
- 路径：`/index.php/api/modelai/doubao_seedance_image_to_video`
- 文档：<https://s.apifox.cn/3cd5a990-f653-4555-9b72-0ac8741ba993/383321696e0.md>
- 参数：
  - `token`（query，可选）：无说明；示例：`88a0bf1afa04176d313604c9f9ac65f8`
  - `prompt`（query，可选）：无说明；示例：`远景。画面以经典三分法构图，背景是层叠透视的墨绿远山和青蓝天空。画面下方是草绿田野，村口一棵粗壮的老槐树占据画面中心。柔和自然光从左上方斜射，树干有清晰明暗交界`
  - `time`（query，可选）：无说明；示例：`3`
  - `image`（query，可选）：无说明；示例：`https://p26-bot-workflow-sign.byteimg.com/tos-cn-i-mdko3gqilj/58aa46b7ee8d44be99`
- Body：`multipart/form-data` / `object`
- 返回：`*/*` / `object`

### 豆包图生视频查询
- 方法：`POST`
- 路径：`/index.php/api/modelai/search_image_to_video`
- 文档：<https://s.apifox.cn/3cd5a990-f653-4555-9b72-0ac8741ba993/383322240e0.md>
- 参数：
  - `token`（query，可选）：无说明；示例：`88a0bf1afa04176d313604c9f9ac65f8`
  - `id`（query，可选）：无说明；示例：`cgt-20251128033719-xqgfg`
- 返回：`*/*` / `object`

### 豆包文字生语音
- 方法：`POST`
- 路径：`/index.php/api/modelai/doubao_voice`
- 文档：<https://s.apifox.cn/3cd5a990-f653-4555-9b72-0ac8741ba993/383322294e0.md>
- 参数：
  - `token`（query，可选）：无说明；示例：`88a0bf1afa04176d313604c9f9ac65f8`
  - `text`（query，可选）：无说明；示例：`每到晒谷的季节，天刚蒙蒙亮，村里的大人们就扛着竹耙、扫帚，带着自家的粮食来到晒谷场。我跟着爷爷，看着他把一袋袋金黄的稻谷倒在晒谷场上，扬起的谷粒在晨曦中闪烁着光`
  - `type`（query，可选）：无说明；示例：`zh_male_tangseng_mars_bigtts`
  - `音色列表`（query，可选）：无说明；示例：`https://d18ugzan8f.feishu.cn/wiki/FHi6wIzxoih4X8kMGqycCxKBnwc?from=from_copylink`
- 返回：`*/*` / `object`

## Ai视频
### 视频转音频工具
- 方法：`POST`
- 路径：`/index.php/api/addons/video2mp3`
- 文档：<https://s.apifox.cn/3cd5a990-f653-4555-9b72-0ac8741ba993/276410578e0.md>
- 参数：
  - `token`（query，可选）：无说明；示例：`8e027ce75bfd1707fb628880ff24b66f`
  - `url`（query，可选）：无说明；示例：`https://aweme.snssdk.com/aweme/v1/playwm?line=0&logo_name=aweme_diversion_search`
- Body：`multipart/form-data` / `object`
- 返回：`*/*` / `object`

### 音频转文字
- 方法：`POST`
- 路径：`/index.php/api/addons/mp3totext`
- 文档：<https://s.apifox.cn/3cd5a990-f653-4555-9b72-0ac8741ba993/335072856e0.md>
- 参数：
  - `token`（query，可选）：无说明；示例：`c014248044672759672057f2086f1d7b`
  - `url`（query，可选）：无说明；示例：`https://34ai.cc/temp/audio/68675c0f27eb9.mp3`
- Body：`multipart/form-data` / `object`
- 返回：`*/*` / `object`

### 创建高质量剪辑
- 方法：`POST`
- 路径：`/index.php/api/Cutapi/autocut`
- 文档：<https://s.apifox.cn/3cd5a990-f653-4555-9b72-0ac8741ba993/367054522e0.md>
- 参数：
  - `audio_url`（query，可选）：无说明；示例：`https://aiyuangongoss.oss-cn-beijing.aliyuncs.com/app%2Fbase%2F%E7%BA%A2%E6%9F%B`
  - `text`（query，可选）：无说明；示例：`最近总有人问我：“陈哥，公司团建20个人，想找个热闹又有特色的地方，你这有吗？”我总拍着胸脯说：“来我家蒙古包！`
  - `user_task_id`（query，可选）：无说明；示例：`42`
  - `draft_folder`（query，可选）：无说明；示例：`F:\\jianying\\JianyingPro Drafts`
  - `is_background_music`（query，可选）：无说明；示例：`1`
  - `is_voice_effect`（query，可选）：无说明；示例：`1`
  - `is_xuanran`（query，可选）：无说明；示例：`2`
  - `number`（query，可选）：无说明；示例：`1`
  - `pangbai`（query，可选）：无说明；示例：`https://34ai.cc/indextts2/flac_6968a5898798b.mp3`
  - `phone`（query，可选）：无说明；示例：`18625522203`
  - `userid`（query，可选）：无说明；示例：`42`
  - `video_material`（query，可选）：无说明；示例：`42`
  - `is_shuziren`（query，可选）：无说明；示例：`1`
  - `taskid`（query，可选）：无说明；示例：`42`
- 返回：`application/json` / `object`

### 渲染高质量剪辑
- 方法：`POST`
- 路径：`/index.php/api/CutVideo/agent_run_cutvideo`
- 文档：<https://s.apifox.cn/3cd5a990-f653-4555-9b72-0ac8741ba993/367585382e0.md>
- 参数：文档未声明或为空
- 返回：`application/json` / `object`

### Sora图生视频
- 方法：`POST`
- 路径：`/index.php/api/CutVideo/sora_create`
- 文档：<https://s.apifox.cn/3cd5a990-f653-4555-9b72-0ac8741ba993/368778238e0.md>
- 参数：
  - `prompt`（query，可选）：无说明
- Body：`multipart/form-data` / `object`
  - 字段：prompt, image_url, aspectRatio, duration
- 返回：`application/json` / `object`

### Sora图生视频·查询结果
- 方法：`POST`
- 路径：`/index.php/api/CutVideo/sora_seacrh`
- 文档：<https://s.apifox.cn/3cd5a990-f653-4555-9b72-0ac8741ba993/368778930e0.md>
- 参数：
  - `prompt`（query，可选）：无说明
- Body：`multipart/form-data` / `object`
  - 字段：task_id
- 返回：`application/json` / `object`

### Sora图生视频定时生图(5秒)
- 方法：`POST`
- 路径：`/index.php/api/CutVideo/dingshi_sora`
- 文档：<https://s.apifox.cn/3cd5a990-f653-4555-9b72-0ac8741ba993/387424052e0.md>
- 参数：
  - `prompt`（query，可选）：无说明
- Body：`multipart/form-data` / `object`
- 返回：`application/json` / `object`

### Sora图生视频定时查结果(5秒)
- 方法：`POST`
- 路径：`/index.php/api/CutVideo/dingshi_sora_seacrh`
- 文档：<https://s.apifox.cn/3cd5a990-f653-4555-9b72-0ac8741ba993/387424147e0.md>
- 参数：
  - `prompt`（query，可选）：无说明
- Body：`multipart/form-data` / `object`
- 返回：`application/json` / `object`

### 【禁用】定时器合成TTS2音频任务
- 方法：`POST`
- 路径：`/index.php/api/CutVideo/run_indextts2`
- 文档：<https://s.apifox.cn/3cd5a990-f653-4555-9b72-0ac8741ba993/375185455e0.md>
- 参数：文档未声明或为空
- 返回：`*/*` / `object`

## Ai语音
### index2克隆音频
- 方法：`POST`
- 路径：`/index.php/api/CutVideo/create_indextts2`
- 文档：<https://s.apifox.cn/3cd5a990-f653-4555-9b72-0ac8741ba993/366986184e0.md>
- 参数：
  - `audio_url`（query，可选）：无说明；示例：`https://aiyuangongoss.oss-cn-beijing.aliyuncs.com/app%2Fbase%2F1_7fae925ebe654f8`
  - `text`（query，可选）：无说明；示例：`我媳妇当年跟我吵架，说“你就守着你那破烤炉过吧”，直到现在我都记得她当时红着眼眶的样子。刚开店那几年，她白天上班，晚上下班还要帮我穿串、收拾桌子，我总嫌她动作慢`
- 返回：`*/*` / `object`

### index2查询克隆结果
- 方法：`POST`
- 路径：`/index.php/api/CutVideo/search_indextts2`
- 文档：<https://s.apifox.cn/3cd5a990-f653-4555-9b72-0ac8741ba993/366986193e0.md>
- 参数：
  - `task_id`（query，可选）：无说明；示例：`1983532301609066497`
  - `token`（query，可选）：无说明
- 返回：`application/json` / `object`

## RPA
### 发送消息
- 方法：`POST`
- 路径：`/index.php/api/wss/onsend`
- 文档：<https://s.apifox.cn/3cd5a990-f653-4555-9b72-0ac8741ba993/296795607e0.md>
- 参数：
  - `uid`（query，可选）：无说明；示例：`3`
  - `content`（query，可选）：无说明；示例：`{
    "action": "send_message",
    "data": {
        "receiver": "文件传输助手",
`
- Body：`application/json` / `object`
- 返回：`application/json` / `object`

### 绑定uid通道
- 方法：`GET`
- 路径：`/index.php/api/wss/bind`
- 文档：<https://s.apifox.cn/3cd5a990-f653-4555-9b72-0ac8741ba993/296796492e0.md>
- 参数：
  - `uid`（query，可选）：无说明；示例：`19`
  - `client_id`（query，可选）：无说明
- 返回：`application/json` / `object`

### RPA发送消息
- 方法：`POST`
- 路径：`/index.php/api/Addons/xhs_userhome_data`
- 文档：<https://s.apifox.cn/3cd5a990-f653-4555-9b72-0ac8741ba993/249968584e0.md>
- 参数：
  - `token`（query，可选）：无说明；示例：`1651dgs163s`
  - `wenzhang`（query，可选）：无说明；示例：`dhbdfghxhtg`
  - `keywords`（query，可选）：无说明；示例：`62151651465`
  - `data`（query，可选）：无说明；示例：`[  "{\"auther_nick_name\":\"寒雨连江\",\"comment_content\":\"求带[哇R]\",\"comment_crea`
- 返回：`application/json` / `object`

### RPA发送服务器消息
- 方法：`POST`
- 路径：`/index.php/api/wss/toadmin`
- 文档：<https://s.apifox.cn/3cd5a990-f653-4555-9b72-0ac8741ba993/311834558e0.md>
- 参数：
  - `uid`（query，可选）：无说明；示例：`1`
  - `content`（query，可选）：无说明；示例：`1`
  - `touser`（query，可选）：无说明；示例：`1`
  - `togroup`（query，可选）：无说明；示例：`1`
- 返回：`*/*` / `object`

### 获取监听用户列表
- 方法：`GET`
- 路径：`/index.php/api/wss/toadmin`
- 文档：<https://s.apifox.cn/3cd5a990-f653-4555-9b72-0ac8741ba993/314438598e0.md>
- 参数：
  - `action`（query，可选）：无说明；示例：`get_listen_user`
  - `data`（query，可选）：无说明
  - `uid`（query，可选）：无说明；示例：`1`

### 向云端发送消息
- 方法：`POST`
- 路径：`/index.php/api/wss/toadmin`
- 文档：<https://s.apifox.cn/3cd5a990-f653-4555-9b72-0ac8741ba993/314450817e0.md>
- 参数：
  - `action`（query，可选）：无说明；示例：`to_message`
  - `data`（query，可选）：无说明；示例：`{"uid":"1","content":"\u6d4b\u8bd5","touser":"\u8d85\u7ea7\u674e","togroup":""}`
  - `uid`（query，可选）：无说明；示例：`1`
- Body：`application/json` / `object`
- 返回：`application/json` / `object`

### 本地登录
- 方法：`POST`
- 路径：`/index.php/api/wss/login`
- 文档：<https://s.apifox.cn/3cd5a990-f653-4555-9b72-0ac8741ba993/318122322e0.md>
- 参数：
  - `phone`（query，可选）：无说明；示例：`18625522203`
  - `password`（query，可选）：无说明；示例：`123456`
- 返回：`application/json` / `object`
  - 主要字段：code, msg

## 小程序
### 小程序获取access_token
- 方法：`POST`
- 路径：`/cgi-bin/token`
- 文档：<https://s.apifox.cn/3cd5a990-f653-4555-9b72-0ac8741ba993/276931534e0.md>
- 参数：
  - `grant_type`（query，可选）：无说明；示例：`client_credential`
  - `appid`（query，可选）：无说明；示例：`wx4cfa0c4b48b4f822`
  - `secret`（query，可选）：无说明；示例：`f919ee3ccc286a564f3a3eec434918fe`
- 返回：`application/json` / `object`

### 获取小程序跳转URL
- 方法：`POST`
- 路径：`/wxa/generatescheme`
- 文档：<https://s.apifox.cn/3cd5a990-f653-4555-9b72-0ac8741ba993/300240486e0.md>
- 参数：
  - `access_token`（query，可选）：无说明；示例：`92_JL3b-00ahbi3Zr8DGDw7ZiLwWEVGdaXmEdXuc5QRN-gJJkCrQRakfR0ts0eJBeUSYZ78X6KXp6aM_`
  - `jump_wxa`（query，可选）：无说明；示例：`{
    "path": "/pages/index/index",
    "query": "",
    "env_version": "rele`
- 返回：`application/json` / `object`
  - 主要字段：errcode, errmsg, openlink

## 小红书类
### 小红书采集关键词文章
- 方法：`POST`
- 路径：`/index.php/api/Addons/xhs_searchwenzhang`
- 文档：<https://s.apifox.cn/3cd5a990-f653-4555-9b72-0ac8741ba993/240486617e0.md>
- 参数：
  - `keyword`（query，可选）：无说明；示例：`郑州创业`
  - `page_count`（query，可选）：无说明；示例：`2`
  - `cookie`（query，可选）：无说明；示例：`abRequestId=1354a2a8-16ea-509c-91d4-2bfc710627b0; xsecappid=xhs-pc-web; a1=1974d`
  - `token`（query，可选）：无说明；示例：`2082b3e87116f4ffa95525e1c034dd53`
- 返回：`application/json` / `object`

### 小红书采集文章评论
- 方法：`POST`
- 路径：`/index.php/api/Addons/xhs_wenzhangpinglun`
- 文档：<https://s.apifox.cn/3cd5a990-f653-4555-9b72-0ac8741ba993/240552823e0.md>
- 参数：
  - `cookie`（query，可选）：无说明
  - `note_url`（query，可选）：无说明；示例：`https://www.xiaohongshu.com/explore/6749437a000000000202a4a9?xsec_token=AB9d12oA`
  - `token`（query，可选）：无说明；示例：`2082b3e87116f4ffa95525e1c034dd53`
- 返回：`application/json` / `object`

### 小红书采集用户主页数据
- 方法：`POST`
- 路径：`/index.php/api/Addons/xhs_userhome_data`
- 文档：<https://s.apifox.cn/3cd5a990-f653-4555-9b72-0ac8741ba993/249551508e0.md>
- 参数：
  - `token`（query，可选）：无说明；示例：`1111`
  - `data`（query，必填）：无说明；示例：`[{'auther_nick_name': '胖胖创业笔记', 'comment_user_home_page_url': 'https://www.xiaoh`
  - `wenzhang`（query，必填）：无说明；示例：`dsfgaewrf`
  - `keywords`（query，必填）：无说明；示例：`dddd`
- 返回：`application/json` / `object`

### 小红书文章采集(综合)
- 方法：`GET`
- 路径：`/index.php/api/Addons/xhs_search_note_list`
- 文档：<https://s.apifox.cn/3cd5a990-f653-4555-9b72-0ac8741ba993/389441137e0.md>
- 参数：
  - `keywords`（query，可选）：无说明；示例：`['郑州创业']`
  - `page`（query，可选）：无说明；示例：`1`
  - `sort_type`（query，可选）：无说明；示例：`general`
  - `search_id`（query，可选）：无说明
  - `session_id`（query，可选）：无说明
  - `filter_note_type`（query，可选）：无说明；示例：`不限`
  - `filter_note_time`（query，可选）：无说明；示例：`不限`
  - `token`（query，可选）：无说明；示例：`88a0bf1afa04176d313604c9f9ac65f8`
  - `Authorization`（header，可选）：无说明；示例：`Bearer xaEvQUR4nXQCmw4qiWyjxyYD5gsBsbOGortQ0Q7BrEp0/lxTWuVtmDi1Vw==`
- 返回：`*/*` / `object`

### 小红书采集用户主页
- 方法：`GET`
- 路径：`/index.php/api/Addons/xhs_search_users_datalist`
- 文档：<https://s.apifox.cn/3cd5a990-f653-4555-9b72-0ac8741ba993/389442573e0.md>
- 参数：
  - `user_id`（query，可选）：无说明；示例：`671b5117000000001d02177a`
  - `cursor`（query，可选）：无说明；示例：`1`
  - `token`（query，可选）：无说明；示例：`88a0bf1afa04176d313604c9f9ac65f8`
  - `Authorization`（header，可选）：无说明；示例：`Bearer xaEvQUR4nXQCmw4qiWyjxyYD5gsBsbOGortQ0Q7BrEp0/lxTWuVtmDi1Vw==`
- 返回：`*/*` / `object`

## 抖音类
### 抖音采集关键词文章(30s)
- 方法：`POST`
- 路径：`/index.php/api/Addons/douyin_search_articles`
- 文档：<https://s.apifox.cn/3cd5a990-f653-4555-9b72-0ac8741ba993/244019261e0.md>
- 参数：
  - `cookie`（query，可选）：无说明；示例：`UIFID_TEMP=e71d819f1cb72e7166823ce125547a3e5a83b631a52f7c0b3c34cd9714dd602d8a7e8`
  - `keyword`（query，必填）：关键词；示例：`创业`
  - `publish_time`（query，必填）：发布时间筛选
0: 不限
1: 最近一天
7: 最近一周
180: 最近半年；示例：`7`
  - `sort_type`（query，必填）：排序方式
0: 综合排序
1: 最多点赞
2: 最新发布；示例：`0`
  - `search_count`（query，必填）：无说明；示例：`2`
  - `token`（query，可选）：34aitoken；示例：`2082b3e87116f4ffa95525e1c034dd53`
- 返回：`application/json` / `object`

### 抖音采集文章评论
- 方法：`POST`
- 路径：`/index.php/api/Addons/douyin_get_comments`
- 文档：<https://s.apifox.cn/3cd5a990-f653-4555-9b72-0ac8741ba993/244019427e0.md>
- 参数：
  - `video_url`（query，可选）：无说明；示例：`https://www.douyin.com/video/7481852508013481268`
  - `cookie`（query，可选）：无说明；示例：`bd_ticket_guard_client_web_domain=2; UIFID_TEMP=60b2ef133e5e740633c50bb923c1ddfc`
  - `token`（query，可选）：无说明；示例：`2082b3e87116f4ffa95525e1c034dd53`
- 返回：`application/json` / `object`

### 抖音采集主页视频
- 方法：`POST`
- 路径：`/index.php/api/Addons/douyin_home_videolist`
- 文档：<https://s.apifox.cn/3cd5a990-f653-4555-9b72-0ac8741ba993/257654218e0.md>
- 参数：
  - `homeurl`（query，可选）：无说明；示例：`长按复制此条消息，打开抖音搜索，查看TA的更多作品。 https://v.douyin.com/oIlWhXHLaTE/`
  - `token`（query，可选）：无说明；示例：`2082b3e87116f4ffa95525e1c034dd53`
- 返回：`application/json` / `object`

### 抖音视频下载链接解析
- 方法：`POST`
- 路径：`/index.php/api/addons/douyin_videourl_jiexi`
- 文档：<https://s.apifox.cn/3cd5a990-f653-4555-9b72-0ac8741ba993/276411051e0.md>
- 参数：
  - `url`（query，可选）：无说明；示例：`https://www.douyin.com/video/7586268789983382843`
  - `token`（query，可选）：无说明；示例：`2082b3e87116f4ffa95525e1c034dd53`
- 返回：`application/json` / `object`

### 综合·抖音采集关键词文章（10s）
- 方法：`POST`
- 路径：`/index.php/api/Addons/fetchSearch`
- 文档：<https://s.apifox.cn/3cd5a990-f653-4555-9b72-0ac8741ba993/334587744e0.md>
- 参数：
  - `keyword`（query，必填）：关键词；示例：`创业`
  - `publish_time`（query，必填）：发布时间筛选
0: 不限
1: 最近一天
7: 最近一周
180: 最近半年；示例：`0`
  - `sort_type`（query，必填）：排序方式
0: 综合排序
1: 最多点赞
2: 最新发布；示例：`0`
  - `search_id`（query，可选）：34aitoken
  - `token`（query，可选）：无说明
  - `Authorization`（header，可选）：无说明；示例：`Bearer xaEvQUR4nXQCmw4qiWyjxyYD5gsBsbOGortQ0Q7BrEp0/lxTWuVtmDi1Vw==`
- Body：`application/json` / `object`
- 返回：`application/json` / `object`

### 综合·抖音采集关键词文章
- 方法：`POST`
- 路径：`/index.php/api/Addons/fetchVideoComments`
- 文档：<https://s.apifox.cn/3cd5a990-f653-4555-9b72-0ac8741ba993/334683217e0.md>
- 参数：
  - `aweme_id`（query，可选）：无说明；示例：`7581775386636717369`
  - `cursor`（query，必填）：关键词；示例：`0`
  - `token`（query，可选）：无说明；示例：`2082b3e87116f4ffa95525e1c034dd53`
- 返回：`application/json` / `object`

## 数字人
### 克隆音色
- 方法：`POST`
- 路径：`/index.php/api/CloneVoice/add`
- 文档：<https://s.apifox.cn/3cd5a990-f653-4555-9b72-0ac8741ba993/365943426e0.md>
- 参数：
  - `name`（query，可选）：无说明；示例：`测试`
  - `description`（query，可选）：无说明；示例：`描述内容`
  - `url`（query，可选）：无说明；示例：`https://jingdongai.oss-cn-hangzhou.aliyuncs.com/20250519/p_8dc5b62da3f556d6e41df`
  - `token`（query，可选）：无说明；示例：`6fe5acda7634be73ef6579361fe17bf2`
- 返回：`application/json` / `object`

### 克隆形象
- 方法：`POST`
- 路径：`/index.php/api/CloneScene/add`
- 文档：<https://s.apifox.cn/3cd5a990-f653-4555-9b72-0ac8741ba993/312243480e0.md>
- 参数：
  - `name`（query，可选）：无说明；示例：`克隆形象`
  - `url`（query，可选）：无说明；示例：`https://34ai.cc/a1833eae62b588e84cf44b6853a2d4e0.mp4`
  - `token`（query，可选）：无说明；示例：`2082b3e87116f4ffa95525e1c034dd53`
- 返回：`application/json` / `object`
  - 主要字段：code, msg, time, data

### 合成声音
- 方法：`POST`
- 路径：`/index.php/api/CreatedScene/voice`
- 文档：<https://s.apifox.cn/3cd5a990-f653-4555-9b72-0ac8741ba993/356218344e0.md>
- 参数：
  - `voice_id`（query，可选）：无说明；示例：`cosyvoice-v1-hlyiyqix-d321dab401944ab1b375194492cda0a8`
  - `text`（query，可选）：无说明；示例：`您好，请问您是想咨询关于广告投放问题吗？`
  - `token`（query，可选）：无说明；示例：`c014248044672759672057f2086f1d7b`
- 返回：`application/json` / `object`

### 合成vlogo 视频
- 方法：`POST`
- 路径：`/index.php/api/vlog/submit`
- 文档：<https://s.apifox.cn/3cd5a990-f653-4555-9b72-0ac8741ba993/312253213e0.md>
- 参数：
  - `token`（query，可选）：34ai 获取；示例：`2082b3e87116f4ffa95525e1c034dd53`
  - `lensList`（query，可选）：镜头列表，按数组下标区分分镜，下标0表示分镜1；[["video"=>'镜头1视频链接',"scene"=>'镜头1'场景scene_task_id]]；统一镜头视频链接与场景传一个；示例：`[{"video":"https:\/\/yc-digital-human-cdn-cn.xhadmin.cn\/dreamapi\/o\/2025-05-21`
  - `voice_id`（query，可选）：音色id；示例：`cosyvoice-v1-uxlgqhsh-91db1b352f924504a9f1d73b366cfa03`
  - `copywrite`（query，可选）：文案；示例：`秋天，这个字眼本身就蕴含着收获与成熟。它是一年四季中的第三季度，通常在北半球从9月22日或23日开始`
  - `package`（query，可选）：font：字体，size：字体大小，color：字体颜色，x：横向距离，y纵向距离；示例：`{"font":"SimSun","size":"30","color":"#666666"}`
- 返回：`application/json` / `object`
  - 主要字段：code, msg, time, data

### 合成数字人
- 方法：`POST`
- 路径：`/index.php/api/CreatedScene/add`
- 文档：<https://s.apifox.cn/3cd5a990-f653-4555-9b72-0ac8741ba993/365943352e0.md>
- 参数：
  - `scene_task_id`（query，可选）：无说明；示例：`784724`
  - `name`（query，可选）：无说明；示例：`1`
  - `audio_url`（query，可选）：无说明；示例：`https://chat.34ai.cc/aliyun/CosyVoice/tts_84bb3211.mp3`
  - `token`（query，可选）：无说明；示例：`6fe5acda7634be73ef6579361fe17bf2`
  - `token`（header，可选）：无说明；示例：`6fe5acda7634be73ef6579361fe17bf2`
- 返回：`application/json` / `object`

### 查询数字人
- 方法：`POST`
- 路径：`/index.php/api/CreatedScene/getListByTaskId`
- 文档：<https://s.apifox.cn/3cd5a990-f653-4555-9b72-0ac8741ba993/365943402e0.md>
- 参数：
  - `video_task_id`（query，可选）：无说明；示例：`795115`
  - `token`（query，可选）：无说明；示例：`71fc14b820123d323bc14e49cd95fa45`
  - `token`（header，可选）：无说明；示例：`6fe5acda7634be73ef6579361fe17bf2`
- 返回：`application/json` / `object`
  - 主要字段：code, msg, time, data

### 音色列表
- 方法：`POST`
- 路径：`/index.php/api/CloneVoice/getList`
- 文档：<https://s.apifox.cn/3cd5a990-f653-4555-9b72-0ac8741ba993/365943440e0.md>
- 参数：
  - `page`（query，可选）：无说明；示例：`1`
  - `pagesize`（query，可选）：无说明；示例：`1`
  - `token`（query，可选）：无说明；示例：`6fe5acda7634be73ef6579361fe17bf2`
- 返回：`application/json` / `object`

### 形象列表
- 方法：`POST`
- 路径：`/index.php/api/CloneScene/getList`
- 文档：<https://s.apifox.cn/3cd5a990-f653-4555-9b72-0ac8741ba993/365945528e0.md>
- 参数：
  - `token`（query，可选）：无说明；示例：`6fe5acda7634be73ef6579361fe17bf2`
  - `page`（query，可选）：无说明；示例：`1`
  - `pagesize`（query，可选）：无说明；示例：`1`
- 返回：`application/json` / `object`
  - 主要字段：code, msg, time, data

### 音频裁剪
- 方法：`POST`
- 路径：`/index.php/api/CutVideo/crop`
- 文档：<https://s.apifox.cn/3cd5a990-f653-4555-9b72-0ac8741ba993/363014398e0.md>
- 参数：
  - `audio_url`（query，可选）：无说明；示例：`https://chat.34ai.cc/aliyun/CosyVoice/tts_2ba9061d.mp3`
  - `start`（query，可选）：无说明；示例：`0.10`
  - `end`（query，可选）：无说明；示例：`0.20`

## 测试
### MCP操作
- 方法：`POST`
- 路径：`/api/admin/robot/robotList/robotAction`
- 文档：<https://s.apifox.cn/3cd5a990-f653-4555-9b72-0ac8741ba993/359875179e0.md>
- 参数：
  - `uid`（query，可选）：无说明；示例：`2`
  - `action`（query，可选）：无说明；示例：`4`
  - `data`（query，可选）：无说明
- Body：`application/json` / `object`
- 返回：`application/json` / `object`

### 算力记录
- 方法：`POST`
- 路径：`/api/flow/tokenLogDetail/postTokenDetail`
- 文档：<https://s.apifox.cn/3cd5a990-f653-4555-9b72-0ac8741ba993/362262368e0.md>
- 参数：文档未声明或为空
- Body：`application/json` / `object`
- 返回：`application/json` / `object`
  - 主要字段：code, message

### 算力回调
- 方法：`POST`
- 路径：`/index.php/api/CutVideo/agent_run_cutvideo`
- 文档：<https://s.apifox.cn/3cd5a990-f653-4555-9b72-0ac8741ba993/370165350e0.md>
- 参数：
  - `id`（query，可选）：无说明；示例：`279`
  - `draft_id`（query，可选）：无说明；示例：`dfd_cat_1761821003_6f2f17a5`
  - `draft_url`（query，可选）：无说明；示例：`https://cn.capcutapi.top/draft/downloader?draft_id=dfd_cat_1761821003_6f2f17a5&a`
  - `suanli_total`（query，可选）：无说明；示例：`12.72`
  - `digital_suanli_total`（query，可选）：无说明；示例：`4.24`
- 返回：`*/*` / `object`

### 获取云端数据
- 方法：`GET`
- 路径：`/index.php/api/CutVideo/getlist`
- 文档：<https://s.apifox.cn/3cd5a990-f653-4555-9b72-0ac8741ba993/368100888e0.md>
- 参数：
  - `phone`（query，可选）：无说明；示例：`18625522203`
  - `video_material`（query，可选）：无说明；示例：`42`
- 返回：`application/json` / `object`
  - 主要字段：category, video_list, music, yinxiao, sceneTaskId, voice, voiceurl

## 蜂巢智工
### RPA登录
- 方法：`POST`
- 路径：`/index.php/api/wss/fiveai_login`
- 文档：<https://s.apifox.cn/3cd5a990-f653-4555-9b72-0ac8741ba993/387215579e0.md>
- 参数：
  - `phone`（query，可选）：无说明；示例：`18625522203`
  - `password`（query，可选）：无说明；示例：`123456`
- Body：`application/json` / `object`
- 返回：`application/json` / `object`
  - 主要字段：code, msg

### RPA登录绑定
- 方法：`POST`
- 路径：`/index.php/api/wss/fiveai_bind`
- 文档：<https://s.apifox.cn/3cd5a990-f653-4555-9b72-0ac8741ba993/387216144e0.md>
- 参数：
  - `phone`（query，可选）：无说明；示例：`18625522203`
  - `password`（query，可选）：无说明；示例：`123456`
- Body：`application/json` / `object`
- 返回：`application/json` / `object`
  - 主要字段：code, msg

### RPA发送指令(采集)
- 方法：`POST`
- 路径：`/index.php/api/wss/fiveai_to_send`
- 文档：<https://s.apifox.cn/3cd5a990-f653-4555-9b72-0ac8741ba993/387236854e0.md>
- 参数：
  - `phone`（query，可选）：无说明；示例：`18625522203`
  - `password`（query，可选）：无说明；示例：`123456`
- Body：`application/json` / `object`
- 返回：`application/json` / `object`
  - 主要字段：code, msg

### RPA发送指令(自动评论)
- 方法：`POST`
- 路径：`/index.php/api/wss/fiveai_to_send`
- 文档：<https://s.apifox.cn/3cd5a990-f653-4555-9b72-0ac8741ba993/402776666e0.md>
- 参数：
  - `phone`（query，可选）：无说明；示例：`18625522203`
  - `password`（query，可选）：无说明；示例：`123456`
- Body：`application/json` / `object`
- 返回：`application/json` / `object`
  - 主要字段：code, msg

### RPA发送指令(发起私信)
- 方法：`POST`
- 路径：`/index.php/api/wss/fiveai_to_send`
- 文档：<https://s.apifox.cn/3cd5a990-f653-4555-9b72-0ac8741ba993/401553735e0.md>
- 参数：
  - `phone`（query，可选）：无说明；示例：`18625522203`
  - `password`（query，可选）：无说明；示例：`123456`
- Body：`application/json` / `object`
- 返回：`application/json` / `object`
  - 主要字段：code, msg

### RPA发送指令(发布视频)
- 方法：`POST`
- 路径：`/index.php/api/wss/fiveai_to_send`
- 文档：<https://s.apifox.cn/3cd5a990-f653-4555-9b72-0ac8741ba993/400434712e0.md>
- 参数：
  - `phone`（query，可选）：无说明；示例：`18625522203`
  - `password`（query，可选）：无说明；示例：`123456`
- Body：`application/json` / `object`
- 返回：`application/json` / `object`
  - 主要字段：code, msg

### RPA发送指令(剪映剪辑)
- 方法：`POST`
- 路径：`/index.php/api/wss/fiveai_to_send`
- 文档：<https://s.apifox.cn/3cd5a990-f653-4555-9b72-0ac8741ba993/405847816e0.md>
- 参数：
  - `phone`（query，可选）：无说明；示例：`18625522203`
  - `password`（query，可选）：无说明；示例：`123456`
- Body：`application/json` / `object`
- 返回：`application/json` / `object`
  - 主要字段：code, msg

### RPA上传采集成功数据
- 方法：`POST`
- 路径：`/api/admin/aiEmployee/task/taskSuccess`
- 文档：<https://s.apifox.cn/3cd5a990-f653-4555-9b72-0ac8741ba993/389661091e0.md>
- 参数：
  - `request_id`（query，可选）：无说明；示例：`654376436`
  - `up_data`（query，可选）：无说明；示例：`456456`
- Body：`application/json` / `object`
- 返回：`application/json` / `object`

### 发布账号管理
- 方法：`POST`
- 路径：`/api/admin/rpaApi/autoSendDetail/receiveData`
- 文档：<https://s.apifox.cn/3cd5a990-f653-4555-9b72-0ac8741ba993/400974524e0.md>
- 参数：文档未声明或为空
- Body：`application/json` / `object`
- 返回：`application/json` / `object`

### 蜂巢智工·剪辑完成保存草稿
- 方法：`POST`
- 路径：`/api/admin/aiEmployee/task/postJyData`
- 文档：<https://s.apifox.cn/3cd5a990-f653-4555-9b72-0ac8741ba993/406153286e0.md>
- 参数：文档未声明或为空
- Body：`application/json` / `object`
- 返回：`application/json` / `object`

### 自动剪辑
- 方法：`POST`
- 路径：`/index.php/api/cutapi/autocut`
- 文档：<https://s.apifox.cn/3cd5a990-f653-4555-9b72-0ac8741ba993/400969903e0.md>
- 参数：
  - `draft_folder`（query，可选）：无说明；示例：`F:\jianying\JianyingPro Drafts`
  - `wenan_list`（query，可选）：无说明；示例：`你问我46岁开全羊馆值不值？我实话告诉你，有时候累得想砸店，但看着那些老客吃得满足的样子，又觉得值。 前几天有个熟客来，笑着说“陈哥你现在是大老板了，不用那么拼`
  - `phone`（query，可选）：无说明；示例：`18625522203`
  - `video_material`（query，可选）：无说明；示例：`42`
  - `token`（query，可选）：无说明；示例：`88a0bf1afa04176d313604c9f9ac65f8`
  - `taskid`（query，可选）：无说明；示例：`123456`
  - `is_background_music`（query，可选）：无说明；示例：`1`
  - `is_voice_effect`（query，可选）：无说明；示例：`0`
  - `pangbai`（query，可选）：无说明；示例：`https://34ai.cc/indextts2/flac_6909920392816.mp3`
- Body：`application/json` / `object`
- 返回：`application/json` / `object`
