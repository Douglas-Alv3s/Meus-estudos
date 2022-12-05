def linha():
    print('---'*30)


numeros = [5, 3, 8, 6, 9]
print(f'Lista inicial {numeros}')

linha()

numeros[2] = 4
print(f'Substituindo um valor da lista {numeros}')

linha()

numeros.append(10)
print(f'Adicionando um elemento a lista {numeros}')

linha()

numeros.sort(reverse=True)
print(f'Invertendo a ordem dos numeros {numeros}')

linha()

numeros.insert(4, 7)
print(f'Inserindo elemento em identação especifica {numeros}')

linha()

numeros.sort()
print(f'Ordenando os numeros da lista {numeros}')

linha()

numeros.pop()
print(f'Removendo o elemento da ultima posição {numeros}')

linha()

numeros.pop(1)
print(f'Removendo em local especifico na lista {numeros}')

linha()

numeros.remove(5)
print(f'Removendo através conteudo especifico {numeros}')