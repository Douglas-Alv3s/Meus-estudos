def busca_bin(lista,chave,ini,fim):
    if ini > fim:
        return -1
    meio = (ini+fim)//2
    print('meio:',meio)
    #verificar caso base\n",
    if chave == lista[meio]:
        return meio
    else:
        if chave < lista[meio]:
            return busca_bin(lista,chave,ini,meio-1)
        else:
            return busca_bin(lista,chave,meio+1,fim)

lista = [1, 2, 3, 4, 5, 6, 7,8]

inicio = 0
final = len(lista)

chavi = int(input('chave: '))

busca_bin(lista, chavi, inicio, final)