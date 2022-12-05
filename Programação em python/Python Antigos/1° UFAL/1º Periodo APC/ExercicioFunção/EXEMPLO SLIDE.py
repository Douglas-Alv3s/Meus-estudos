'''Ex: Cálculo de imposto de renda

● Todo mês uma empresa precisa calcular quanto de 
imposto de renda de seus funcionários irá repassar 
para a receita federal
● Regras
– Se o funcionário ganha até R$ 1500,00 ele está isento de pagar imposto
– Se ganha acima disso, precisa pagar 27% de imposto sobre o salário

Crie uma lista de salários de funcionários

– Calcule o imposto de renda para cada funcionário na lista'''

#$def calcular_imposto_de_renda (lista_salario):
lista_salario = [1220, 1500, 1700]
money_impostos = 0
cont = 0 

for salario in lista_salario:
    cont += 1
    print(f'O valor que o {cont}º Funcionario tera que pagar em imposto é: {money_impostos}')
    if salario <= 1500:
        money_impostos = 0
        print(money_impostos)
    else:
        money_impostos = salario * 27/100
        print(money_impostos)

