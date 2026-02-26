# Hello World 示例插件

这是一个最小化的 OpenClaw 插件示例，用于演示插件的基本结构和开发规范。

## 功能

- 监听消息，当收到 `/hello` 时自动回复问候语
- 支持自定义问候语和触发关键词
- 演示 `activate` / `deactivate` / `onConfigChange` 生命周期

## 配置

| 字段 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| greeting | string | 你好！我是 OpenClaw 插件 👋 | 自定义问候语 |
| trigger | string | /hello | 触发关键词 |
| enabled | boolean | true | 是否启用自动回复 |

## 安装

在 ClawPanel 插件中心搜索 `hello-world` 并安装，或使用自定义安装输入本仓库地址。

## 开发参考

- [插件开发完整指南](https://github.com/zhaoxinyi02/ClawPanel/blob/main/docs/plugin-dev/README.md)
- [plugin.json JSON Schema](../../schemas/plugin.schema.json)
