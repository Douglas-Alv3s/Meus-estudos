'''Refaça o desafio 009, mostrando a tabuada de um numero
que o usuario escolher, só que agora ultilizando o laço for.'''

n= int(input('Digite um valor: '))

for i in range(0,11):
    print('{} x {} = {}'.format(n, i, n*i))