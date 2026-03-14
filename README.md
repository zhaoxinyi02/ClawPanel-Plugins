<div align="center">

# ClawPanel-Plugins

**ClawPanel 官方插件与技能仓库 — OpenClaw 扩展生态中心**

[![ClawPanel](https://img.shields.io/badge/ClawPanel-v5.0.3-violet?style=flat-square)](https://github.com/zhaoxinyi02/ClawPanel)
[![License](https://img.shields.io/badge/license-MIT-green?style=flat-square)](LICENSE)
[![Plugins](https://img.shields.io/badge/plugins-1-blue?style=flat-square)](#插件列表)

[插件开发指南](https://github.com/zhaoxinyi02/ClawPanel/blob/main/docs/plugin-dev/README.md) · [ClawPanel 主仓库](https://github.com/zhaoxinyi02/ClawPanel) · [提交插件](#提交插件)

</div>

---

## 简介

本仓库是 [ClawPanel](https://github.com/zhaoxinyi02/ClawPanel) 的官方插件与技能仓库。

- `registry.json`：供插件中心读取插件列表
- `skills/registry.json`：供技能中心读取自定义技能列表

你后续可以把自己的特色技能放到 `skills/` 目录，并通过 ClawPanel 的技能市场让用户一键安装。

## 目录结构

```
ClawPanel-Plugins/
├── registry.json           # 插件注册表（ClawPanel 读取此文件）
├── skills/
│   ├── registry.json       # 自定义技能注册表
│   ├── _template/          # 自定义技能模板（含配置项声明示例）
│   └── ...                 # 你的自定义技能
├── official/               # 官方插件
│   └── hello-world/        # 示例插件
│       ├── plugin.json     # 插件元数据
│       └── index.js        # 插件入口
├── community/              # 社区贡献插件
│   └── (你的插件)/
├── schemas/
│   └── plugin.schema.json  # plugin.json 的 JSON Schema 定义
└── README.md
```

## 插件列表

### 官方插件

| 插件 | 版本 | 分类 | 说明 |
|:---|:---:|:---:|:---|
| [hello-world](official/hello-world/) | v1.0.0 | 基础 | 最小化示例插件，演示插件开发规范 |

### 社区插件

暂无，欢迎提交你的第一个插件！

## 安装插件

### 方式一：通过 ClawPanel 插件中心（推荐）

1. 打开 ClawPanel → 插件中心
2. 浏览插件市场
3. 点击「安装」即可

### 方式二：自定义 URL 安装

1. 打开 ClawPanel → 插件中心 → 「自定义安装」
2. 输入插件的 Git 仓库 URL 或 zip 下载链接
3. 点击安装

### 方式三：手动安装

将插件目录放入 OpenClaw 的 `extensions/` 目录，然后在 ClawPanel 中刷新插件列表。

## 提交插件

欢迎所有开发者提交插件！提交流程：

1. **Fork** 本仓库
2. 在 `community/` 目录下创建你的插件目录
3. 确保包含完整的 `plugin.json`（参考 [JSON Schema](schemas/plugin.schema.json)）
4. 编写 `README.md` 说明文档
5. 在 `registry.json` 的 `plugins` 数组中添加你的插件信息
6. 提交 **Pull Request**

### 审核清单

- [ ] `plugin.json` 包含必需字段（id, name, version, author, description）
- [ ] `id` 全小写，使用连字符分隔，全局唯一
- [ ] 包含 `README.md` 说明文档
- [ ] 代码无恶意行为（如未经授权的网络请求、文件删除等）
- [ ] 声明了所有必要权限
- [ ] 无硬编码 API Key / Token / 密码
- [ ] 版本号遵循语义化版本（SemVer）

## 开发插件

详细的插件开发指南请参阅：

📖 **[插件开发完整指南](https://github.com/zhaoxinyi02/ClawPanel/blob/main/docs/plugin-dev/README.md)**

内容包括：
- 插件目录结构和 `plugin.json` 规范
- JSON Schema 配置系统（自动生成前端表单）
- PluginContext API（消息处理、任务调度、存储、HTTP 等）
- 插件生命周期（安装 → 激活 → 运行 → 停用 → 卸载）
- 权限系统和冲突检测
- 调试与测试方法
- 示例插件代码

## registry.json 格式

```json
{
  "version": "1.0.0",
  "updatedAt": "2026-02-26T00:00:00Z",
  "plugins": [
    {
      "id": "plugin-id",
      "name": "插件名称",
      "version": "1.0.0",
      "author": "作者",
      "description": "一句话描述",
      "category": "basic|ai|message|fun|tool",
      "tags": ["标签1", "标签2"],
      "gitUrl": "https://github.com/user/plugin.git",
      "downloadUrl": "https://example.com/plugin.zip",
      "homepage": "https://github.com/user/plugin"
    }
  ]
}
```

## 许可证

本仓库中的官方插件采用 [MIT License](LICENSE)。

社区插件的许可证由各插件作者自行确定，请查看各插件目录中的 `LICENSE` 文件。

---

*© 2025 ClawPanel Team*
## 自定义技能市场

ClawPanel 的技能中心会优先从这个仓库读取：

- GitHub：`skills/registry.json`
- 失败时回退到 Gitee 镜像

每个技能建议至少包含：

- `id`
- `name`
- `description`
- `version`
- `author`
- `tags`
- `path`
- `files`

如果技能需要用户配置参数（例如 `apiKey`、`baseUrl`、`modelId`），建议在技能目录里的 `skill.json` 里声明 `config` 数组。

参考模板：

- `skills/_template/SKILL.md`
- `skills/_template/skill.json`
