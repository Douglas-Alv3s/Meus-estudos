nome = input('Digite seu nome: ')
altura = float(input('Digite sua altura: '))
sexo = input('Informe seu sexo [M ou F]:').upper()

if sexo in "mM":
    peso_ideal = (72.7 * altura) - 58
    print('O peso ideal para você é: {:.2F}'.format(peso_ideal))
elif sexo in "fF":
    peso_ideal = (62.1 * altura) - 44.7
    print('O peso ideal para você é: {:.2F}'.format(peso_ideal))