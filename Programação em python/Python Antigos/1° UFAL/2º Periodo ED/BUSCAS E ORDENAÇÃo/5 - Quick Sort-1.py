# Quick Sort do Professor

def quick_sort(lista, p, r):
    if p < r:
        q = particao(lista, p, r)
        quick_sort(lista, p, q)
        quick_sort(lista, q+1, r)
    return lista


def particao(lista, ini, fim):
    pivo = lista[len(lista)-1]
    i = ini-1
    j = fim+1
    while i < j:
        j -= 1
        while lista[j] > pivo:
            j -= 1
        i += 1
        while lista[i] < pivo:
            i += 1
        if i < j:
            lista[i], lista[j] = lista[j], lista[i]
    return j


lista = [1, 2, 9, 7, 3, 8, 6, 4]
print(particao(lista, 0, len(lista)-1))
print(lista)
