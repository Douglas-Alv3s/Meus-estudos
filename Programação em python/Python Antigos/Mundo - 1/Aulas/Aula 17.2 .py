Valores = []

Valores.append(4)
Valores.append(2)
Valores.append(7)
Valores.append(5)

Valores.sort()

print(Valores)
for c, v in enumerate(Valores):
    print(f'Encontrei na posição {c}º o valor {v}!')


Lista_A = [2,4,6]
Lista_B = [1,3,5]

Lista_A[len(Lista_A):] = Lista_B

Lista_A.sort()
print(Lista_A)