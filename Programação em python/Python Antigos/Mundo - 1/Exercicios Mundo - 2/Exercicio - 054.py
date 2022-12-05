'''Crie um programa que leia o ano de nascimento de sete
pessoas. No, final mostre quantas pessoas ainda não atingiram 
a maioridade e quantas já são de maior.'''

maior = 0
menor = 0
ano_atual = 2022
idade = 0

for i in range(1,7+1):
    nascimento = int(input('Digite o ano de nascimento: '))
    idade = ano_atual - nascimento
    print(idade)
    if idade < 18:
        menor += 1
    else:
        maior += 1

print(f'numero de pessoas que ainda não atingiram a maioridade: [{menor}]')
print(f'Numero de pessoas que ja atingiram a maioridade: [{maior}]')

