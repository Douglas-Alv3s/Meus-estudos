'''Faça um programa que leia um numero inteiro e diga se ele
é ou não um numero primo.'''

num = int(input('Digite um número: '))
cont = 0

print('')

for i in range(1, num+1):
    if num % i == 0: 
        cont += 1    

print(f'O numero {num} foi dividido {cont}.')

if cont == 2:
    print('logo é Primo')
else: 
    print('Logo não é Primo')

