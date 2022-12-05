'''Crie um programa onde o usuario possa digitar varios valores numericos e 
cadastre-os em uma lista. Caso o número já exista lá dentro, ele não sera
adicionado. No final, serão exibidos todos os valores unicos digitados, em
ordem crescente'''


def Criar_lista (Escolha):
    lista_numerica =[]

    continuar = Escolha

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
    print('-='*20)
    print(f'Você digitou os valores {lista_numerica}')

    print('Programa encerrado!')
    print('-='*20)

Iniciar = str(input('Iniciar programa digite [S]: ')).strip().upper()
if Iniciar != 'S':
    print('O programa não foi iniciado!')
else:
    print('...Iniciando Programa...')
    print('='*30)
    Criar_lista(Iniciar)