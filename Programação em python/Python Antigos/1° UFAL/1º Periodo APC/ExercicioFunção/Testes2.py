'''def soma (a, b):
    s = a + b
    print(s)


soma(9,10)'''

'''def contador(*num):
    tam = len(num)
    print(f'Os numeros do conjunto é {num} e a quantia de numeros nele é {tam}')


contador(5,9,3,5,6,1,9,2,4,7,8)'''


'''def dobrar (lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1



valores = []
dobrar(valores)
print(valores)
'''

'''def somar(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')


somar(5,10,5)
somar(17, 13)'''


'''def area(a, b):
    A = a * b
    print(f'A área doo terreno {a}x{b} é: {A}m²')

a = float(input('LARGURA [m]: '))
b = float(input('COMPRIMENTO [m]: '))

area(a,b)'''

###############################################

'''def lin(*texto):
    tamanho = ('-'*len(texto))
    print(tamanho)
    print(texto)
    print(tamanho)


escreva = input('')
palavra = escreva
lin(palavra)'''


'''def contador (inicio, fim, passo):
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    if inicio <= fim: 
        cont = inicio
        while cont <= fim:
            print(f'{cont} ', end='')
            cont += passo
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont} ', end='')
            cont -= passo



   

contador(1,10,1)
print('')
contador(10,0,2)
print('')
inicio = int(input('Digite o inicio: '))
fim = int(input('Digite o Fim: '))

passo = int(input('Digite o passe: '))



contador(inicio, fim, passo)'''

def maior (* conj):
    cont = maior = 0
    for valor in conj:
        print(f'{valor} ', end='')
        
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')


maior(5,9,3,9,6,10,2,1,0,6)
maior(3,5,1)
maior(9,15,13)
maior(4)