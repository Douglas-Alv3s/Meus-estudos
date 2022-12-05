# 1. Faça um programa que recebe um número e calcula o fatorial desse número

n = int(input('Digite o número para o calcular o fatorial: '))
calculo = n
f = 1

while(calculo > 0):
    print(calculo)
    f = f * calculo
    calculo -= 1

print(f'O fatorial de {n}! é: {f}')
