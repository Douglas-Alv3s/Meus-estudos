# Maior e Menor valores na Lista

numeros = []
maior = 0
menor = 0 
            
for i in range(0, 5):
    numeros.append(int(input(f'Digite um valor para posição {i}º: ')))
    if i == 0:
        maior = menor = numeros[i]
    else:
        if numeros[i] > maior:
            maior = numeros[i]
        if menor > numeros[i]:
            menor = numeros[i]

print('-='*30)

print(f'Você digitou os valores {numeros}')

print(f'O maior valor digitado foi {maior} na posições ', end='')
for posição, valor in enumerate(numeros):
    if valor == maior:
        print(f'{posição}...', end='')
print()

print(f'O menor valor digitado foi {menor} na posições ', end='')
for posição, valor in enumerate(numeros):
    if valor == menor:
        print(f'{posição}...', end='')
print()