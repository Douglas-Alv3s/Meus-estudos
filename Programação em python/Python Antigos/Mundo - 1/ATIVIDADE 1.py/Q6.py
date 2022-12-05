# 6. Algoritmo que recebe duas listas e imprime a
# intersecção das duas listas

def intersecção_lista (lista_1, lista_2):
    intersecção = []

    for i in lista_1:
        for p in lista_2:
            if i == p:
                intersecção.append(i)

    print('--'*30)
    print(f'A intersecção dessas duas lista é: {intersecção}')
    print('--'*30)


l_1 = [3, 8, 2, 15, 7, 9]
l_2 = [1, 4, 10, 8, 3, 14]

intersecção_lista(l_1, l_2)

#A função desse algoritmo é: f(n): n²