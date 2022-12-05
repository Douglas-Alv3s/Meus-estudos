#Primeira Questão
ficheiro = open("Questão 1.txt", "w")
ficheiro.write("5384423 Manoel\n4345566 Alberto\n3235574 Mariana")

dicionario = {}

ficheiro = open('1.txt', 'r')
for linha in ficheiro:
    Linhas = linha.split(' ')
    dicionario[Linhas[0]] = Linhas[1][:-1]
print(dicionario)
