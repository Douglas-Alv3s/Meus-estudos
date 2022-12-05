# 3. Implemente uma função recursiva que, dada uma lista 
# de inteiros ordenada, busque por um valor


def acharvalor(c, Lista, inicio, final):
    metade=(inicio+final)//2
    if Lista[metade] == c :
      return print('Valor encontrado')
    else:
        if c < Lista[metade]:
            return acharvalor(c, Lista, metade-1, final)
        else:
            return acharvalor(c, Lista, metade+1, final)

def pertence(c, Lista):
    n = len(Lista)
    inicio = 0
    final = n
    return acharvalor(c, Lista, inicio, (final-1))

listinha=[1,2,3,4,5,6,7]
pertence(4, listinha)