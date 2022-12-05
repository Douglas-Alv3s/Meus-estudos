'''3. Escreva uma função que recebe como parâmetro de entrada duas matrizes. A função deve comparar
elemento por elemento e criar uma nova matriz informando se estes são iguais ou não, como no exemplo
a seguir:
'''
def Nova_matriz(i, p):
    matriz = [0] * i
    for i in range(i):
        matriz[i] = [0] * p
    
    return matriz

def Comparação_Matriz(A, B):
    if len(A) == len(B):
        New_matriz = Nova_matriz(len(A), len(B))

        for i in range(len(A)):
            for p in range(len(B)):
                if A[i][p] == B[i][p]:
                    New_matriz[i][p] = 1
                else:
                    New_matriz[i][p] = 0
    else:
      print("Não dá para comparar essas matrizes :( ")
    return New_matriz

def CriarMatriz(n):

    lista = []
    matriz = []

    for i in range(0, n):
        for j in range(0, n):
             lista.append(int(input(f"Digite um valor para [{i},{j}] da matriz A: ")))     
        matriz.append(lista)   
        lista = []
    
    return matriz

num = int(input("Digite o número de linhas/colunas da matriz : "))
Matriz_A = CriarMatriz(num)

num_1 = int(input("Digite o número de linhas/colunas da matriz : "))
Matriz_B = CriarMatriz(num_1)

print(Comparação_Matriz(Matriz_A, Matriz_B))