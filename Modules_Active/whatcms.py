#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
# Identificação de fingerprint com validação ULTRA-rígida.
# Só reporta quando o padrão é inequívoco (evita falsos positivos).

import hashlib
import json
import os
import re
from concurrent.futures import ThreadPoolExecutor, as_completed

import requests
from Config.config_requests import headers

requests.packages.urllib3.disable_warnings()

PASTA = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DICT = os.path.join(PASTA, 'Dictionaries', 'TideFinger.json')

# Só aceita keyword se for um "identificador" forte:
# - 12+ caracteres
# - contém . / _ - : ou < > (indica URL, path, HTML tag, CSS/JS)
# - não é uma palavra comum
PALAVRAS_GENERICAS = re.compile(
    r'^(powered|by|copyright|version|home|index|login|admin|'
    r'帝国|织梦|phpcms|dedecms|empirecms|southidc|discuz)',
    re.IGNORECASE
)


def getmd5(data):
    md5 = hashlib.md5()
    md5.update(data)
    return md5.hexdigest()


def _pattern_forte(pattern):
    """Verifica se o padrão é específico o suficiente."""
    if not pattern or not isinstance(pattern, str):
        return False
    pattern = pattern.strip()
    if len(pattern) < 12:
        return False
    if PALAVRAS_GENERICAS.match(pattern):
        return False
    # Precisa ter estrutura (URL, path, tag HTML, seletor CSS)
    tem_estrutura = any(c in pattern for c in './:_-<>[]()')
    return tem_estrutura


def testar_fingerprint(item, url):
    try:
        pattern = item.get('match_pattern', '')
        if not _pattern_forte(pattern):
            return None

        r = requests.get(url + item['path'], headers=headers,
                         timeout=5, verify=False)

        if item['options'] == 'md5':
            if pattern == getmd5(r.content):
                return item['cms_name']
        elif item['options'] == 'keyword':
            if pattern in r.text:
                return item['cms_name']
    except Exception:
        pass
    return None


def Whatcms(url):
    if not os.path.exists(DICT):
        print(f"Dicionário não encontrado: {DICT}")
        return

    with open(DICT, 'r', encoding='utf-8') as fr:
        data = json.load(fr)

    print(f"Fingerprints carregados: {len(data)} itens")
    print("Power By Tidefinger: http://finger.tidesec.com")

    encontrados = set()
    with ThreadPoolExecutor(max_workers=20) as ex:
        futuros = [ex.submit(testar_fingerprint, item, url) for item in data]
        for fut in as_completed(futuros):
            res = fut.result()
            if res:
                encontrados.add(res)

    if encontrados:
        for r in sorted(encontrados):
            print(f"Fingerprint do alvo: {r}")
    else:
        print("Nenhum fingerprint identificado.")


def run(url):
    Whatcms(url)


if __name__ == '__main__':
    run('https://wordpress.org')
