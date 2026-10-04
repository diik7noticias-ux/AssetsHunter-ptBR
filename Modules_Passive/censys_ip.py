#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
# Censys API v2 (a v1 foi descontinuada em 2022).
# Crie conta grátis em https://search.censys.io
# Gere API ID e Secret em https://search.censys.io/account/api

import requests
from Config.config_censys import API_ID, API_SECRET
from Core.decorators import Save_info

BASE = "https://search.censys.io/api/v2"


@Save_info
def Censys_ip(ip):
    if API_ID == "API_ID" or API_SECRET == "API_SECRET":
        print("⚠️  Configure API_ID e API_SECRET em Config/config_censys.py")
        return []

    url = f"{BASE}/hosts/{ip}"
    try:
        r = requests.get(url, auth=(API_ID, API_SECRET), timeout=15)
        if r.status_code == 404:
            print(f"IP não encontrado no Censys: {ip}")
            return []
        if r.status_code == 401:
            print("Credenciais inválidas (API_ID/API_SECRET).")
            return []
        if r.status_code != 200:
            print(f"Erro HTTP {r.status_code}: {r.text[:200]}")
            return []

        data = r.json().get('result', {})
        resultado = []
        resultado.append(f"IP: {ip}")
        resultado.append(f"País: {data.get('location', {}).get('country', '-')}")
        resultado.append(f"ASN: {data.get('autonomous_system', {}).get('asn', '-')}")
        resultado.append(f"Descrição: {data.get('autonomous_system', {}).get('description', '-')}")
        for svc in data.get('services', []):
            porta = svc.get('port')
            nome = svc.get('service_name', '-')
            resultado.append(f"  Serviço: porta {porta} ({nome})")
        for linha in resultado:
            print(linha)
        return resultado
    except Exception as e:
        print(f"Erro ao consultar Censys: {e}")
        return []


def run(ip):
    Censys_ip(ip)


if __name__ == '__main__':
    run('8.8.8.8')
