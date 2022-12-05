#quinta questão.
def lista(nota):
  atual = []
  for c in nota:
    menor = min(nota)
    maior = max(nota)
    outras = ((c - menor)/(maior - menor))*10
  
  if menor < maior:
    menor = 0
  if maior > menor:
    maior = 10
  atual.append(menor)
  atual.append(maior)
  atual.append(outras)
  return atual


nota = []

for c in range(1, 4):
  #nome = str(input(f'Nome do {c}° aluno: '))
  notas = float(input(f'Nota do {c}° aluno: '))
  nota.append(notas)

print(lista(nota))