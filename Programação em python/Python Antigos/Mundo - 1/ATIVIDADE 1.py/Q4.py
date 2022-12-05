# 4. Identificar a soma máxima entre dois elementos de um 
# conjunto

def Soma_MAX (conjunto):
    maior1 = maior2 = 0

    for i in conjunto:
        if i > maior1:
            maior1 = i    

    for i in conjunto:
        if i > maior2 and i < maior1:
            maior2 = i

    soma_Max =  maior1 + maior2
    
    print('--'*30)
    print(f'A soma dos dois maiores valores da lista é {soma_Max}.')
    print('--'*30)

CONJUNTO = [2, 4, 3, 6, 10, 1, 9, 6, 7, 12]
Soma_MAX(CONJUNTO)

#A função desse algoritmo é: f(n): 2n