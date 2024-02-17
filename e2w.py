#!/bin/python
from os import stat,system
import getpass, sys
import pyAesCrypt
import io

banner = '''
███████╗██████╗ ██╗    ██╗    ██╗    ██╗ █████╗ ██╗     ██╗     ███████╗████████╗
██╔════╝╚════██╗██║    ██║    ██║    ██║██╔══██╗██║     ██║     ██╔════╝╚══██╔══╝
█████╗   █████╔╝██║ █╗ ██║    ██║ █╗ ██║███████║██║     ██║     █████╗     ██║   
██╔══╝  ██╔═══╝ ██║███╗██║    ██║███╗██║██╔══██║██║     ██║     ██╔══╝     ██║   
███████╗███████╗╚███╔███╔╝    ╚███╔███╔╝██║  ██║███████╗███████╗███████╗   ██║   
╚══════╝╚══════╝ ╚══╝╚══╝      ╚══╝╚══╝ ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝   ╚═╝   
                                                                                 
Author: r4msolo                                                    [coldwallet] 
'''
bufferSize = 64 * 1024
choice = input(banner + '\n1 - Criptografar Seed\t\t0 - Sair\n2 - Ler Seed Criptografada\n\n[E2W] : ')

if choice == '1':
    phrase = str(input('Frase de backup (seed): '))
    phrase = io.BytesIO(phrase.encode())
    password = getpass.getpass('\nCrie uma Senha:')
    arq = str(input('Nome para arquivo com chaves: '))
    narq = '.keys/'+arq+'.aes'
    with open(narq, "wb") as fOut:
        pyAesCrypt.encryptStream(phrase, fOut, password, bufferSize)
        print("\n[+] Arquivo '{}' criado! Use sua senha para ler o conteúdo dele.\n".format(arq))
    quit()

if choice == '2':
    print(system('ls -la .keys/'))
    arq = str(input('[!] Nome do arquivo: '))
    narq = '.keys/'+arq+'.aes'
    encFileSize = stat(narq).st_size
    password = getpass.getpass('\nDigite a Senha:')
    with open(narq, "rb") as fIn:
        try:
            fOut = io.BytesIO()
            pyAesCrypt.decryptStream(fIn, fOut, password, bufferSize, encFileSize)
            print('\n=> '+fOut.getvalue().decode('utf-8'))

        except ValueError:
            print('[!] Senha incorreta')
            quit()
if choice  == '0':
    quit()
else:
    print ('\n\n[!] Opção inválida!\n')
    quit()
