# Selection Sort

# ...CUSTO: [O(n²)]


def selection(lista):
    # para cada elemento na posicao i da lista\n",
    for i in range(0, len(lista)-1):
        menor = i
        # selecionar o menor elemento\n",
        for j in range(i+1, len(lista)):  # vai ser sempre um numero maior que i
            if lista[j] < lista[menor]:
                menor = j
            # pra testes, passo a passo do processo
            print(f'valor i:{i}, valor j:{j}')

        # trocar com a posicao i
        lista[i], lista[menor] = lista[menor], lista[i]
        # pra testes, passo a passo do processo
        print('Passo a Passo...', lista)

    return lista


lista = [3, 9, 5, -8, 4, 0, 2, -10]
selection(lista)
