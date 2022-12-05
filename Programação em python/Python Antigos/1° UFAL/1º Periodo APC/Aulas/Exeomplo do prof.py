def VerificarLucro (lista):
    i = 0
    Lucro_verificar = 10000000

    while i <= len(lista):
        money = (lista[i][1])
        nome_empresa = (lista[i][0])

        if money == Lucro_verificar:
            print(f'A empresa com lucro de R$10.000.000 foi {nome_empresa}')
            break
        else:
            i += 1
        
empresa = [['Brama', 45000000], ['coca',185006], ['cajuina', 10000000]]
VerificarLucro(empresa)