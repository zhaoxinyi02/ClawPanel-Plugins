#!/usr/bin/env python3
import json
import re
import sys
import time
from html import unescape
from urllib.parse import urlparse

try:
    import requests
except ImportError:
    print(json.dumps({"ok": False, "error": "Missing dependency: requests"}, ensure_ascii=False))
    sys.exit(1)

DEFAULT_HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
}


def strip_html(html: str) -> str:
    html = re.sub(r"<script[\\s\\S]*?</script>", " ", html, flags=re.I)
    html = re.sub(r"<style[\\s\\S]*?</style>", " ", html, flags=re.I)
    html = re.sub(r"<[^>]+>", " ", html)
    html = unescape(html)
    html = re.sub(r"\\s+", " ", html).strip()
    return html


def extract_title(html: str) -> str:
    match = re.search(r"<title[^>]*>(.*?)</title>", html, flags=re.I | re.S)
    if not match:
        return ""
    return re.sub(r"\\s+", " ", unescape(match.group(1))).strip()


def fetch(url: str, delay_ms: int = 800, timeout: int = 15) -> dict:
    parsed = urlparse(url)
    if parsed.scheme not in {"http", "https"}:
        return {"ok": False, "error": "Only http/https URLs are supported"}

    time.sleep(max(delay_ms, 0) / 1000)
    resp = requests.get(url, headers=DEFAULT_HEADERS, timeout=timeout)
    resp.raise_for_status()
    html = resp.text
    text = strip_html(html)
    return {
        "ok": True,
        "url": resp.url,
        "status": resp.status_code,
        "title": extract_title(html),
        "content": text[:12000],
        "contentLength": len(text),
    }


def main():
    if len(sys.argv) < 2:
        print(json.dumps({"ok": False, "error": "Usage: index.py <url> [delay_ms]"}, ensure_ascii=False))
        sys.exit(1)

    url = sys.argv[1]
    delay_ms = int(sys.argv[2]) if len(sys.argv) > 2 else 800
    try:
        result = fetch(url, delay_ms=delay_ms)
    except Exception as exc:
        result = {"ok": False, "error": str(exc)}
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
