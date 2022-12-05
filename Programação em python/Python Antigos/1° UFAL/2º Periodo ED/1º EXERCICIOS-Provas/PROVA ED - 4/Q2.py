class Celula:
    item = None
    proximo = None

    def __init__(self, item):
        self.item = item


class FilaEncadeada:
    inicio = None
    fim = None
    tamanho = 0

    def __init__(self):
        self.inicio = Celula(None)
        self.fim = self.inicio

    def estaVazia(self):
        return self.tamanho == 0

    def enfileirar(self, item):
        self.fim.proximo = Celula(item)
        self.fim = self.fim.proximo
        self.tamanho += 1

    def desenfileirar(self):
        if not self.estaVazia():
            aux = self.inicio.proximo
            self.inicio.proximo = aux.proximo
            item = aux.item
            del aux  # deletar o espaço de memoria para a celula
            self.tamanho -= 1

            if self.tamanho == 0:
                self.fim = self.inicio

            return item

        else:
            print('Fila vazia')

    def imprimir(self):
        aux = self.inicio.proximo
        while aux != None:
            print(aux.item)
            aux = aux.proximo
        print('---')

    def estaNulo(self):
        aux = self.inicio.proximo
        if (not aux is None) and (aux.item == "-"):
            return True
        else:
            return False


download = ['d1', 'd2', 'd3', 'd4', 'd5',
            'd6', 'd7', '-', '-', '-', 'd8', 'd9']
upload = ['u1', 'u2', '-', '-', 'u3', 'u4', 'u5', 'u6', 'u7']

trafego_Pacotes = []
tamanho_total = len(download) + len(upload)
limitador = 0

fila_download = FilaEncadeada()
fila_upload = FilaEncadeada()

for k in download:
    fila_download.enfileirar(k)

for k in upload:
    fila_upload.enfileirar(k)


while limitador < tamanho_total:
    limitador += 1

    if not fila_download.estaNulo():
        for j in range(4):
            if not fila_download.estaVazia() and not fila_download.estaNulo():
                trafego_Pacotes.append(fila_download.desenfileirar())
    else:
        while fila_download.estaNulo() == True:
            fila_download.desenfileirar()
    if not fila_upload.estaNulo():
        for j in range(2):
            if not fila_upload.estaVazia() and not fila_upload.estaNulo():
                trafego_Pacotes.append(fila_upload.desenfileirar())
    else:
        while fila_upload.estaNulo() == True:
            fila_upload.desenfileirar()

print(trafego_Pacotes)
