#14. Algoritmo que recebe um conjunto de inteiros e calcula 
#a amplitude do conjunto. A amplitude é dada por:

conj = []


for i in range(5):
    conj.append(int(input(f'Digite {i+1}º Numero do conjunto: ')))

    A = max(conj)
    B = min(conj)

    amplitude = A - B

print(f'A amplitude desse conjunto é de: {amplitude}')
