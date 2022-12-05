#exemplo1 - não tem entrada de dados, solicita os dados dentro da própria função


def somamax ():
    conj = []
    
    
    for i in range (4):
        conj.append(int(input('Digite: ')))

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
    variavel = max1 + max2
    return variavel


SomaMax = somamax()
print(f'A soma maxima é: {SomaMax}')