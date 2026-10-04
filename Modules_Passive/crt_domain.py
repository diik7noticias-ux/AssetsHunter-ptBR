#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
# Consulta Certificate Transparency.
# Usa crt.sh (wildcard %25) com fallback para Cert Spotter.

import time
import requests
from Config.config_requests import headers
from Core.decorators import Save_info

CRTSH_URL = "https://crt.sh/?q=%25.{domain}&output=json"
CERTSPOTTER_URL = "https://api.certspotter.com/v1/issuances?domain={domain}&include_subdomains=true&expand=dns_names"


def _get_json(url, tentativas=5):
    for i in range(tentativas):
        try:
            r = requests.get(url, headers=headers, timeout=60)
            if r.status_code == 200:
                return r.json()
            # 404/429/5xx do crt.sh são transitórios
            if r.status_code in (404, 429, 500, 502, 503, 504):
                print(f"  Tentativa {i+1}: HTTP {r.status_code} (retry)")
        except Exception as e:
            print(f"  Tentativa {i+1} falhou: {type(e).__name__}")
        if i < tentativas - 1:
            time.sleep(2 ** i)  # backoff: 1s, 2s, 4s, 8s
    return None


def _crtsh(domain):
    data = _get_json(CRTSH_URL.format(domain=domain))
    if not data:
        return set()
    out = set()
    for item in data:
        for d in item.get('name_value', '').split('\n'):
            d = d.strip().lower()
            if d and '*' not in d:
                out.add(d)
    return out


def _certspotter(domain):
    data = _get_json(CERTSPOTTER_URL.format(domain=domain))
    if not data:
        return set()
    out = set()
    for item in data:
        for d in item.get('dns_names', []):
            d = d.strip().lower()
            if d and '*' not in d:
                out.add(d)
    return out


@Save_info
def Crt_domain(domain):
    print(f"Consultando crt.sh para {domain}...")
    dominios = _crtsh(domain)

    if not dominios:
        print("crt.sh não respondeu. Tentando Cert Spotter...")
        dominios = _certspotter(domain)

    resultado = sorted(dominios)
    print(f"Subdomínios encontrados: {len(resultado)}")
    for d in resultado[:50]:
        print(d)
    if len(resultado) > 50:
        print(f"... e mais {len(resultado) - 50}")
    return resultado


def run(domain):
    Crt_domain(domain)


if __name__ == '__main__':
    run("google.com")
