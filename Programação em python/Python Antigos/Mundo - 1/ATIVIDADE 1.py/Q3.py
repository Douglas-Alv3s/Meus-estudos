# 3. Calcular o fatorial de um número

def Fatorial (num):
    print('=='*30)
    fatorial = 1
    cont = num

    while 0 < cont:
        fatorial = cont * fatorial
        cont -= 1

    print(f'O fatorial de {num}! é: {fatorial}')
    print('=='*30)

Numero = int(input('Digite o valor para fatorar: '))
Fatorial(Numero)

#A função desse algoritmo é: f(n): n