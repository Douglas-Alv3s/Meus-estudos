# 1. Escreva um programa que recebe vários números do usuário e armazena em uma lista até que o
# usuário digite um valor menor do que zero. O número menor que 0 não deve ser armazenado na lista.
# Em seguida o programa pede ao usuário que informe um número x e escreve uma mensagem informando
# se esse número x pertence ou não a lista informada.

conj = []
var = True


while var:
    num = int(input('Digite os valores do conjunto[Digite numero menor que 0 para parar]: '))
    if num < 0:
        var = False
    else:
        conj.append(num)
        

print(conj)   

x = int(input('Digite o valor x: '))   
var1 = 0

for i in conj:
    if x == i:
        print('O Valor informado pertece ao conjunto!!!')
        var1 += 1
        var1 = 1
        break
if var1 == 0:
    print('Não pertence!!!')

    
