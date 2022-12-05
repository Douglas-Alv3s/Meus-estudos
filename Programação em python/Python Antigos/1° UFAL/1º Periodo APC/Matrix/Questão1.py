'''1. Implemente uma função que recebe uma matriz 
e verifica se ela é simétrica.'''

def verificação(matriz):
    verifica = 'V'
    for i in range(4):
        for p in range(4):
            matriz[i][p] = int(input(f'Digites os valores [{i}-{p}]: '))
            print('=-'*20)

    for i in range(4):
        for p in range(4):
            print(f'[{matriz[i][p] :^5}]', end=' ')
            if matriz[i][p] != matriz[p][i]:
                verifica = 'F'
        print('=-'*20)

    if verifica == 'V':
        return 'É uma matriz simétrica!'
    else:
        return 'Não é uma matriz simétrica'


matriz = [[0,0,0], [0,0,0], [0,0,0]]
print(verificação(matriz))