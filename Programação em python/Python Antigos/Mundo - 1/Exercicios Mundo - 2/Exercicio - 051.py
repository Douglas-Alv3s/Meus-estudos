'''Desenvolva um programa que leia o primeiro termo e a razão
de uma PA. No final, mostre os 10 primeiros termos dessa progressão.'''

Primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
decimo = Primeiro_termo + (10 - 1) * razao

for i in range(Primeiro_termo, decimo + razao, razao):
    print('{}'.format(i), end=' -> ')
print('Fim')

