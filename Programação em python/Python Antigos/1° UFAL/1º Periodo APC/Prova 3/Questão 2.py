'''2. Uma empresa possui vários funcionários e estes podem acumular alguns cargos entre os vários se-
tores da empresa. A empresa possui então uma lista com todos os funcionários e seus respectivos salários.
Como a empresa não é muito organizada em relação as finanças, alguns funcionários aparecem repetidos
na lista, porém com salário diferente, quando este funcionário acumula mais de um cargo. No entanto
na hora de pagar os funcionários, quando um funcionário está repetido na lista, ela considera apenas o
salário de maior valor para efetuar o pagamento. Faça um programa que recebe a lista de funcionários
e seus salários e retorne uma lista com os funcionários e os salários que efetivamente receberão (sem
repetições e considerando o maior dos salários em caso de repetição).

Ex: Entrada: jose 1.200, pedro 1.600, ana 1.950, jose 1.350, marta 1.850, ana 1.630, pedro 1.650,
jorge 2.350

Saída: jose 1.350, pedro 1.650, ana 1.950, marta 1.850, jorge 2.350
'''

def Corrigir_Salario(quant_de_f):
    lista_de_f = {}

    for i in range(quant_de_f):
      nome = input(f"Digite o nome do {i+1} vendedor: ")
      salario = float(input(f"Digite o valor do total de vendas do {i+1}: "))
    
      if nome not in lista_de_f.keys():
         lista_de_f[nome] = salario
      else:
        if lista_de_f[nome] < salario:
            lista_de_f[nome] = salario
    return lista_de_f

def Todos_Funcionarios(funcionarios):
    for nome, salario in funcionarios.items():
        print(f'Nome: {nome} / Salário: {salario}')
        print('-='*30)
    
quant_de_V = int(input("Digite a quantidade de vendedores da loja: "))
funcionarios = Corrigir_Salario(quant_de_V)
Todos_Funcionarios(funcionarios)
