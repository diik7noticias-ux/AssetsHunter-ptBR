#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
'''
 ____       _     _     _ _   __  __           _
|  _ \ __ _| |__ | |__ (_) |_|  \/  | __ _ ___| | __
| |_) / _` | '_ \| '_ \| | __| |\/| |/ _` / __| |/ /
|  _ < (_| | |_) | |_) | | |_| |  | | (_| \__ \   <
|_| \_\__,_|_.__/|_.__/|_|\__|_|  |_|\__,_|___/_|\_\
'''
import argparse
from Modules_Active import hawkeye, inforisk, whatcms
from Modules_Passive import domain_ip, crt_domain, asn_cidr, censys_ip, ip_whois, domain_whois
from Tools import cidr_ip, kill_repeat, email_dig


def Console():
    parser = argparse.ArgumentParser()
    ahf_modules_passive = parser.add_argument_group('AHF Modules_Passive')
    ahf_modules_active = parser.add_argument_group('AHF Modules_Active')
    ahf_tools = parser.add_argument_group('AHF Tools')


########################################################################################################################

    #Módulos de varredura ativa
    ahf_modules_active.add_argument("-hawkeye", dest='hawkeye',help="Detecção WEB (CIDR/arquivo)")
    ahf_modules_active.add_argument("-inforisk", dest='inforisk', help="Detecção de vazamento de informações")
    ahf_modules_active.add_argument("-whatcms", dest='whatcms', help="Identificação de fingerprint (TideFinger)")

    #Módulos de varredura passiva
    ahf_modules_passive.add_argument("-asn", dest='asn',help="Consulta ASN ICDR")
    ahf_modules_passive.add_argument("-censys", dest='censys',help="Consulta à API CENSYS")
    ahf_modules_passive.add_argument("-crt", dest='crt',help="Consulta de domínio via Certificate Transparency")
    ahf_modules_passive.add_argument("-dns", dest='dns',help="Resolução de registro DNS A")
    ahf_modules_passive.add_argument("-ipwhois", dest='ipwhois',help="Consulta IP Whois")
    ahf_modules_passive.add_argument("-whois", dest='whois',help="Consulta Whois de domínio")


    #Módulos de coleta de ativos
    ahf_tools.add_argument("-cidr", dest='cidr',help="Converte CIDR em intervalo de IP")
    ahf_tools.add_argument("-emaildig", dest='emaildig',help="Ferramenta de mineração de e-mail (entrada: arquivo)")
    ahf_tools.add_argument("-removal", dest='removal',help="Ferramenta de deduplicação de dados (entrada: arquivo)")

    args = parser.parse_args()


########################################################################################################################


    #Módulos de varredura ativa
    if args.hawkeye:
        hawkeye.run(args.hawkeye)
    elif args.inforisk:
        inforisk.run(args.inforisk)
    elif args.whatcms:
        whatcms.run(args.whatcms)

    #Módulos de varredura passiva
    elif args.asn:
        asn_cidr.run(args.asn)
    elif args.crt:
        crt_domain.run(args.crt)
    elif args.censys:
        censys_ip.run(args.censys)
    elif args.dns:
        domain_ip.run(args.dns)
    elif args.ipwhois:
        ip_whois.run(args.ipwhois)
    elif args.whois:
        domain_whois.run(args.whois)

    #Módulos de coleta de ativos
    elif args.cidr:
        cidr_ip.run(args.cidr)
    elif args.emaildig:
        email_dig.run(args.emaildig)
    elif args.removal:
        kill_repeat.run(args.removal)


########################################################################################################################
