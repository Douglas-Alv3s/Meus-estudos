class Celula:
	item = None
	proximo = None

	def __init__(self,item):
		self.item = item

class Lista_Encadeada:
	inicio = None
	tamanho = 0

	def __init__(self):
		self.inicio = Celula(None)

	#verificar se tá vazia
	def estaVazia(self):
		return self.tamanho == 0

	#inserir
	def inserir(self,item,pos):
		if pos <= self.tamanho:
			p = self.inicio
			for i in range(pos):
				p = p.proximo
			aux = Celula(item)
			aux.proximo = p.proximo
			p.proximo = aux
			self.tamanho+=1
		else:
			print('operacao invalida')
	
	def inserirF(self,item):
		p = self.inicio
		for i in range(self.tamanho):
			p = p.proximo
		p.proximo = Celula(item)
		self.tamanho+=1

	#remover
	def remover(self,pos):
		if not self.estaVazia() and pos<self.tamanho:
			p = self.inicio
			for i in range(pos):
				p = p.proximo
			aux = p.proximo
			p.proximo = aux.proximo
			item = aux.item
			del aux
			self.tamanho -=1
			return item
		else:
			print('operacao invalida')

	#imprimir
	def imprimir(self):
		p = self.inicio
		for i in range(self.tamanho):
			p = p.proximo
			print(p.item, end = ' ')
		print('')


class TableE:
    m = 0
    table = []

    #criar
    def __init__(self,m):
        self.m = m
        self.table = [None]*m

    def hash(self,x):
        return x % self.m

    #inserir
    def inserir(self,voto):
        if voto == 'basquete':
            voto = 5
            h = self.hash(voto)
            if self.table[h] == None:
                self.table[h] = Lista_Encadeada()
            self.table[h].inserirF(voto)
        elif voto == 'futebol':
            voto = 6
            h = self.hash(voto)
            if self.table[h] == None:
                self.table[h] = Lista_Encadeada()
            self.table[h].inserirF(voto)
        elif voto == "judo":
            voto = 7
            h = self.hash(voto)
            if self.table[h] == None:
                self.table[h] = Lista_Encadeada()
            self.table[h].inserirF(voto)
        elif voto == "volei":
            voto = 8
            h = self.hash(voto)
            if self.table[h] == None:
                self.table[h] = Lista_Encadeada()
            self.table[h].inserirF(voto)
        elif voto == 'ciclismo':
            voto = 9
            h = self.hash(voto)
            if self.table[h] == None:
                self.table[h] = Lista_Encadeada()
            self.table[h].inserirF(voto)
        else:
            None                      

    #remover
    def remover(self,x):
        h = self.hash(x)
        if self.table[h] == None:
            print('nao existe')
        else:
            self.table[h].remover(x)

    #imprimir
    def imprimir(self):
        for i in range(self.m):
            print(i,' ',end='')
            if self.table[i]!= None:
                self.table[i].imprimir()
            print('')
        print('---')


################ EXECUÇÃO ##############

tabela = TableE(5)
print(' Indices e suas respectivas representações:\n [0] Basquete Voto - 5\n [1] futebol Voto - 6\n [2] judo Voto - 7\n [3] volei Voto - 8\n [4] ciclismo Voto - 9\n')

tabela.inserir('basquete')
tabela.inserir('futebol')
tabela.inserir('futebol')
tabela.inserir('basquete')
tabela.inserir('judo')
tabela.inserir('volei')
tabela.inserir('futebol')
tabela.inserir('basquete')
tabela.inserir('futebol')
tabela.inserir('volei')
tabela.inserir('judo')
tabela.inserir('judo')
tabela.inserir('futebol')
tabela.inserir('ciclismo')
tabela.inserir('judo')


tabela.imprimir()