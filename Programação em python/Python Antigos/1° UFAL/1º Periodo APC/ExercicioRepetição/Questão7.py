#7. Faça um programa que recebe um conjunto de inteiros e 
#verifica se existe algum número negativo no conjunto.

conj = []


for i in range(5):
    conj.append(int(input(f'Digite {i+1}º Numero do conjunto: ')))

    
for i in range(5):
    if conj[i] < 0:
    
        print(f'Existe o elemento negativo: {conj[i]}')
    else:
        print('Não Existe')