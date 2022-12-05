Agenda = []
dados = ['', '']

r = ''
while True:
    dados[0] = str(input('Nome: ')).lower()
    dados[1] = int(input('Número: '))
    Agenda.append(dados[:])

    for i in range(1,len(Agenda)): 
        j = i
        while j>0 and Agenda[j]<Agenda[j-1]: 
            Agenda[j-1],Agenda[j] = Agenda[j],Agenda[j-1]
            j-=1

    print(Agenda)
    r = str(input('Quer Continuar?[S/N] ')).upper().strip()
    if r == 'S' or r == 'N':
        if r == 'N':
            print('...Programa Encerrado...')
            break
    else:
        r = str(input('Caractere Invalido. Quer Continuar?[S/N] ')).upper().strip()