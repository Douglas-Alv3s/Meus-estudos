# Criar uma lista com numero indeterminado e partindo dessa lista crie uma
# de numeros pares e impares.

lista = []
lista_Par = []
lista_Impar = []

while True:

    num = int(input('Digite um valor: '))
    lista.append(num)

    resultado = num % 2
    if resultado == 0:
        lista_Par.append(num)
    else:
        lista_Impar.append(num)

    resposta = str(input('Quer continuar? [S/N] ')).strip().upper()
    if resposta == 'N' or resposta == 'S':
        if resposta == 'N':
            break
    else:
        resposta = str(input('Caractere invalido! Quer continuar? [S/N]  ')).strip().upper()   

print('-='*20)
print('...Resultado...')
print('--'*20)
print(f'Lista Completa: {lista}')
print(f'Lista de Pares {lista_Par}')
print(f'Lista de Imparares {lista_Impar}')
print('--'*20)
print('...Programa Encerrado...')
print('-='*20)