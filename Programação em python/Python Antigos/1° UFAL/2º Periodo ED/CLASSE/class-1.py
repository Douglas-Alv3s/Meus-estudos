# Criar uma classe com no minimo 3 propriedades para a classe carro e no minimo 3 metodos.

class Carro:
    def __init__(self,Marca, Cor, Ano, Valor):
        self.Marca = Marca
        self.Cor = Cor
        self.Ano = Ano
        self.Valor = Valor

    def analisar_carro(self):
        print(f'Marca: {self.Marca}\nCor: {self.Cor}\nAno: {self.Ano}\nValor: {self.Valor}')

    
    def comprar_carro(self,money):
        dinheiro = 0
        if self.Valor <= money: 
            dinheiro = money - self.Valor
            print('Carro Comprado. Sobrou: R$',dinheiro)
            carro1.sair_carro()
        else:
            dinheiro = money - self.Valor
            print('Dinheiro insuficiente. Falta: R$',dinheiro)
    
    def sair_carro (self):
        print('Retirando carro...')


carro1 = Carro('Uno', 'Vermelho', '2020', 12000)

carro1.analisar_carro()
carro1.comprar_carro(13000)

