# mediana 

conjunto = [1, 2, 6, 7, 15, 36, 39, 40, 41, 42, 43, 47, 49, 54]

tamanho = len(conjunto)
mediano = 0

if tamanho % 2 == 0:
    print('Par')
    primeiro_numero = int(tamanho/2)-1
    segundo_numero = primeiro_numero + 1
    mediano = (conjunto[primeiro_numero] + conjunto[segundo_numero]) / 2
else:
    mediano = (tamanho/2)+0.5
    print('Ímpar')

print(conjunto[primeiro_numero])
print(conjunto[segundo_numero])
print(mediano)