'''Faça um programa que leia o peso de cinco pessoas, mostre  
qual foi o maior peso e o menor peso lidos.'''

maior_peso = 0
menor_peso = 9999999999
lista = []

for i in range(1, 5+1):
    peso = float(input('Peso: '))
    
    if maior_peso < peso:
        maior_peso = peso

    if menor_peso > peso:
        menor_peso = peso

print(maior_peso)
print(menor_peso)