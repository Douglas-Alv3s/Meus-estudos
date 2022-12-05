x = 1
lista = []
while x > 0:
    valor =  int(input())
    if valor < 0:
        x = -1
    
    if valor >= 0:
        lista.append(valor)

n = int(input())

aux = 0
for i in lista:
    if n == i:
        print("O valor digitado pertence a lista ", n)
        aux = 1
        break

if aux == 0:
    print("Não pertence a lista ", n)

print(lista)