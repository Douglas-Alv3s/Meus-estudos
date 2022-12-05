'''Crie um programa onde o usuario possa digitar cinco valores numericos 
e cadastre-os em uma lista, já na posição correta de inserção.(sem usar o sort())

no final mostre a lista ordenada'''

Lista_Num = []

for i in range(5):
    num = (int(input('Digite um valor: ')))
    if i == 0 or num > Lista_Num[len(Lista_Num)-1]:
        Lista_Num.append(num)
        print('Adicionado no final da lista...')
    else:
        pos = 0
        while pos < len(Lista_Num):
            if num <= Lista_Num[pos]:
                Lista_Num.insert(pos, num)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1

print('-='*30)
print(f'Os valores digitados em ordem foram: {Lista_Num}')

