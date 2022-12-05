# 2. Escreva um programa que possui uma função
# que recebe uma lista e um valor e verifica se
# existe o valor na lista
def lin ():
    print('=-'*30)


def verifica():
    
    conj = []
    n = int(input('Digite o valor para verificar: '))
    lin()
    
    for i in range(5):
        conj.append(int(input('Digite a lista de numeros: ')))
    lin()

    var1 = 0
    for i in conj:
        if i == n:
            lin()
            print(f'O valor {n} existe na lista!!!')
            var1 += 1
            var1 = 1
            lin()
            break
    if var1 == 0:
        print(f'O valor {n} não existe na lista!!!')
        lin()



lin()
verifica()
