'''Faça um programa que leia o sexo de uma pessoas,mas só
aceite os valores "M" ou "F". Caso esteja errado, peça a
digitação novamente até ter um valor correto'''


sexo = str(input('Informe o sexo com [M/F]: ')).strip().upper()

while sexo != 'M' and sexo != 'F':
    sexo = str(input('Caractere Invalido. Informe sexo por [M/F]: ')).strip().upper()

print(f'Sexo informado valido: {sexo}')

