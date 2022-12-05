#2. Faça um programa que conta o número de valores negativos em um conjunto#

conj = []
q = 0

for i in range(5):
    conj.append(int(input(f'Digite {i+1}º Numero do conjunto: ')))

for i in range(5):
    if conj[i] < 0:
        q = q + 1
print(f'A quantidade de valores negativos nesse conjunto é de: {q}')

