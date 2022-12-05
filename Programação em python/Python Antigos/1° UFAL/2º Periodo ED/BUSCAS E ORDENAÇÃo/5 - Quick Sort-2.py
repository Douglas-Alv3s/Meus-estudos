# Quick Sort Youtube


def QuickSort(lista, inicio, fim):
    if inicio < fim:
        piv = partition(lista, inicio, fim)
        QuickSort(lista, inicio, piv-1)
        QuickSort(lista, piv+1, fim)


def partition(lista, inicio, fim):
    pivoT = lista[fim]
    i = inicio  # Barra Amarela - onde esta os elementos menores
    for j in range(inicio, fim):  # Barra roxa - está sempre avançando
        if lista[j] <= pivoT:
            lista[j], lista[i] = lista[i], lista[j]
            i = i + 1
    lista[i], lista[fim] = lista[fim], lista[i]
    return i

lista = [1, 2, 9, 7, 3, 8, 6, 4]
QuickSort(lista, 0, len(lista)-1)
