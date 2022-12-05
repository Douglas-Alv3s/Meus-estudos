Ficheiro = open("Questão 4.txt", "w")
Ficheiro.write("7\n8\n7\n5\n7\n4\n7\n6")

Todas_Notas = 0
soma = 0
Media = 0
Acima_Media = 0
Ficheiro = open('Questão 4.txt', 'r')
Notas = []
for nota in Ficheiro:
  nota= int(nota)
  Todas_Notas = Todas_Notas + 1
  soma = soma + nota
  Notas.append(nota)
Media = soma / Todas_Notas
for nota in Notas:
  nota= int(nota)
  if(nota > Media):
    Acima_Media = Acima_Media + 1
print(f'Foram lidas {Todas_Notas} notas')
print('-='*20)
Nota_Texto = '';
for nota in Notas:
  nota = str(nota)
  Nota_Texto = Nota_Texto + nota + ", "
print(Nota_Texto)  
print('-='*20)
print('-='*20)
print(f'Soma de todas as notas informadas é: {soma}')
print('--'*20)
print(f'A media de todas as notas é: {Media}')
print('--'*20)
print(f'As notas acima da média foi: {Acima_Media}')

Ficheiro.close()