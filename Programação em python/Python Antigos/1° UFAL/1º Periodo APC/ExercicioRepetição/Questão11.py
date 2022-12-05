#11. Algoritmo que recebe uma palavra e um 
#caractere e conta as ocorrências do caractere na 
#palavra. 

print('Digite uma frase: ')
texto = str(input(''))

print('Digite a caractere para a verificação:')
caractere = str(input(''))

rep = 0

for i in range(len(texto)):
    texto = texto.upper()
    caractere = caractere.upper()


for i in range(len(texto)):
    if texto[i] == caractere:
        rep = rep + 1

print(f'O caractere [{caractere}] se repete: {rep} vezes.')

    