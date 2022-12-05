# 1. Implemente uma função recursiva que, dados dois
# números inteiros x e n, calcule o valor de x.n


def multiplicar(x, n):
    if n == 0 or x == 0:
        return 0
    elif n == 1:
        return x
    else:
        return x + (multiplicar(x, n-1))


R = multiplicar(10, 5)
print(f'{R}')
