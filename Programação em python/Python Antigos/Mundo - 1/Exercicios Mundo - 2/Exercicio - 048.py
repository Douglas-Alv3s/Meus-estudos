'''Faça um programa que calcule a soma entre os numeros impares
que são multiplos de três e que se encontram no intervalo de 1 até 500.'''

somaImpar = 0

for i in range(3,500,3):
    somaImpar = somaImpar + i
print(f'A soma dos numeros multiplos de três no intervalo de 1 e 500 é: {somaImpar}')
   