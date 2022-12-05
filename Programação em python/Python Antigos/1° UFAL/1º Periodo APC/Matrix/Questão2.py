#Segunda questão.

def verificação(matriz, valor):
  for L in range(len(matriz)):
    for C in range(len(matriz)):
      matriz[L][C] = int(input(f'Digite os valores da matriz: ({L}-{C}): '))
    print()
  for L in range(len(matriz)):
    for C in range(len(matriz)):
      matriz[L][C] *= valor
      print(f'[{matriz[L][C] :^5}]', end='')
    print()

valor = int(input('Quer multiplicar a matriz por qual valor: '))
matriz = [[0,0,0], [0,0,0], [0,0,0]]
verificação(matriz, valor)