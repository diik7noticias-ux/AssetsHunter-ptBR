#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
'''
 ____       _     _     _ _   __  __           _
|  _ \ __ _| |__ | |__ (_) |_|  \/  | __ _ ___| | __
| |_) / _` | '_ \| '_ \| | __| |\/| |/ _` / __| |/ /
|  _ < (_| | |_) | |_) | | |_| |  | | (_| \__ \   <
|_| \_\__,_|_.__/|_.__/|_|\__|_|  |_|\__,_|___/_|\_\
'''
# Função de resolução de registro A usando bibliotecas de terceiros
# Fornece uma interface externa que detecta automaticamente o tipo de entrada
# Reconhece automaticamente se é lista de domínios ou domínio único
# Também filtra 'http://', 'https://' e '/' para evitar erros de digitação

import dns.resolver
from Core.decorators import Print_info


def Domain_ip(domain):
    res=[]
    domain=domain.replace('https://','').replace('https//','').replace('/','')
    A = dns.resolver.query(domain, 'A')
    for i in A.response.answer:
        for j in i.items:
            if j.rdtype == 1:
                res.append(j.address)
    return res



def Domains_ip(domains):
    res=[]
    for domain in domains:
        domain = domain.replace('https://', '').replace('https//', '').replace('/', '')
        A = dns.resolver.query(domain, 'A')
        for i in A.response.answer:
            for j in i.items:
                if j.rdtype == 1:
                    res.append(j.address)
    return res

@Print_info
def run(domain):
    if isinstance(domain,str):
        return Domain_ip(domain)
    elif isinstance(domain,list):
        return Domains_ip(domain)
    else:
        pass

if __name__ == '__main__':
    # print(Domain_ip("www.taobao.com"))
    # print(Domains_ip(["www.taobao.com"]))
    print(run("taobao.com"))