# AssetsHunter — Caçador de Ativos (pt-BR)

Framework de caça a ativos para reconhecimento em segurança ofensiva.
A coleta de informações é uma arte. 🐰

> Tradução para português do projeto original
> [rabbitmask/AssetsHunter](https://github.com/rabbitmask/AssetsHunter),
> de autoria de **Tide_RabbitMask**. Todos os créditos ao autor original.

---

## 📖 Sobre

O **AssetsHunter** é um framework de **coleta de informações (OSINT)** e
**reconhecimento** para profissionais de segurança ofensiva. Reúne módulos
passivos, ativos e ferramentas auxiliares em uma única interface de linha
de comando.

---

## ⚠️ Aviso legal

Esta ferramenta deve ser usada **apenas** em:

- Alvos próprios (seus domínios, seus servidores, seu laboratório)
- Alvos para os quais você tem **autorização por escrito**
- Programas de bug bounty dentro do escopo permitido

O uso contra terceiros sem autorização é **crime** no Brasil
(Lei 12.737/2012) e em diversas outras jurisdições.

---

## 🚀 Instalação

### Linux / macOS

    git clone https://github.com/diik7noticias-ux/AssetsHunter-ptBR.git
    cd AssetsHunter-ptBR
    pip install -r requirements.txt
    pip install netaddr ipwhois python-whois lxml dnspython pymysql beautifulsoup4 censys requests

### Termux (Android)

    pkg update && pkg upgrade -y
    pkg install -y python python-pip git clang make libcrypt libxml2 libxslt openssl libffi
    git clone https://github.com/diik7noticias-ux/AssetsHunter-ptBR.git
    cd AssetsHunter-ptBR
    pip install -r requirements.txt
    pip install netaddr ipwhois python-whois lxml dnspython pymysql beautifulsoup4 censys requests

---

## 🎯 Uso

Ver o menu de ajuda:

    python AssetsHunter.py -h

### Módulos passivos (OSINT)

    python AssetsHunter.py -asn AS12345
    python AssetsHunter.py -censys 8.8.8.8
    python AssetsHunter.py -crt exemplo.com
    python AssetsHunter.py -dns exemplo.com
    python AssetsHunter.py -ipwhois 8.8.8.8
    python AssetsHunter.py -whois exemplo.com

### Módulos ativos (só em alvos autorizados)

    python AssetsHunter.py -hawkeye 192.168.1.0/24
    python AssetsHunter.py -inforisk https://exemplo.com
    python AssetsHunter.py -whatcms https://exemplo.com

### Ferramentas

    python AssetsHunter.py -cidr 192.168.1.0/24
    python AssetsHunter.py -emaildig arquivo.txt
    python AssetsHunter.py -removal arquivo.txt

---

## 📋 Parâmetros

| Parâmetro | Descrição |
|---|---|
| `-asn` | Consulta ASN ICDR |
| `-censys` | Consulta à API CENSYS |
| `-crt` | Consulta de domínio via Certificate Transparency |
| `-dns` | Resolução de registro DNS A |
| `-ipwhois` | Consulta IP Whois |
| `-whois` | Consulta Whois de domínio |
| `-hawkeye` | Detecção WEB (CIDR/arquivo) |
| `-inforisk` | Detecção de vazamento de informações |
| `-whatcms` | Identificação de fingerprint (TideFinger) |
| `-cidr` | Converte CIDR em intervalo de IP |
| `-emaildig` | Ferramenta de mineração de e-mail |
| `-removal` | Ferramenta de deduplicação de dados |

---

## 🙏 Créditos

- **Autor original:** Tide_RabbitMask
- **Repositório original:** https://github.com/rabbitmask/AssetsHunter
- **Tradução pt-BR:** diik7noticias-ux

---

## 📄 Licença

Este projeto segue a licença do repositório original. Consulte o arquivo
`LICENSE` para mais detalhes.
