# 8. Faça um programa que recebe um conjunto de
# inteiros e um valor n e verifica se existe algum
# número com valor maior que n no conjunto


conj = []
print('')
n = int(input('Digite o Valor N: '))
print('')

for i in range(5):
    conj.append(int(input(f'Digite {i+1}º Numero do conjunto: ')))

print('')


for i in range(5):
    if conj[i] > n:
        print(f'Existe o numero [{conj[i]}] no conjunto que é maior que valor: {n}')
    else:
        print('Não Existe')
