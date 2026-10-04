#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
'''
 ____       _     _     _ _   __  __           _
|  _ \ __ _| |__ | |__ (_) |_|  \/  | __ _ ___| | __
| |_) / _` | '_ \| '_ \| | __| |\/| |/ _` / __| |/ /
|  _ < (_| | |_) | |_) | | |_| |  | | (_| \__ \   <
|_| \_\__,_|_.__/|_.__/|_|\__|_|  |_|\__,_|___/_|\_\
'''
# Infelizmente não foi possível obter todos os CIDRs do servidor
# Se houver uma técnica melhor, evitamos usar APIs

import requests
from Config.config_requests import headers
from Core.decorators import Print_info

def Asn_cidr(asn):
    try:
        r=requests.get("https://api.hackertarget.com/aslookup/?q="+str(asn),headers=headers)
        res = r.text.split('\n')[1:]
        return res
    except:
        return ("Desculpe, falha de rede ou consultas excessivas...")

@Print_info
def run(asn):
    return Asn_cidr(asn)

if __name__ == '__main__':
    run("AS0000")
