# Busca Binaria

def busca_binaria(lista, chave, inicio, fim):
    if inicio > fim:
        return '...Não existe na lista...'

    # verificar caso base
    meio = (inicio + fim)//2
    # print(meio)
    if chave == lista[meio]:  # o meio é igual a chave.
        print('--'*30)
        return print(f'O item procurado foi encontrado na posição[{meio}] da lista.')
    else:
        if chave < lista[meio]:  # o meio e maior que a chave.
            return busca_binaria(lista, chave, inicio, meio-1)
        else:  # o meio e menor que a chave.
            return busca_binaria(lista, chave, meio+1, fim)


conjunto = [1, 3, 4, 7, 8, 11, 16, 17, 18, 19, 20]
inicio = 0
fim = len(conjunto) - 1
chave = 2

busca_binaria(conjunto, chave, inicio, fim)

# A BUSCA BINARIA só funciona quando a lista está ordenada.
