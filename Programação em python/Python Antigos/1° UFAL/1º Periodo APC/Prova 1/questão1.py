salario = int(input('Informe o salario fixo do funcionario: '))

com = int(input('Informe a comissão fixa para a quantidade de carros: '))
num_c = int(input('Informe quantos carros o funcionario vendeu: '))
val_t = int(input('Informe o valor total das vendas: '))
print('')
print('')

comissao = (com * num_c)
vendas_t = (val_t * 5/100)

print(f'O valor da comissão de acordo a quantidade de carros é: R${comissao}')
print('')
print(f'O valor que recebeu pelas vendas: R${vendas_t}')
print('')

salario_final = (salario + comissao + vendas_t)

print(f'O salário final do vendedor nesse mês é: R${salario_final}')

