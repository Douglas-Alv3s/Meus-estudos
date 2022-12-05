'''Crie um programa que leia dois valores e mostre um menu na tela:

[1]Somar
[2]Multiplicar
[3]Maior 
[4]Novos números 
[5]Sair do Programa'''


def lin ():
    print('=-'*20)


valor1 = int(input('Digite o 1º Valor: '))
valor2 = int(input('Digite o 2º Valor: '))

lin()

programa = 0
soma = 0
multiplica = 0
maior = 0


while programa != 5:
    print(' [1]Somar;\n [2]Multiplicar;\n [3]Maior;\n [4]Novos números;\n [5]Sair do Programa.')
    lin()
    programa = int(input('Digite o que desejas: '))
    lin()
    lin()
    if programa == 1:
        soma = valor1 + valor2
        print(f'A soma de {valor1} com {valor2} é: {soma}')
        lin()
        lin()
    if programa == 2:
        multiplica = valor1 * valor2
        print(f'A multiplicação de {valor1} com {valor2} é: {multiplica}')
        lin()
        lin()
    if programa == 3:
        if valor1 > valor2:
            maior = valor1
            print(f'O maior valor informado é: {maior}')
            lin()
            lin()
        else:
            maior = valor2
            print(f'O maior valor informado é: {maior}')
            lin()
            lin()
    if programa == 4:
        valor1 = int(input('Digite o novo valor do 1º: '))
        valor2 = int(input('Digite o novo valor do 2º: '))
        lin()
        lin()

print('+'*25)
print('+ Programa encerrado! +')
print('+'*25)