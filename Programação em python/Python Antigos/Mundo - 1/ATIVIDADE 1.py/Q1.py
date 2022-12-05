# 1. Contar o número de elementos negativos em um conjunto

def ContNEGATIVOS (CONJUNTO):
    cont = 0 
    for i in CONJUNTO:
        if i < 0:
            cont += 1

    print('--'*25)
    print(f'Teve {cont} numeros negativos no conjunto.')
    print('--'*25)

conjunto = [4, 2, -1, 5, -9, -2, 0, 20]
ContNEGATIVOS(conjunto)

#A função desse algoritmo é: f(n): n