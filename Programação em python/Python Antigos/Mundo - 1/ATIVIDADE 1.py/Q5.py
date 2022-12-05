# 5. Copiar uma lista de inteiros, retirando elementos repetidos

def listaUNICA (conjunto):
    lista = []

    num = i = 0

    tamanho = len(conjunto)
    
    print('=='*30)
    while 0 < tamanho:
        num = conjunto[i]
        if num not in lista:
            lista.append(num)
        else:
            print('Removeu o valor',num)
        
        i +=1
        tamanho -=1

    
    print('--'*30)
    print(f'Lista sem repetição {lista}')
    print('=='*30)

CONJUNTO = [9, 5, 3, 8, 5, 10, 2, 8, 4]
listaUNICA(CONJUNTO)

#A função desse algoritmo é: f(n): n