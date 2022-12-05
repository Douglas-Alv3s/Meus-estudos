from tkinter.messagebox import YES


class Fila:
    itens = None
    inicio = None
    fim = None
    tamanho = None
    media = None
    média = None

    def __init__(self, tamanho):
        # tamanho += 1
        self.itens = [0]*tamanho
        self.inicio = self.fim = 0
        self.tamanho = tamanho
        self.media = self.média = 0
    # verificar se esta vazia
    def estaVazia(self):
        return self.inicio == self.fim

    # verificar se ta cheia
    def estaCheia(self):
        return (self.fim+1) % self.tamanho == self.inicio

    # enfileirar
    def enfileirar(self, item):
        if not self.estaCheia():
            self.itens[self.fim] = item
            self.fim = (self.fim+1) % self.tamanho
        else:
            self.desenfileirar()
            self.itens[self.fim] = item
            self.fim = (self.fim+1) % self.tamanho


    # desenfileirar
    def desenfileirar(self):
        if not self.estaVazia():
            item = self.itens[self.inicio]
            self.inicio = (self.inicio + 1) % self.tamanho
            return item
        else:
            print('Fila vazia')

    # Calcular Média
    def CalcularMedia (self):  
        self.média = 0
        self.media = 0
        for i in (self.itens):
            self.media = self.media + i
        self.média = self.media/(self.tamanho)
        print(f'A média Móvel é: {self.média}')
        print('-='*10)

    # imprimir
    def imprimir(self):
        i = self.inicio
        while i != self.fim:
            print(self.itens[i])
            i = (i+1) % self.tamanho
        print('---')


fila = Fila(4)

fila.enfileirar(5.64)
fila.enfileirar(5.75)
fila.enfileirar(5.86)
fila.enfileirar(5.46)
fila.CalcularMedia()

fila.enfileirar(5.29)
fila.CalcularMedia()

fila.enfileirar(5.21)
fila.CalcularMedia()

fila.enfileirar(5.42)
fila.CalcularMedia()

fila.enfileirar(5.75)
fila.CalcularMedia()

fila.enfileirar(5.80)
fila.CalcularMedia()

fila.enfileirar(5.95)
fila.CalcularMedia()