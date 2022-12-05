# 9. Faça um programa que recebe um conjunto de
# inteiros e um valor n e indica qual o valor mais
# próximo de n no conjunto.

conjunto = []
n = int(input('Digite um valor: '))
difT = 0

for numero in range(0, 5):
    conjunto.append(int(input('Digite o conjunto: ')))

    diferença = conjunto[numero] - n
    diferença = diferença**2
    diferença = diferença**0.5

    if diferença == 0:

