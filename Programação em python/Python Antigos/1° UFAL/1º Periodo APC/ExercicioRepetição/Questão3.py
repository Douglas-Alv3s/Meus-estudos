# 3. Faça um programa que recebe um conjunto de inteiros e imprime os valores que estão abaixo da
# média do conjunto#

lista = []

v = 0

for i in range(5):
    lista.append(int(input(f'Digite {i+1}º Numero do conjunto: ')))

    v = v + lista[i]
    m = v/5


for i in range(5):
    if lista[i] < m:
        print(
            f'A média do conjunto é {m} e os numeros a baixo dela é: {lista[i]}')
