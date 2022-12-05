# 2. Implemente uma função recursiva que, dados dois 
# números inteiros x e n, calcule o valor de x^n

def potencia (x, n):
    if n == 0:
        return 1
    else:
        return x * potencia(x, n-1)

R = potencia(5, 2)
print(R)