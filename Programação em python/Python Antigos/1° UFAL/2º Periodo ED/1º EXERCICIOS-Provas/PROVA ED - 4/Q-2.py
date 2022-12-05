
class Celula:
    item = None
    proximo = None
    
    def __init__(self,item):
        self.item = item

class Pilha:
    topo = None
    tamanho = 0
    dados = []
    
    def inserir(self,item):
        self.dados.append(item)
        celula = Celula(item)
        celula.proximo = self.topo
        self.topo = celula
        self.tamanho+=1
        
    def remover(self):
        if self.tamanho > 0:
            celula = self.topo
            item  = celula.item
            self.topo = celula.proximo
            del celula
            self.tamanho -= 1
            return item
        else:
            print('ERRO: pilha vazia')
            return None
        
    def imprimir(self):
        celula = self.topo
        while celula != None:
            print(celula.item)
            celula = celula.proximo
    
    def FRASE(self,frase):
        self.dados = list(frase)
        
        for item in frase:
          celula = Celula(item)
          celula.proximo = self.topo
          self.topo = celula
          self.tamanho+=1


    def palindromo(self):
        Inverso = []
        celula = self.topo
        while celula != None:
            Inverso.append(celula.item);
            celula = celula.proximo
        # print(reverd)
        # print(self.dados)
        if (Inverso == self.dados):
          print(f'{fraseStr}  |  Sim')
        else:
          print(f'{fraseStr}  |  Não')

pilha = Pilha()
pilha.FRASE('osso')
print(pilha.palindromo())