#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
'''
 ____       _     _     _ _   __  __           _
|  _ \ __ _| |__ | |__ (_) |_|  \/  | __ _ ___| | __
| |_) / _` | '_ \| '_ \| | __| |\/| |/ _` / __| |/ /
|  _ < (_| | |_) | |_) | | |_| |  | | (_| \__ \   <
|_| \_\__,_|_.__/|_.__/|_|\__|_|  |_|\__,_|___/_|\_\
'''
# Olá~ hora do código! Este módulo oferece três métodos
# Censys_ip é usado pelo framework, consulta 1 página (100 itens) por padrão
# Censys_ip_all é um extra para uso manual
# Censys_demo é o exemplo bruto, para outros usos personalizados
# Uso seguro: exceções são tratadas para não desperdiçar chamadas de API
# Atualização do módulo: 24/04/2020 00h14  Status: validado

import json
from time import sleep
import requests
from Config.config_censys import API_ID, API_SECRET, API_URL
from Config.config_requests import headers
from Core.decorators import  Save_info


@Save_info
def Censys_ip(Domain,page):
    data = {
        "query": Domain,
        "page": page,
        "fields": ["ip"],
    }
    try:
        res = requests.post(API_URL,data=json.dumps(data), auth=(API_ID, API_SECRET),headers=headers)
        results=res.json()["results"]
        ips=[]
        for i in results:
            ips.append(i["ip"])
        return ips
    except:
        print("Falha de rede ao acessar o Censys...")


def Censys_ip_all(Domain):
    ips=[]
    i=1
    while 1:
        res=Censys_ip(Domain,i)
        if res:
            ips=ips+res
            if len(res)<100:
                break
            i=i+1
            sleep(1)
        else:
            print("Este resultado pode estar incompleto...")
            break
    return ips


def Censys_demo(Domain):
    data = {
        "query": Domain,
        "page": 1,
        "fields": [],
    }
    res = requests.post(API_URL,data=json.dumps(data), auth=(API_ID, API_SECRET),headers=headers)
    return res.json()

def run(Domain):
    return Censys_ip(Domain, 1)


if __name__ == '__main__':
    print(Censys_ip("taobao.com",1))
    # print(Censys_ip_all("taobao.com"))
