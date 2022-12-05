#Terceira questão: 

def vefificação(matriz, num):
  contador = 0
  
  for i in range(len(matriz)):
    for p in range(len(matriz)):
      matriz[i][p] = int(input(f'Digite os valores da matriz: ({i}--{p}): '))
    print()
  
  for i in range(len(matriz)):
    for p in range(len(matriz)):
      print(f'[{matriz[i][p] :^4}]', end='')
      if matriz[i][p] == num:
        contador += 1
      else:
        contador += 0
    print()
  if contador > 0:
    return 'Esse número existe na matriz!'
  else:
    return 'Esse número não existe na matriz!' 


matriz = [[0,0,0], [0,0,0], [0,0,0]]
num = int(input('Digite o número para verificação: '))

vefificação(matriz, num)
