#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
# Detecção WEB em CIDR ou arquivo.
# Versão otimizada com httpx (async).

import asyncio
import re

import httpx

from Config.config_hawkeye import Port_HTTP, Port_HTTPS
from Config.config_requests import headers
from Core.decorators import Save_info
from Tools.cidr_ip import Cidr_ips


def urlcheck(url):
    if 'http' in url:
        return url
    return 'http://' + str(url)


def Get_urls(cidr):
    urls = []
    try:
        ips = Cidr_ips(cidr)
        for ip in ips:
            for p in Port_HTTP:
                urls.append(f'http://{ip}:{p}')
            for p in Port_HTTPS:
                urls.append(f'https://{ip}:{p}')
    except Exception:
        pass
    return urls


TITLE_RE = re.compile(r'<title.*?>(.*?)</title>', re.IGNORECASE | re.DOTALL)


async def checar(client, url):
    try:
        r = await client.get(url, headers=headers, timeout=10)
        m = TITLE_RE.findall(r.text)
        if m:
            titulo = m[0].strip()[:80]
            linha = f'{url} {r.status_code} {titulo}'
        else:
            corpo = r.text.replace('\n', '')[:30]
            linha = f'{url} {r.status_code} {corpo}'
        print(linha)
        return linha
    except Exception:
        return None


async def varrer(urls):
    resultados = []
    async with httpx.AsyncClient(verify=False, follow_redirects=True) as client:
        tarefas = [checar(client, u) for u in urls]
        for coro in asyncio.as_completed(tarefas):
            res = await coro
            if res:
                resultados.append(res)
    return resultados


@Save_info
def Hawkeye_cidr(cidr):
    urls = Get_urls(cidr)
    if not urls:
        print("Formato de CIDR incorreto, verifique! w(ﾟДﾟ)w")
        return []
    print(f'Iniciando detecção ~ tarefas carregadas: {len(urls)} itens')
    return asyncio.run(varrer(urls))


@Save_info
def Hawkeye_file(filename):
    try:
        with open(filename, 'r') as f:
            urls = [urlcheck(l.strip()) for l in f if l.strip()]
    except Exception:
        print('Forneça um arquivo! w(ﾟДﾟ)w')
        return []
    print(f'Iniciando detecção ~ tarefas carregadas: {len(urls)} itens')
    return asyncio.run(varrer(urls))


def run(*args):
    if len(args) == 1:
        if '/' in args[0]:
            Hawkeye_cidr(args[0])
        else:
            Hawkeye_file(args[0])


if __name__ == '__main__':
    Hawkeye_cidr('192.0.2.0/29')
