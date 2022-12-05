'''1. Uma empresa de vendas tem o seu sistema hospedado em núvem e seus aplicativos cliente se comu-
nicam com o servidor via API. Uma das funções do sistema é calcular a comissão de seus vendedores. A
empresa paga ao vendedor uma comissão calculada de acordo com o valor de suas vendas. Se o valor da
venda de um vendedores for maior que R$ 50.000.00 a comissão será de 12% do valor vendido. Se o valor
da venda do vendedor estiver entre R$ 30.000.00 e R$50.000.00, a comissão será de 9.5%. Em qualquer
outro caso, a comissão será de 7%. Para enviar os dados das vendas para o servidor, o programa cliente
envia uma lista de dicionários com os dados de cada vendedor. Escreva um programa que receba os
dados das vendas de vários vendedores e envia essa lista para uma função que gera um relatório contendo
nome, valor da venda e comissão de cada um dos vendedores. O relatório deve mostrar também o total
de vendas da empresa.'''

def lin():
    print('-='*20)

Pessoas_funcionario = dict()

comissao = total_vendas = 0
numero_de_f = int(input('Quantidade de funcionarios: '))

for i in range (numero_de_f):
    funcionario = input('Nome do Funcionario: ')
    venda_funcionario = int(input('Valor da venda: R$'))

    lin()
    
    if venda_funcionario > 50000:
        comissao = venda_funcionario * 0.12
    elif venda_funcionario > 30000 and venda_funcionario <= 50000:
        comissao = venda_funcionario * 0.095
    else:
        comissao = venda_funcionario * 0.07
    total_vendas =total_vendas + venda_funcionario

    Pessoas_funcionario[funcionario] = [venda_funcionario, comissao]

def relatorio(Pessoas_funcionario, total_vendas):
  
  print('+'*100)

  for p , s in Pessoas_funcionario.elementos():
    print(f'O funcionario: {p} fez uma venda de R${s[0] :.2f}', end=' ')
    print(f'e sua comissão foi de R${s[1] :.2f}')
  print('-'*100)
  
  print(f'\n Faturamento total da empresa R$: {total_vendas :.2f}')

  
relatorio(Pessoas_funcionario, total_vendas)

