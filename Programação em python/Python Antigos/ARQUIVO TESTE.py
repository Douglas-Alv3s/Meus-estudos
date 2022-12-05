class Pessoas:

    def __init__(self):
        self.pessoas = []
        self.informações = [None]*4 
        self.Nome = None
        self.Idade = None
        self.Profissão = None
        self.Endereço = None
    
    def Dados(self):
        self.Nome = str(input('NOME: '))
        self.Idade = int(input('IDADE: '))
        self.Profissão = str(input('Profissão: '))
        self.Endereço = str(input('ENDEREÇO: '))

    def InserirDados (self):
        for i in range(0,4):
            if self.informações[i] == None:
                print(f'Não foi passado todas informações necessárias')
            else:
                self.pessoas.append(self.informações)
                print('Dados Inseridos')

    def LimparDados(self):
        self.informações.clear
    


pessoa = Pessoas()

pessoa.Dados()