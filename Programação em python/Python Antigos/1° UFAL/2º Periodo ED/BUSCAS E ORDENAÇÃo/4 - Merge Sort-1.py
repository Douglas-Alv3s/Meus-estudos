def merge_sort(lista):
    return divide(lista,0,len(lista)-1)

def divide(lista, inicio, fim):
    if inicio < fim:
        meio = (inicio + fim)//2
        lista = divide(lista, inicio, meio)
        lista = divide(lista,meio + 1,fim)
        return merge(lista, inicio, meio, meio+1, fim)
    else:
        return lista

def merge(lista, i1,f1,i2,f2):
    lista_ordenada = lista.copy()
    i = i1
    j = i2
    for count in range(i1,f2+1):
        if i > f1:
            lista_ordenada[count] = lista[j]
            j+=1
        elif j > f2:
            lista_ordenada[count] = lista[i]
        elif lista[i] < lista[j]:
            lista_ordenada[count] = lista[i]
            i+=1
        else:
            lista_ordenada[count] = lista[j]
            j+=1
    lista = lista_ordenada.copy()
    return lista

lista = [3,2,-10,8,-1,5,1,4,7,9]
merge_sort(lista)