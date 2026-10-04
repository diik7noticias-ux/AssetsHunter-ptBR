#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Menu simples para o AssetsHunter-ptBR.
Basta rodar: python menu.py
"""

import os
import sys
import subprocess

PASTA = os.path.dirname(os.path.abspath(__file__))
SCRIPT = os.path.join(PASTA, 'AssetsHunter.py')


def limpar():
    os.system('clear' if os.name != 'nt' else 'cls')


def pausar():
    input('\nPressione ENTER para voltar ao menu...')


def rodar(args):
    print()
    print('=' * 55)
    print('  Executando:', 'AssetsHunter.py', ' '.join(args))
    print('=' * 55)
    print()
    try:
        subprocess.run(
            [sys.executable, SCRIPT] + args,
            cwd=PASTA,
            env={**os.environ, 'PYTHONWARNINGS': 'ignore'},
        )
    except Exception as e:
        print('Erro ao executar:', e)
    pausar()


def pedir_alvo(msg='Digite o domínio ou IP: '):
    return input(msg).strip()


def pedir_url(msg='Digite a URL (ex: https://exemplo.com): '):
    return input(msg).strip()


def pedir_arquivo(msg='Digite o caminho do arquivo: '):
    return input(msg).strip()


def mostrar_menu():
    limpar()
    print('=' * 55)
    print('   🐰 AssetsHunter-ptBR — Menu Simples')
    print('=' * 55)
    print()
    print('  CONSULTAS SEGURAS (qualquer domínio público)')
    print('  1.  Descobrir o IP de um domínio            (DNS)')
    print('  2.  Ver registro de um domínio              (Whois)')
    print('  3.  Ver informações de um IP                (IP Whois)')
    print('  4.  Descobrir subdomínios                   (CRT)')
    print()
    print('  FERRAMENTAS LOCAIS (não tocam em ninguém)')
    print('  5.  Converter CIDR em lista de IPs')
    print('  6.  Deduplicar um arquivo de texto')
    print('  7.  Minerar e-mails de um arquivo')
    print()
    print('  TESTES ATIVOS (só em alvos AUTORIZADOS!)')
    print('  8.  Identificar tecnologia de um site      (WhatCMS)')
    print('  9.  Buscar arquivos expostos                (InfoRisk)')
    print(' 10.  Detectar serviços numa faixa de IPs    (Hawkeye)')
    print()
    print('   0.  Sair')
    print()
    print('=' * 55)


def main():
    while True:
        mostrar_menu()
        opcao = input('Escolha uma opção [0-14]: ').strip()

        if opcao == '0':
            print('\nAté logo! 🐰')
            break

        elif opcao == '1':
            alvo = pedir_alvo('Domínio (ex: example.com): ')
            if alvo:
                rodar(['-dns', alvo])

        elif opcao == '2':
            alvo = pedir_alvo('Domínio (ex: example.com): ')
            if alvo:
                rodar(['-whois', alvo])

        elif opcao == '3':
            alvo = pedir_alvo('IP (ex: 8.8.8.8): ')
            if alvo:
                rodar(['-ipwhois', alvo])

        elif opcao == '4':
            alvo = pedir_alvo('Domínio (ex: example.com): ')
            if alvo:
                rodar(['-crt', alvo])

        elif opcao == '5':
            cidr = input('CIDR (ex: 192.168.1.0/24): ').strip()
            if cidr:
                rodar(['-cidr', cidr])

        elif opcao == '6':
            arq = pedir_arquivo('Arquivo com duplicatas: ')
            if arq:
                rodar(['-removal', arq])

        elif opcao == '7':
            arq = pedir_arquivo('Arquivo com e-mails: ')
            if arq:
                rodar(['-emaildig', arq])

        elif opcao == '8':
            print('\n⚠️  Use apenas em alvos AUTORIZADOS.')
            url = pedir_url()
            if url:
                rodar(['-whatcms', url])

        elif opcao == '9':
            print('\n⚠️  Use apenas em alvos AUTORIZADOS.')
            url = pedir_url()
            if url:
                rodar(['-inforisk', url])

        elif opcao == '10':
            print('\n⚠️  Use apenas em alvos AUTORIZADOS.')
            print('    Para testar, use 192.0.2.0/29 (documentação).')
            cidr = input('CIDR (ex: 192.0.2.0/29): ').strip()
            if cidr:
                rodar(['-hawkeye', cidr])

        elif opcao == '11':
            alvo = pedir_alvo('Domínio (ex: example.com): ')
            if alvo:
                rodar(['-subfinder', alvo])

        elif opcao == '12':
            alvo = pedir_alvo('Domínio (ex: example.com): ')
            if alvo:
                rodar(['-wayback', alvo])

        elif opcao == '13':
            alvo = pedir_alvo('Domínio (ex: example.com): ')
            if alvo:
                rodar(['-urlscan', alvo])

        elif opcao == '14':
            print('\n⚠️  Use apenas em alvos AUTORIZADOS.')
            print('    Aceita: URL única, lista separada por vírgula, ou arquivo.')
            alvo = input('Alvo: ').strip()
            if alvo:
                rodar(['-probe', alvo])

        else:
            print('\n❌ Opção inválida.')
            pausar()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\n\nInterrompido. Até logo! 🐰')
