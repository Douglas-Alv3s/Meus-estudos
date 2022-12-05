# Hotel

dias = int(input('Informe a quantidade de dias: '))


if dias > 5:
    taxa = 7.50
    valor_hotel = (150.00 * dias) + (taxa * dias)
    print(taxa)
    print(f'O valor do Hotel é: {valor_hotel}')

elif dias == 5:
    taxa = 9.00
    valor_hotel = (150.00 * dias) + (taxa * dias)
    print(taxa)
    print(f'O valor do Hotel é: {valor_hotel}')

elif dias < 5:
    taxa = 10.50
    valor_hotel = (150.00 * dias) + (taxa * dias)
    print(taxa)
    print(f'O valor do Hotel é: {valor_hotel}')
