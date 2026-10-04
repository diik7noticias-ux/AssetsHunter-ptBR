#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# URLs antigas arquivadas via Wayback Machine (archive.org).
import requests
from Config.config_requests import headers
from Core.decorators import Save_info


@Save_info
def Wayback(domain):
    url = (f"http://web.archive.org/cdx/search/cdx?url={domain}/*"
           f"&output=json&fl=original&collapse=urlkey&limit=500")
    print(f"Consultando Wayback Machine para {domain}...")
    try:
        r = requests.get(url, headers=headers, timeout=90)
        if r.status_code != 200:
            print(f"HTTP {r.status_code}")
            return []
        data = r.json()
        urls = sorted(set(row[0] for row in data[1:])) if len(data) > 1 else []
        print(f"URLs arquivadas: {len(urls)}")
        for u in urls[:100]:
            print(u)
        if len(urls) > 100:
            print(f"... e mais {len(urls) - 100}")
        return urls
    except Exception as e:
        print(f"Erro: {e}")
        return []


def run(domain):
    Wayback(domain)


if __name__ == '__main__':
    run('example.com')
