#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
'''
 ____       _     _     _ _   __  __           _
|  _ \ __ _| |__ | |__ (_) |_|  \/  | __ _ ___| | __
| |_) / _` | '_ \| '_ \| | __| |\/| |/ _` / __| |/ /
|  _ < (_| | |_) | |_) | | |_| |  | | (_| \__ \   <
|_| \_\__,_|_.__/|_.__/|_|\__|_|  |_|\__,_|___/_|\_\
'''
# Este é um exemplo, não integrado ao framework
# A coleta de informações sensíveis tende a ser personalizada por cenário
# Exemplo usado pelo autor, deixado como referência
# Os detalhes são úteis para tratar arquivos txt bagunçados

import re
import time


def Info_dig(filename):
    fr=open(filename,'r')
    # fr=open(filename,'r',encoding='UTF-8')
    data=fr.readlines()
    fr.close()

    data_str=''
    for i in data:
        data_str=data_str+i.replace('\n','')

    name = re.compile(r'(Nome:.*?)Conta').findall(data_str)
    job = re.compile(r'(Cargo/Posição:.*?)Departamento').findall(data_str)
    department =re.compile(r'(Departamento:.*?)Telefone central').findall(data_str)
    email=re.compile(r'(E-mail:.*?)Ramal').findall(data_str)
    phone=re.compile(r'(Celular:.*?)Fax').findall(data_str)

    timetoken = str(int(time.time()))
    filename = 'info_dig_result_{}.rabbit'.format(timetoken)

    for i in range(len(name)):
        fw=open(filename,'a')
        fw.write('No '+str(i+1)+'\n'+name[i]+'\n'+job[i]+'\n'+department[i]+'\n'+email[i]+'\n'+phone[i]+'\n\n\n')
        fw.close()
        print('Resultado salvo em: '+filename)


if __name__ == '__main__':
    Info_dig('demo.txt')