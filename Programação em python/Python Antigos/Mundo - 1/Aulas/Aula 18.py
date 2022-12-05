'''dados = ['Pedro', 25]
dados1 = ['Mara', 19]
dados2 = ['João', 32]


pessoas = []
pessoas.append(dados[:])
pessoas.append(dados1[:])
pessoas.append(dados2[:])

print(pessoas)
print(pessoas[2][0])'''

# ####################################################################
# Copia Normal de lista pra outro lista, com mais de um dado 
'''Teste = []
Teste.append('Gustavo')
Teste.append(40)

galera = []
galera.append(Teste[:])

Teste[0] = 'Maria'
Teste[1] = '22'
galera.append(Teste[:])'''

# Adicionar varias sublistas através de um [for] usando substituindo os itens!!!
'''Galerinha = []
Teste1 = ['Nome', 'Idade']

for i in range(3):
    Teste1[0] = (input(str('Digite o nome do aluno: ')))
    Teste1[1] = (int(input('Digite a idade: ')))
    Galerinha.append(Teste1[:])

print(Galerinha)'''

# Adicionar varias sublistas atravésde um [for] usando o comando clear().
Galerinha = []
dados = []

for i in range(3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    Galerinha.append(dados[:])
    dados.clear()

print(Galerinha)