# 4. Faça um programa programa que recebe um conjunto de inteiros e conta quantos elementos
# maiores que n existem no conjunto


conj = []
n = int(input('Digite o valor N: '))
q = 0

for i in range(5):
    conj.append(int(input(f'Digite {i+1}º Numero do conjunto: ')))

for i in range(5):
    if conj[i] > n:
        q = q + 1

print(f'A quantia de elementos maiore que N é: {q}')
