ficheiro = {"Douglas": 82911111111}

ficheiro = open('Questão 3.txt','at')

for nome in ficheiro.keys():
  ficheiro.write(f"{ficheiro[nome]}: {nome}\n")
  
ficheiro.close()