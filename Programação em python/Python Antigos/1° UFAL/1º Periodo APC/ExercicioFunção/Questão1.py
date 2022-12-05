# 1. Escreva um programa que possui uma função
# “maior”, que recebe uma lista e devolve o maior
# elemento na lista

def maior(conj):
    maior = conj[0]
    for valor in conj:
        if valor == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
    return maior


conj = []
for i in range(5):
    conj.append(int(input('Valores do conjunto: ')))

Maior = maior(conj)

print(f'O maior elemento informado foi: {Maior}.')
