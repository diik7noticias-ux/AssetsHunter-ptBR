#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Probe de hosts vivos (HTTPX).
import asyncio
import os
import re

import httpx

from Config.config_requests import headers

requests_not_used = None
TITLE_RE = re.compile(r'<title[^>]*>(.*?)</title>', re.IGNORECASE | re.DOTALL)


async def _probe(client, url):
    try:
        r = await client.get(url, timeout=10)
        m = TITLE_RE.findall(r.text)
        title = m[0].strip()[:80] if m else ''
        server = r.headers.get('Server', '-')
        return f"{url} [{r.status_code}] server={server} title={title}"
    except Exception:
        return None


async def _run_all(urls):
    out = []
    async with httpx.AsyncClient(verify=False, follow_redirects=True) as client:
        tasks = [_probe(client, u) for u in urls]
        for coro in asyncio.as_completed(tasks):
            r = await coro
            if r:
                print(r)
                out.append(r)
    return out


def Probe(alvo):
    if os.path.isfile(alvo):
        with open(alvo) as f:
            urls = [l.strip() for l in f if l.strip()]
    elif ',' in alvo:
        urls = [u.strip() for u in alvo.split(',')]
    else:
        urls = [alvo]
    urls = [u if u.startswith('http') else 'http://' + u for u in urls]
    print(f"Probing {len(urls)} alvo(s)...")
    return asyncio.run(_run_all(urls))


def run(alvo):
    Probe(alvo)


if __name__ == '__main__':
    Probe('example.com')
