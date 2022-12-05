
'''Desenvolva um programa que leia seis numeros inteiros e 
mostre a soma apenas daqueles que forem PARES. Se o valor 
digitado for Impar, desconside-0'''


cont = 0
soma = 0
00
for i in range(0,6):
    n = int(input('Digite um Valor: '))
    if n % 2 == 0:
        cont = cont + 1
        soma = soma + n
print('A quantidade de numeros pares é {} e a soma entre eles é {}!'.format(cont, soma))

    
