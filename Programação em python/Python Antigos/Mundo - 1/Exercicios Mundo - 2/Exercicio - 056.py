'''Desenvolva um programa que leia  o nome, idade e sexo de 4 pessoas. No
final do programa, mostre:

    *A media de idade do grupo
    *Qual o nome do homem mais velho?
    *Quantas mulheres tem menos de 20 anos.'''




maior_idade = 0
mulheres = 0
média = 0
nomemaisvelho = ''
soma = 0

for p in range(4):
    print('=-'*10, end='')
    print('{}ª Pessoa!!!'.format(p+1), end='')
    print('=-'*10,end='')
    
    print('')
    
    nome = str(input(f'Digite o nome: '))
    idade = int(input(f'Digite a idade: '))
    sexo = str(input(f'sexo [M]/[F] : ')).strip().upper()

    if sexo == 'M' and idade > maior_idade:
        maior_idade = idade 
        nomemaisvelho = nome

    soma = soma + idade
    media = soma/4 

    if sexo == 'F' and idade < 20:
        mulheres = mulheres + 1

print('=-'*10, end='')
print('')
print('A idade média do grupo é: {}'.format(media))
print('')
print('=-'*10, end='')
print('')
print(f'O homem mais velhor tem {maior_idade} e se chama {nomemaisvelho}')
print('')
print('=-'*10, end='')
print('')
print('A quantidade de mulheres com menos de 20 anos é: {}'.format(mulheres))
print('')
print('=-'*10, end='')