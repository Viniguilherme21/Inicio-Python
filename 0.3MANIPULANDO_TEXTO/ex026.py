'''
Faça um programa que leia uma frase pelo teclado e mostre:
Quantos vezes aparece a letra “A”
Em que posição ela aparece a primeira vez
Em que posição ela aparece a última vez.
'''

frase = input('Digite uma frase: ').strip().upper()

print('A letra "A aparece {} na frase'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
print('A última letra A aparece na posição {}'.format(frase.rfind('A')+1)) # "R" eu utilizo para procurar da direita para esquerda

