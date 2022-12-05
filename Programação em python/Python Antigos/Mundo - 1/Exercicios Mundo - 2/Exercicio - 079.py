'''Crie um programa onde o usuario possa digitar varios valores numericos e 
cadastre-os em uma lista. Caso o número já exista lá dentro, ele não sera
adicionado. No final, serão exibidos todos os valores unicos digitados, em
ordem crescente'''

def linha ():
    print('--'*30)


lista_numerica =[]

continuar = 'S'

while continuar == 'S' and continuar != 'N':
    num = (int(input('Digite um Valor: ')))
    if num not in lista_numerica:
        lista_numerica.append(num)
        print('O valor foi adicionado...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Informação invalida. Digite [S/N] ')).strip().upper()


lista_numerica.sort()

linha()
linha()
print(f'Você digitou os valores {lista_numerica}')
linha()
print('Programa encerrado!')
linha()