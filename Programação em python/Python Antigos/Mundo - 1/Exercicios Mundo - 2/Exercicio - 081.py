lista = []
cont = 0
verificar_numero = 5

while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    
    cont += 1
    
    resposta = str(input('Quer continuar? [S/N]: ')).strip().upper()
    if resposta == 'S' or resposta == 'N':
        if resposta == 'N':
            break
    else:
        resposta = str(input('Caractere Invalido! Quer continuar? [S/N]: ')).strip().upper()       


print('-='*30)
lista.sort(reverse= True)
print(f'Você digitou {cont} elementos!')
print(f'Os valores em ordem decrescente são: {lista}')
if verificar_numero in lista:
    print(f'O elemento {verificar_numero} está na lista.')
else:
    print(f'O elemento {verificar_numero} não está na lista.')