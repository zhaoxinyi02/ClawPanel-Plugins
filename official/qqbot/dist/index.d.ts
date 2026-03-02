import type { MoltbotPluginApi } from "clawdbot/plugin-sdk";
declare const plugin: {
    id: string;
    name: string;
    description: string;
    register(api: MoltbotPluginApi): void;
};
export default plugin;
export { qqbotPlugin } from "./src/channel.js";
export { setQQBotRuntime, getQQBotRuntime } from "./src/runtime.js";
export { qqbotOnboardingAdapter } from "./src/onboarding.js";
export * from "./src/types.js";
export * from "./src/api.js";
export * from "./src/config.js";
export * from "./src/gateway.js";
export * from "./src/outbound.js";
