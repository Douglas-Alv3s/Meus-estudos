# Faça um programa que leia nome e peso de várias pessoas,
# guardando tudo em uma lista. No final, mostre:

# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

Pessoas = []
dados = ['', '']
Pesadas = []
leves = []
maior_peso = menor_peso = 0
i = 0

while True:
    print('--'*30)
    dados[0] = str(input('Nome: '))
    dados[1] = float(input('Peso: '))
    Pessoas.append(dados[:])
    print('--'*30)
    if (Pessoas[i][1]) > maior_peso:
        maior_peso = (Pessoas[i][1])
        menor_peso = maior_peso
    if (Pessoas[i][1]) < menor_peso:
        menor_peso = (Pessoas[i][1])

    i += 1

    R = str(input('Quer continuar? [S/N] ')).strip().upper()
    if R == 'S' or R == 'N':
        if 'N' == R:
            break
    else:
        print('--'*30)
        R = str(input('Caractere Invalido.\nDigite um caractere valido [S/N] ')).strip().upper()

i = 0
while i < len(Pessoas) :
    if (Pessoas[i][1]) == maior_peso:
       Pesadas.append(Pessoas[i][0])
    if (Pessoas[i][1]) == menor_peso:
        leves.append(Pessoas[i][0])
    i += 1
print('--'*30)
print('--'*30)
print(f'Ao todo, foram cadastradas {len(Pessoas)} pessoas.')
print(f'O Maior peso foi {maior_peso}Kg. Peso de {Pesadas}')
print(f'O menor peso foi {menor_peso}Kg. Peso de {leves}')
print('--'*30)
print('--'*30)