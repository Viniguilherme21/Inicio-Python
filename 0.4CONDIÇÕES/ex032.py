'''
Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
'''

import datetime

ano = int(input('Digite o ano que você quer analisar ou Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = datetime.date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} NÃO é BISSEXTO'.format(ano))



