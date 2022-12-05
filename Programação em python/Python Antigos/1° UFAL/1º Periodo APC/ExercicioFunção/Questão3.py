#3. Escreva um programa que possui uma função 
#que recebe uma lista e diz qual a soma máxima 
#entre dois elementos da lista

def somaMax (conj):
    conj = []
    for i in range (4):
        conj.append(int(input('Valores da lista: ')))


    max1 = 0

    for i in conj:
        if i == max1:
            max1 = i
        elif i > max1:
            max1 = i
    conj.remove(max1)

    max2 = 0

    for i in conj:
        if i == max2:
            max2 = i
        if i > max2 :
            max2 = i

    print(max1)
    print(max2)
    variavel = max1 + max2
    return variavel


conjunto = list()

SomaMaxima = somaMax(conjunto)

print(f'A soma dos dois maiores elementos da lista é: {SomaMaxima}')