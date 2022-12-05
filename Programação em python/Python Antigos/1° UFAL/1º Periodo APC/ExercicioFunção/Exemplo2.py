#exemplo1 - tem entrada de dados, pega de para os dados e dentro trata


def somaMax (conj):
    max1 = 0

    for i in conj:
        if max1 == i:
            max1 = i
        elif max1 < i:
            max1 = i
    
    conj.remove(max1)

    max2 = 0

    for i in conj:
        if max2 == i:
            max2 = i
        elif max2 < i:
            max2 = i
    
    print(max1)
    print(max2)

    variante = max1 + max2
    return variante

conj =  []

for i in range (5):
    conj.append(int(input('Digite valores: ')))


SomaMaxima = somaMax(conj)

print(f'A soma dos maiores valores é: {SomaMaxima}')