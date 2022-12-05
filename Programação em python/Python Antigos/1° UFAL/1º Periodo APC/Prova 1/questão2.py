
nc1 = input('Nome Completo do Corretor 1: ')
nc2 = input('Nome Completo do Corretor 2: ')
nc3 = input('Nome Completo do Corretor 3: ')
print('')
cv1 = int(input(f'Insira o valor da venda do corretor {nc1}: '))
cv2 = int(input(f'Insira o valor da venda do corretor {nc2}: '))
cv3 = int(input(f'Insira o valor da venda do corretor {nc3}: '))
print('')
print('')

print('Relatorio da Empresa')
print('')

if cv1 > 50000:
    comissao1 = cv1 * 12/100
    print(
        f'O corretor {nc1} recebeu uma comissão de: R${comissao1} na sua venda de: R${cv1}.')
elif cv1 >= 30000 and cv1 <= 50000:
    comissao1 = cv1 * 9.5/100
    print(
        f'O corretor {nc1} recebeu uma comissão de: R${comissao1} na sua venda de: R${cv1}')
elif cv1 < 30000:
    comissao1 = cv1 * 7/100
    print(
        f'O corretor {nc1} recebeu uma comissão de: R${comissao1} na sua venda de: R${cv1}')



if cv2 > 50000:
    comissao2 = cv2 * 12/100
    print(
        f'O corretor {nc2} recebeu uma comissão de: R${comissao2} na sua venda de: R${cv2}')
elif cv2 >= 30000 and cv2 <= 50000:
    comissao2 = cv2 * 9.5/100
    print(
        f'O corretor {nc2} recebeu uma comissão de: R${comissao2} na sua venda de: R${cv2}')
elif cv2 < 30000:
    comissao2 = cv2 * 7/100
    print(
        f'O corretor {nc2} recebeu uma comissão de: R${comissao2} na sua venda de: R${cv2}')



if cv3 > 50000:
    comissao3 = cv3 * 12/100
    print(
        f'O corretor {nc3} recebeu uma comissão de: R${comissao3} na sua venda de: R${cv3}')
elif cv3 >= 30000 and cv3 <= 50000:
    comissao3 = cv3 * 9.5/100
    print(
        f'O corretor {nc3} recebeu uma comissão de: R${comissao3} na sua venda de: R${cv3}')
elif cv3 < 30000:
    comissao3 = cv3 * 7/100
    print(
        f'O corretor {nc3} recebeu uma comissão de: R${comissao3} na sua venda de: R${cv3}')

print('')
tve = cv1 + cv2 + cv3
print(f'O valor total de vendas da empresa foi de R${tve}')
