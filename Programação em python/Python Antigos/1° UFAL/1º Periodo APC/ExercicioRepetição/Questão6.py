# 6. Faça um algoritmo que recebe dois conjuntos de inteiros A
# e B e calcula a distância euclidiana entre estes dois conjuntos.

A = []
B = []

for i in range(2):
    A.append(int(input(f'Digite {i+1}º Numero do conjunto A: ')))

print('')

for i in range(2):
    B.append(int(input(f'Digite {i+1}º Numero do conjunto B: ')))

a = (A[0] - B[0])**2
b = (A[1] - B[1])**2
c = a + b

Dist_euc = (c)**0.5
print('')
print('A distância euclidiana entre os conjuntos A e B é: {:.2F}'.format(Dist_euc))