#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Consulta pública do URLScan.io (sem API key).
import requests
from Config.config_requests import headers
from Core.decorators import Save_info


@Save_info
def Urlscan(domain):
    url = f"https://urlscan.io/api/v1/search/?q=domain:{domain}&size=100"
    print(f"Consultando URLScan.io para {domain}...")
    try:
        r = requests.get(url, headers=headers, timeout=30)
        if r.status_code != 200:
            print(f"HTTP {r.status_code}")
            return []
        results = r.json().get('results', [])
        saida = []
        for item in results:
            page = item.get('page', {})
            linha = f"{page.get('url','-')} | IP: {page.get('ip','-')} | Server: {page.get('server','-')}"
            saida.append(linha)
        print(f"Resultados: {len(saida)}")
        for l in saida[:50]:
            print(l)
        return saida
    except Exception as e:
        print(f"Erro: {e}")
        return []


def run(domain):
    Urlscan(domain)


if __name__ == '__main__':
    run('example.com')
