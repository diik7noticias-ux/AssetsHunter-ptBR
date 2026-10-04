#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
'''
 ____       _     _     _ _   __  __           _
|  _ \ __ _| |__ | |__ (_) |_|  \/  | __ _ ___| | __
| |_) / _` | '_ \| '_ \| | __| |\/| |/ _` / __| |/ /
|  _ < (_| | |_) | |_) | | |_| |  | | (_| \__ \   <
|_| \_\__,_|_.__/|_.__/|_|\__|_|  |_|\__,_|___/_|\_\
'''
import re
import requests

from Config.config_requests import headers

requests.packages.urllib3.disable_warnings()

def svn_check(url):
    try:
        req = requests.get(url+'/.svn/entries', headers=headers, timeout=3, verify=False)
        contents = str(req.text).split('\x0c')
        pattern = re.compile(r'has-props|file|dir')
        for content in contents:
            match = len(pattern.search(content).group(0))
            if req.status_code == 200 and match > 0:
                print ("[+] Vulnerabilidade de vazamento de código-fonte SVN...\tpayload: "+url+'/.svn/entries')
    except:
        pass

def robots_check(url):
    try:
        req = requests.get(url+'/robots.txt', headers=headers, timeout=3, verify=False)
        if "Disallow" in req.text:
            print ("[+] Arquivo robots.txt encontrado...\tpayload: " + url+'/robots.txt')
    except:
        pass

def options_check(url):
    try:
        req = requests.options(url, headers=headers, timeout=3, verify=False)
        if r"OPTIONS" in req.headers['Allow']:
            print ("[+] Método OPTIONS habilitado...\tpayload: " + url + "\tAllow:" + req.headers['Allow'])
    except:
        pass

def jsp_conf_check(url):
    try:
        req = requests.get(url+'/WEB-INF/web.xml', headers=headers, timeout=3, verify=False)
        if req.headers["Content-Type"] == "application/xml":
            print("[+] Arquivo de configuração web.xml encontrado...\tpayload: " + url + '/WEB-INF/web.xml')
    except:
        pass

def git_check(url):
    try:
        req = requests.get(url+'/.git/config', headers=headers, timeout=3, verify=False)
        if r"repositoryformatversion" in req.text and req.status_code == 200:
            print("[+] Vulnerabilidade de vazamento de código-fonte Git...\tpayload: " + url + '/.git/config')
    except:
        pass

def jet_ide_check(url):
    try:
        req = requests.get(url+'/.idea/workspace.xml', headers=headers, timeout=3, verify=False)
        if r"<?xml version=" in req.text and r"project version" in req.text and req.status_code==200:
            print("[+] Vazamento do arquivo workspace.xml do JetBrains IDE...\tpayload: " + url + '/.idea/workspace.xml')
    except:
        pass

def crossdomain_check(url):
    try:
        req = requests.get(url+'/crossdomain.xml', headers=headers, timeout=3, verify=False)
        if r"<cross-domain-policy>" in req.text and r"allow-access-from" in req.text:
            print("[+] Arquivo crossdomain.xml encontrado...\tpayload: " + url + '/crossdomain.xml')
    except:
        pass

def apache_check(url):
    try:
        req = requests.get(url+'/server-status', headers=headers, timeout=3, verify=False)
        if r"Server uptime" in req.text and r"Server Status" in req.text and req.status_code == 200:
            print("[+] Vazamento do arquivo de status do Apache...\tpayload: " + url + '/server-status')
    except:
        pass

def Inforisk(url):
    svn_check(url)
    robots_check(url)
    options_check(url)
    jsp_conf_check(url)
    git_check(url)
    jet_ide_check(url)
    crossdomain_check(url)
    apache_check(url)

def run(url):
    Inforisk(url)

if __name__ == '__main__':
    run('http://127.0.0.1')