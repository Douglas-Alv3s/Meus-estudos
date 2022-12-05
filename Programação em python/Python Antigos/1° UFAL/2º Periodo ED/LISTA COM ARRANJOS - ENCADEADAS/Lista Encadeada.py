class Celula:
  item = None
  proximo = None

  def __init__(self,item):
    self.item  = item


class Lista_Encadeada:
  inicio = None
  quantidade = None

  def __init__(self):
    self.quantidade = 0

    #verificar se esta vazia
  def estaVazia(self):
    return self.quantidade == 0

    #inserir
  def inserir(self,item,pos):
    if self.estaVazia():
      self.inicio = Celula(item)
      self.quantidade+=1
    else:
      if pos <= self.quantidade:
        p = self.inicio
        for i in range(pos-1):
          p = p.proximo
        aux = Celula(item)
        aux.proximo = p.proximo
        p.proximo = aux
        self.quantidade +=1
      else:
        print('operacao invalida')
    
  def adicionar(self, item):
    if self.estaVazia():
      self.inicio = Celula(item)
      self.quantidade+=1
    else:
      p = self.inicio
      while p.proximo!= None:
        p = p.proximo
      aux = Celula(item)
      p.proximo = aux
      self.quantidade +=1

  #remover
  def remover(self,pos):
    if not self.estaVazia():
      if pos <= self.quantidade:
        if pos == 0:
          aux = self.inicio
          self.inicio = aux.proximo
          item = aux.item
          del aux
          self.quantidade -= 1
          return item
        else:
          p = self.inicio
          for i in range(pos-1):
            p = p.proximo
          aux = p.proximo
          item = aux.item
          p.proximo = aux.proximo
          self.quantidade -=1
          del aux
          return item
      else:
        print('operacao invalida')
    else:
      print('operacao invalida')

    #imprimir
  def imprimir(self):
      p = self.inicio
      while p!= None:
        print(p.item)
        p = p.proximo
      print('---')