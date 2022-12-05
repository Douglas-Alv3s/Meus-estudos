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