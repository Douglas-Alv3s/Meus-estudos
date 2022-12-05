#4. Faça um algoritmo que copie o conteúdo de 
#uma lista para outra, eliminando valores 
#repetidos. Implemente funções para isso


def CopiarLista_sem_Repetição(lista):
  Nova_Lista = []
  
  for num in lista: 
    repetiu = False
    
    for num1 in Nova_Lista: 
      if(num == num1):
        repetiu = True
    
    if(repetiu == False):
        Nova_Lista.append(num)
  
  return Nova_Lista

print(CopiarLista_sem_Repetição([1,1,5,6,7,3,6,3,9,6,4,4,9,8,3,2,1,7,0,5])) 