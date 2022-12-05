'''1. Escreva uma função que conta a quantidade de 
vogais em um texto e armazena tal quantidade em 
um dicionário, onde a chave é a vogal considerada.'''

def Contagem_de_Vogal(texto):
  dic = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
  
  for i in texto:
    for p in dic:
      if i == p:
        dic[p]  = dic[p] + 1
  return dic

print(Contagem_de_Vogal('O trabalho socio cultural é ótimo!!'))