def insertion(lista):
      #para cada elemento da lista a partir do primeiro\n",
      for i in range(1,len(lista)):
          #coloque o elemento na ordem correta pra trás\n",
          j = i
          while j > 0 and lista[j]<lista[j-1]:
              lista[j],lista[j-1] = lista[j-1],lista[j]
              j-=1
      return lista

lista = [3,9,5,-8,4,0,2,-10]
insertion(lista)