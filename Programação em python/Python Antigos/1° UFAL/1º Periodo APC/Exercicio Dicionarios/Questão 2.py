'''# 2. Escreva um programa que lê duas notas de
vários alunos e armazena tais notas em um
dicionário, onde a chave é o nome do aluno. A
entrada de dados deve terminar quando for lida uma
string vazia como nome. Escreva uma função que
retorna a média do aluno, dado seu nome'''

nome_do_aluno = None
dic = {}


while nome_do_aluno != '':
  nome_do_aluno = str(input('Digite o nome do aluno: '))
 
  if nome_do_aluno != '':
    ab1 = float(input('Digite 1° Nota: '))
    ab2 = float(input('Digite 2° Nota: '))
    dic[nome_do_aluno] = [ab1, ab2] 

def mediaAluno(nome_do_aluno):
  soma = 0
  for i in dic[nome_do_aluno]:
    soma = soma + i
  media  = soma / 2
  return media

nome_do_aluno = str(input('Digite o nome do aluno: '))
print(mediaAluno(nome_do_aluno))