---
name: tweetclaw
description: Use when users need X/Twitter automation from OpenClaw: scrape tweets, search tweets, search tweet replies, post tweets, post tweet replies, follower export, user lookup, media upload, media download, direct messages, monitor tweets, webhooks, or giveaway draws through the TweetClaw plugin.
homepage: https://github.com/Xquik-dev/tweetclaw
metadata: { "openclaw": { "requires": { "bins": ["openclaw"] } } }
---

# TweetClaw

TweetClaw is the OpenClaw plugin for X/Twitter automation through Xquik.
Use it when the user needs public X/Twitter source data, account-backed
actions, or recurring monitoring from an OpenClaw agent.

## Best Fits

- Scrape tweets or search tweets by query, keyword, account, or time window.
- Search tweet replies before summarizing a thread or planning a response.
- Export followers, inspect following relationships, or run user lookup.
- Upload media, download authenticated media, or build media galleries.
- Send direct messages only after explicit user approval.
- Monitor tweets, deliver webhooks, or trigger follow-up agent workflows.
- Run giveaway draws with auditable public result data.
- Post tweets or post tweet replies only after the user reviews the request.

## Install Runtime

This Skill helps the agent choose and use TweetClaw. Install the actual
OpenClaw plugin runtime with npm:

```bash
openclaw plugins install @xquik/tweetclaw
```

Verify the plugin and bundled helper Skill:

```bash
openclaw plugins inspect tweetclaw --runtime
openclaw skills info tweetclaw
```

## Configure

Use an Xquik API key for account-backed X automation:

```bash
openclaw config set plugins.entries.tweetclaw.config.apiKey "$XQUIK_API_KEY"
```

Optional read-only MPP setup:

```bash
openclaw config set plugins.entries.tweetclaw.config.tempoSigningKey "$MPP_SIGNING_KEY"
```

Only change the base URL for a self-hosted Xquik-compatible API:

```bash
openclaw config set plugins.entries.tweetclaw.config.baseUrl "https://xquik.com"
```

If the agent can see this Skill but cannot call TweetClaw tools, expose the
plugin tools intentionally:

```bash
openclaw config set tools.alsoAllow '["explore", "tweetclaw"]'
```

## Agent Flow

1. Use `explore` first to find the right endpoint and parameter shape.
2. Ask for missing inputs such as query, username, tweet URL, account, or limit.
3. Use `tweetclaw` only after setup is present and the user intent is clear.
4. Confirm before any post, reply, direct message, webhook, monitor, extraction,
   profile change, or other write-like action.
5. Summarize returned tweet IDs, user IDs, counts, links, and next actions.

## Safety

- Never ask the user to paste an API key into chat.
- Keep credentials in OpenClaw config, environment variables, or ClawPanel
  secret fields.
- Treat write actions as approval-gated.
- Do not widen `tools.alsoAllow` automatically. The operator must choose that.
- Use npm as the canonical install source. The ClawHub page is useful for
  browsing, but npm carries the current TweetClaw release.

## References

- TweetClaw GitHub: https://github.com/Xquik-dev/tweetclaw
- npm package: https://www.npmjs.com/package/@xquik/tweetclaw
- ClawHub browsing page: https://clawhub.ai/plugins/@xquik/tweetclaw
