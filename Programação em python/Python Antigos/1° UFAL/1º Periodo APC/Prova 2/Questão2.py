#2.Um funcionário do IBGE viu o excelente trabalho que você fez no algoritmo anterior e ficou
#impressionado. Resolveu então contratá-lo para escrever um programa. O programa recebe como entrada
#um inteiro que corresponde a quantidade de pessoas entrevistadas e, em seguida, para cada pessoa
#entrevistada o programa recebe um inteiro que corresponde a idade do entrevistado. O programa deve
#calcular:

n = int(input('Quantidade de pessoas entrevistadas: '))
Quant_P = []

faixa1 = 0
faixa2 = 0
faixa3 = 0
faixa4 = 0
faixa5 = 0
for i in range(1, n + 1):
    id = int(input(f'Digite a idade {i}º '))
    if id <= 15:
        faixa1 = faixa1 + 1
    if 16 <= id <= 30:
        faixa2 = faixa2 + 1
    if 31 <= id <= 45:
        faixa3 = faixa3 + 1
    if 46 <= id <= 60:
        faixa4 = faixa4 + 1
    if id > 60:
        faixa5 = faixa5 + 1


valor_t = n 
valor_1 = faixa1/n
porcentagem_de_1 = valor_1*100


print(f'A quantidade de pessoas []: {faixa1}')
print(f'A quantidade de pessoas []: {faixa2}')
print(f'A quantidade de pessoas []: {faixa3}')
print(f'A quantidade de pessoas []: {faixa4}')
print(f'A quantidade de pessoas []: {faixa5}')

print(f'A porcentagem de pessoas na primeira faixa etaria é: {porcentagem_de_1}%')
