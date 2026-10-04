#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Enumeração de subdomínios via fontes públicas (sem API key).
import requests
from Config.config_requests import headers
from Core.decorators import Save_info


def _hackertarget(domain):
    try:
        r = requests.get(f"https://api.hackertarget.com/hostsearch/?q={domain}", timeout=30)
        if r.status_code == 200 and 'error' not in r.text.lower():
            return {l.split(',')[0].strip().lower() for l in r.text.strip().split('\n') if ',' in l}
    except Exception:
        pass
    return set()


def _otx(domain):
    try:
        r = requests.get(f"https://otx.alienvault.com/api/v1/indicators/domain/{domain}/passive_dns", timeout=30)
        if r.status_code == 200:
            return {i['hostname'].lower() for i in r.json().get('passive_dns', []) if i.get('hostname')}
    except Exception:
        pass
    return set()


def _crtsh(domain):
    try:
        r = requests.get(f"https://crt.sh/?q=%25.{domain}&output=json", timeout=60)
        if r.status_code == 200:
            subs = set()
            for item in r.json():
                for d in item.get('name_value', '').split('\n'):
                    d = d.strip().lower()
                    if d and '*' not in d and d.endswith(domain):
                        subs.add(d)
            return subs
    except Exception:
        pass
    return set()


@Save_info
def Subfinder(domain):
    print(f"Enumerando subdomínios de {domain}...")
    todos = set()
    for nome, fn in [('HackerTarget', _hackertarget), ('AlienVault OTX', _otx), ('crt.sh', _crtsh)]:
        print(f"  Consultando {nome}...")
        try:
            subs = fn(domain)
            print(f"    -> {len(subs)} encontrados")
            todos.update(subs)
        except Exception as e:
            print(f"    -> Erro: {e}")
    resultado = sorted(todos)
    print(f"\nTotal de subdomínios únicos: {len(resultado)}")
    for s in resultado[:100]:
        print(s)
    if len(resultado) > 100:
        print(f"... e mais {len(resultado) - 100}")
    return resultado


def run(domain):
    Subfinder(domain)


if __name__ == '__main__':
    run('example.com')
