#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
'''
 ____       _     _     _ _   __  __           _
|  _ \ __ _| |__ | |__ (_) |_|  \/  | __ _ ___| | __
| |_) / _` | '_ \| '_ \| | __| |\/| |/ _` / __| |/ /
|  _ < (_| | |_) | |_) | | |_| |  | | (_| \__ \   <
|_| \_\__,_|_.__/|_.__/|_|\__|_|  |_|\__,_|___/_|\_\
'''
import time

# Decorador de impressão de lista
def Print_info(fun):
    def work(*args,**kwargs):
        res=fun(*args, **kwargs)
        if res:
            if isinstance(res, str):
                print(res)
            elif isinstance(res, list):
                for i in res:
                    print(i.replace('\n',''))
            else:
                pass
        return fun(*args, **kwargs)
    return work

# Decorador de exportação de resultados
# Salva arquivo com extensão .rabbit, para evitar abertura descuidada no Bloco de Notas,
# pois pode ficar bagunçado. Recomendado: Notepad++, SublimeText, VSCode, etc.

def Save_info(fun):
    def work(*args,**kwargs):
        result=(fun(*args, **kwargs))
        if result:
            timetoken = str(int(time.time()))
            filename='Output/{}_result_{}.rabbit'.format(fun.__name__,timetoken)
            for i in result:
                try:
                    fw = open(filename, 'a')
                    fw.write(i.replace('\n','') + '\n')
                    fw.close()
                except:
                    pass
            print('Resultado salvo em: '+filename)
        # return fun(*args, **kwargs)
    return work
