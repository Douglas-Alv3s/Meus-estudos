#3.Uma organização não-governamental está realizando um estudo com uma determinada comu-
#nidade. Uma das características analisadas desta comunidade foi o índice de massa corporal (IMC), com
#o objetivo de identificar as pessoas que estão abaixo do peso ideal. O IMC é calculado dividindo o peso
#(em kg) pela altura (em metros) ao quadrado (eq. 1). Você foi então contratado para criar um programa
#que automatiza o processo de computação dos dados.O programa recebe como entrada um inteiro
#ue corresponde a quantidade de pessoas entrevistadas e, em seguida, para cada pessoal entrevistada o
#programa recebe o peso e a altura do entrevistado. O programa deve calcular:

n = int(input('Quantidade de pessoas entrevistadas: '))
Quant_P = []

faixa1 = 0
faixa2 = 0
faixa3 = 0
faixa4 = 0

for i in range(1, n + 1):
    peso = float(input(f'Digite o peso {i}º: '))
    altura = float(input(f'Digite a altura {i}º: '))
    IMC = peso/altura**2


    if 18.49 >= IMC:
        faixa1 = faixa1 + 1
    elif 18.5 <= IMC <= 24.99:
        faixa2 = faixa2 + 1
    elif  25 <= IMC <= 29.99:
        faixa3 = faixa3 + 1
    elif 30 <= IMC :
        faixa4 = faixa4 + 1
    

valor_1 = faixa1/n
porcentagem_de_1 = valor_1*100

print(f'A quantidade de pessoas [Abaixo do Peso]: {faixa1}')
print(f'A quantidade de pessoas [Peso Normal]: {faixa2}')
print(f'A quantidade de pessoas [Acima do Peso]: {faixa3}')
print(f'A quantidade de pessoas [Obesidade]: {faixa4}')

print(f'A porcentagem de pessoas que estão abaixo do peso, com relação ao total de pessoas é {porcentagem_de_1}%')