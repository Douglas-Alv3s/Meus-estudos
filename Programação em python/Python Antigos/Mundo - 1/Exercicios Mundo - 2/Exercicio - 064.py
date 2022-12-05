'''Crie um programa que leia varios numeros inteiros
pelo teclado. O programa só vai parar quando o usuário 
digitar o valor 999, que é a condição de parada. No 
final mostre quantos números foram digitas e qual foi
a soma entre eles.'''

num = 0
contador = 0
soma = 0

while num != 999:
    num = int(input('Digite os valores e para parar digite [999]: '))
    contador += 1
    if num != 999:
        soma = soma + num

print('-='*30)
print('-='*30)

print(f'A quantidade de numeros digitados: {contador}')
print('-'*40)
print(f'A soma dos numeros digitados foi de {soma}')
