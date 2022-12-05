# 12. Algoritmo que recebe uma palavra e conta
# quantas vogais há na palavra

print('Digite uma frase: ')
texto = str(input(''))
vogal = ['A','E','I','O','U']

rep = 0

for i in range(len(texto)):
    texto = texto.upper()
    if texto[i] in vogal:
        rep = rep + 1

print(f'A uma qunatida de {rep} vogais na palavra {texto}')
