arquivo = open("Questão 5.txt", "w")
arquivo.write("janeiro - 40\nfevereiro - 31\nmarço - 35\nabril - 29\nmaio - 41\njunho - 25\njulho - 21\nagosto - 18\nsetembro - 25\noutubro - 28\nnovembro - 43\ndezembro - 45\n")

arquivo = open('Questão 5.txt', 'r')
Temp_mensal_Mdia = []
soma = 0
Temp_anual_M = 0

for Temp_M_mensal in arquivo:
  Temp_M_mensal = int(Temp_M_mensal.split(' - ')[1])
  Temp_mensal_Mdia.append(int(Temp_M_mensal))
for Temp_M_mensal in Temp_mensal_Mdia:
  soma = soma + Temp_M_mensal
Temp_anual_M = soma / len(Temp_mensal_Mdia)

print(f'Média da temperatura anual foi de {Temp_anual_M}')
arquivo.close()

print('-='*20)

Meses_acima = ''

print('Mêses acima da média:\n')
for index, Temp_M_mensal in enumerate(Temp_mensal_Mdia):
  if(Temp_M_mensal > Temp_anual_M):
    arquivo = open('5.txt', 'r')
    mês = arquivo.readlines()[index]
    arquivo.close()
    Meses_acima = Meses_acima + mês
print(Meses_acima)