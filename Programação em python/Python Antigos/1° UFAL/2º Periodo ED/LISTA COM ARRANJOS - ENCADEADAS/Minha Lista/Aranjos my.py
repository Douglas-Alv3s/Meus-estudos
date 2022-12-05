class Lista:
    itens = None
    tamanho = None
    ultimo = None


    def __init__(self, tamanho):
        self.itens = [None]*tamanho
        self.ultimo = 0
        self.tamanho = tamanho

    def EstaCheia(self):
        return self.ultimo == self.tamanho
    
    def EstaVazia(self):
        return self.ultimo == 0
    
    def Adicionar(self, item):
        if not self.EstaCheia():
            self.itens[self.ultimo] = item
            self.ultimo += 1
        else:
            print('Operação Invalida...')

    def inserir(self, item, pos): #Função própria das listas com Arranjos.
        if not self.EstaCheia  or pos <= self.ultimo: #pós and --- faz com que seja inserido antes da ultima posição para garantir que não haja espaços em brancos:
            for i in range(self.ultimo, pos, -1):
                self.itens[i] = self.itens[i-1]
            self.itens[pos] = item
            self.ultimo +=1
        else:
            print('Operação Invalida...')

    def remover(self, pos):
        if not self.EstaVazia or pos < self.ultimo:
            item = self.itens[pos]
            for i in range(pos, self.ultimo -1):
                self.itens[i] = self.itens[i+1]
            self.ultimo -= 1
            return item
        else:
            print('Operação Invalida...')
            return None


    def imprimir(self):
        for i in range(self.ultimo):
            print(self.itens[i])
        print('---')




listinha = Lista(6)

listinha.Adicionar(5)
listinha.Adicionar(3)
listinha.Adicionar(6)
listinha.Adicionar(1)
listinha.Adicionar(10)
listinha.inserir(4, 4)

listinha.remover(7)
listinha.imprimir()

