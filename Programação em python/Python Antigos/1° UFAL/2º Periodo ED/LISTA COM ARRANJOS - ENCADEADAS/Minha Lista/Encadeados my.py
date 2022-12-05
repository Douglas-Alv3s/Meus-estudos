from msilib.schema import Class


class Celula:
    item = None
    proximo = None

    def __init__(self, item):
        self.item = item

###############################


class ListaEncadeada:
    inicio = None
    quantidade = None

    def __init__(self):
        self.quantidade = 0

    # Verifica se está vazia
    def EstaVazia(self):
        return self.quantidade == 0

    # Função inserir das listas Encadeadas
    def inserir(self, pos, item):
        if self.EstaVazia():
            self.inicio = Celula(item)
            self.quantidade += 1
        else:
            if pos <= self.quantidade:
                p = self.inicio
                for i in range(pos - 1):
                    p = p.proximo
                aux = Celula(item)
                aux.proximo = p.proximo
                p.proximo = aux
                self.quantidade += 1
            else:
                print('Operação Invalida...')

    # Função de remover das listas encadeadas
    def remover(self, pos):
        if not self.EstaVazia():
            if pos <= self.quantidade:
                if pos == 0:
                    aux = self.inicio
                    self.inicio = aux.proximo
                    item = aux.item
                    p.proximo = aux.proximo
                    self.quantidade -= 1
                    del aux
                    return item
                else:
                    p = self.inicio
                    for i in range(pos-1):
                        p = p.proximo
                    aux = p.proximo
                    item = aux.item
                    p.proximo = aux.proximo
                    self.quantidade -= 1
                    del aux
                    return item
            else:
                print('Operação Invalida...')
        else:
            print('Operação Invalida...')

    # imprimir
    def imprimir(self):
        p = self.inicio
        while p != None:
            print(p.item)
            p = p.proximo
        print('---')
