'''3. Escreva um programa para armazenar uma agenda de telefones em
um dicionário. Cada pessoa pode ter um ou mais telefones e a chave do
dicionário é o nome da pessoa. Seu programa deve ter as seguintes
funções:

* incluirNovoNome – essa função acrescenta um novo nome na agenda, com um ou mais telefones. Ela deve receber como argumentos o nome e os telefones.

* incluirTelefone – essa função acrescenta um telefone em um nome existente naagenda. Caso o nome não exista na agenda, você deve perguntar se a pessoa deseja incluílo. Caso a resposta seja afirmativa, use a função anterior para incluiro novo nome.

* excluirTelefone – essa função exclui um telefone de uma pessoa
que já está na agenda. Se a pessoa tiver apenas um telefone, ela deve
serexcluída da agenda.

* excluirNome – essa função exclui uma pessoa da agenda.

* consultarTelefone – essa função retorna os telefones de uma pessoa na agenda.'''


import time
import os

agenda = {}

def incluirNovoNome(nome, numeros):
  if(agenda.get(nome) == None):
    agenda[nome] = numeros
  else:
    agenda[nome].append(numeros)
  print('numeros adicionados')
  time.sleep(1)
  
def incluirTelefone(nome, numero):
  if(agenda.get(nome) == None):

    def incluirTelefoneTexto():
      os.system('clear')
      print("Digite o numero de uma das opções abaixo para prosseguir")
      print("")
      print("0. Não")
      print("1. Sim")
      print("")
      opçãoit = int(input('Esse nome não existe na agerda, deseja incluir-lo?\n'))
      return opçãoit

    opçãoit = 2;
    while (opçãoit > 1):
      opçãoit = incluirTelefoneTexto()

    if(opçãoit == 1):
      agenda[nome] = [numero]
      print("Contato adicionado")
      time.sleep(1)

  else:
    agenda[nome].append(numero)
    print("numero adicionado")

def excluirTelefone(nome, numero):
  del(agenda[nome][numero])
  print("Telefone excluido")
  if (len(agenda[nome]) == 0):
    del(agenda[nome])
    print("Contato excluido")
    time.sleep(1)

def excluirNome(nome):
  del(agenda[nome])
  print("Contato excluido")
  time.sleep(1)

def consultarTelefone(nome):
  print(agenda[nome])


while (True):
    os.system('clear')
    print("Digite o numero de uma das opções abaixo para prosseguir")
    print("")
    print("1. Adicionar novo nome a agenda")
    print("2. Adicionar novo numero")
    print("3. Excluir telefone")
    print("4. Excluir nome")
    print("5. Consultar telefone")
    print("0. Sair")
    print("")
    opção  = int(input())
    if(opção <= 5):
        if(opção == 1):
            os.system('clear')
            nome = input('Qual nome deseja inserir na agenda?\n')
            numeros = []
            numero = None
            while(numero != ''):
              numero = input('Qual numero deseja adicionar a esse contato?\n')
              if(numero != ''):
                numeros.append(numero)
            opção = incluirNovoNome(nome, numeros)
        elif(opção == 2):
            os.system('clear')
            nome = input('Qual nome deseja inserir na agenda?')
            numero = input('Qual numero deseja adicionar a esse contato?\n')
            opção = incluirTelefone(nome, numero)
        elif(opção == 3):
            os.system('clear')
            nome = input('De qual pessoa deseja excluir o numero na agenda?\n')
            numero = input('Qual numero deseja excluir?')
            opção = excluirTelefone(nome, numero)
        elif(opção == 4):
            os.system('clear')
            numero = input('Qual nome deseja excluir da agenda?\n')
            opção = excluirNome(nome)
        elif(opção == 5):
            os.system('clear')
            nome = input('De qual o nome da pessoa que deseja consultar os numeros na agenda? \n')
            consultarTelefone(nome)
            print("")
            input('Pressione para voltar')
        elif(opção == 0):
            break
    else:
        opção =  int(input('Digite uma opção valida: '))