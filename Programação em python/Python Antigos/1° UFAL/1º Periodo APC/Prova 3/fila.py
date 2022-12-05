funcionarios = dict()
comissão = total = 0
while True:
  vendedor = input('Informe o nome corretor: ')
  venda = int(input('Qual o valor de sua venda: R$'))
  if venda > 50000:
    comissão = venda * 0.12
  elif venda > 30000 and venda <= 50000:
    comissão = venda * 0.095
  else:
    comissão = venda * 0.07
  total += venda

  funcionarios[vendedor] = [venda, comissão]
  adicionar = input('Adicionar mair um funcionar? [S/N]: ').upper()
  while adicionar not in 'SN':
    adicionar = input('tente novamente [S/N]: ').upper()
  if adicionar == 'N':
    break
  else:
    print()

print()
def relatorio(funcionarios, total):
  print('=-' * 45)
  for K, L in funcionarios.items():
    print(f'O funcionario: {K} fez uma venda de R${L[0] :.2f}', end=' ')
    print(f'e sua comissão foi de R${L[1] :.2f}')

  print(f'\nO faturamento total da empresa foi de R$: {total :.2f}')
  print('=-' * 45)
relatorio(funcionarios, total)
