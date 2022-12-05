# 10. Algoritmo que recebe uma palavra e imprime 
# o reverso dessa palavra

print('Digite uma frase: ')
texto = str(input(''))

reverso = ''
tamanho = len(texto)


while tamanho > 0:
    reverso = reverso + texto[tamanho - 1]
    tamanho = tamanho - 1
print(f'O reverso de {texto} é : {reverso}')