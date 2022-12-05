# Merge Sort do carinha do youtube       https://youtu.be/5prE6Mz8Vh0


def mergesort(lista, inicio, fim):
    if fim == None:
        fim = len(lista)
    if(fim - inicio > 1):
        meio = (fim + inicio)//2

        # Recursão
        mergesort(lista, inicio, meio)
        mergesort(lista, meio+1, fim)
        merge(lista, inicio, meio, fim)


def merge(lista, inicio, meio, fim):
    # Cria uma lista com os elementos do lado esquerdo
    lista_esquerda = lista[inicio:meio]
    # Cria uma lista com os elementos do lado Direito
    lista_direita = lista[meio:fim]
    topo_esquerdo, topo_direito = 0, 0

    for k in range(inicio, fim):
        if topo_esquerdo >= len(lista_esquerda):
            lista[k] = lista_direita[topo_direito]
            topo_direito += 1
        elif topo_direito >= len(lista_direita):
            lista[k] = lista_esquerda[topo_esquerdo]
            topo_esquerdo += 1
        elif lista_esquerda[topo_esquerdo] < lista_direita[topo_direito]:
            lista[k] = lista_esquerda[topo_esquerdo]
            topo_esquerdo += 1
        else:
            lista[k] = lista_direita[topo_direito]
            topo_direito += 1


listaas = [5, 9, 43, 45, 1, 58, 15, 145, 0, 18, -1, 58, 41, 854, 12, 56]
lista_ordenada = mergesort(listaas, 0, len(listaas))
print(lista_ordenada)
