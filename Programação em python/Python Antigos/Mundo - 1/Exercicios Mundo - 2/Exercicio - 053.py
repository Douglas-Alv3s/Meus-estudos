'''Crie um programa que leia uma frase qualquer e diga se ela
é um Polindromo, desconsiderando os espaços.'''

frase = str(input('Digite uma frase: ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)

contrario = ''

for letra in range(len(junto) - 1, -1, -1):
    #print(junto[letra],end='')
    contrario += junto[letra]

if contrario == junto:
    print('É um Polindromo!!!')
else:
    print('Não é um Polindromo!!!') 