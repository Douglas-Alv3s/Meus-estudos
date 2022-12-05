# 1. Você está implementando uma agenda telefônica onde, a cada inserção 
# de um novo contato, agenda é mantida ordenada. Implemente um algoritmo
#  que recebe varios nomes e números do usuário em qual .quer ordem e simule
#  a inserção desse nome na agenda. A cada nova inserção, a agenda ordenada
# é impressa na tela. Seu programa deve ter uma função para buscar nomes na 
# agenda. Implemente a forma mais eficiente de resolver o problema.



def Inserir_telefone (dados):
    for i in range(1):
        dados[0] = str(input('Nome: ')).lower()
        dados[1] = int(input('Número: '))
        Agenda.append(dados[:])


# def busca_bin(lista,chave,ini,fim):
#     if ini > fim:
#         return -1
#     meio = (ini+fim)//2
#     print('meio:',meio)
#     #verificar caso base
#     if chave == lista[meio][0]:
#         return meio
#     else:
#         if chave < lista[meio]:
#             return busca_bin(lista,chave,ini,meio-1)
#         else:
#             return busca_bin(lista,chave,meio+1,fim)

def Procurar_nome (buscar):
    for i in range(len(Agenda)):
        if buscar == Agenda[i][0]:
            print(Agenda[i])

Agenda = []
dados = ['', '']
Ordem_lista = sorted(Agenda)
print(Ordem_lista)
inicio = 0
final = len(Agenda)

while True:
    print('--'*40)
    print('[1] - Mostrar Lista.')
    print('[2] - Adicionar novo contato.')
    print('[3] - Procurar nome')
    print('[4] - Parar')
    print('--'*40)
    opções = int(input('Digite Qual opção deseja: '))
    print('-='*40)
    if opções == 1:
        print(Ordem_lista)
    elif opções == 2:
        Inserir_telefone(dados)
        Ordem_lista = sorted(Agenda)
        print(Ordem_lista)
    elif opções == 3:
        Nome = str(input('Buscar nome: '))
        Procurar_nome(Nome)
    elif opções == 4:
        print('Programa Encerrado...')
        break
    else:
        opções = int(input('Opção Invalida. Digite [1] [2] [3] [4]'))
        print('--'*40)
        print('[1] - Mostrar Lista.')
        print('[2] - Adicionar novo contato.')
        print('[3] - Procurar nome')
        print('[4] - Parar')
        print('--'*40)




