Ficheiro = open("Questão 2.txt", "w")
Ficheiro.write("– 200.135.80.9\n– 192.168.1.1\n– 8.35.67.74\n– 257.32.4.5")

Ficheiro = open('Questão 2.txt', 'r')
for linha in Ficheiro:
  Linhas = linha.split('– ')
  partes = Linhas[1].split('.')

  Estado = 'Válido'

  for parte in partes:
    parte = int(parte)
    if (parte > 255):
      Estado = 'Inválido'
      break
  print(linha[:-2], "=>", Estado)

Ficheiro.close()