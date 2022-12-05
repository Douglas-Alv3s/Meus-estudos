# Aula 16 mundo 3 é isso ai kkkkk

# METODOS DE FATIAMENTO 

from collections import _OrderedDictItemsView


fatiamento = ('Hamburguer', 'Suco', 'Pizza', 'Batata')

print(fatiamento[2])
print()
print(fatiamento[0:2])
print()
print(fatiamento[1:])
print()
print(fatiamento[-1])
print()
print(fatiamento[:-1])
print()
print(len(fatiamento))

print()
# Para percorrer a tupla

for i in fatiamento:
    print(i)
print('Comi Bastante')

print()
print()


for i in range(0, len(fatiamento)):
    print(f'Eu comi {fatiamento[i]} na posição {i}')
print('Terminei de comer')


# Para mostrar a tupla em Ordem

print(sorted(fatiamento))

