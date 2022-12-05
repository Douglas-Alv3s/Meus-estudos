# Classe
# Sintaxe

# Marca, Mémoria Ram, Placa de video
class Computador:
    def __init__(self, marca, memoriaRam, Placa_de_Video):
        self.marca = marca
        self.memoriaRam = memoriaRam
        self.Placa_de_Video = Placa_de_Video
    
    def ligar (self):
        print('Estou Ligando...')

    def desligar (self):
        print('Estou desligando...')

    def Exibir_Configuração (self):
        print(f'Marca: {self.marca}\nMemoria Ram: {self.memoriaRam}\nPlaca de Video: {self.Placa_de_Video}')
        # return 'Marca: '+self.marca+'\nMemoria Ram: '+self.memoriaRam+'\nPlaca de Video:'+ self.Placa_de_Video


computador1 = Computador('Lenovo','8gb','intel Grapich')
computador1.ligar()
computador1.desligar()
computador1.Exibir_Configuração()




# Ligar, Desligar, Exibir Configurações