'''Faça um programa que leia um número qualquer e mostre o seu fatorial.

Ex:
5! = 5x4x3x2x1 = 120'''

num = int(input('Digite um número: '))
fatorial = 1

while 0 < num:
    fatorial = fatorial * num
    num -= 1
    
print(fatorial)