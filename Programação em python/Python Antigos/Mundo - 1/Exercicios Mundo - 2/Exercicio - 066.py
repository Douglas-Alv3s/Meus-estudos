dis_usuario = (1,2, 'Noemy')
dis_motoristas = [(3,4, 'Ronaldo'), (7,4, 'Carlos'), (1,4, 'Bob'), (8,2, 'Ana'), (5,2, 'Clara'), (2,2, 'Gil')]

def dist_euclidiana(tuplaU, tuplaM):
  xu = tuplaU[0]
  yu = tuplaU[1]
  xm = tuplaM[0]
  ym = tuplaM[1]
  de = ((xu - xm)**2) + ((yu - ym)**2)
  return  de ** 0.5

def insertOrd(lista, valor, nome):
    inicio, fim = 0, len(lista)
    while inicio < fim:
        meio = (inicio + fim) // 2
        if valor < lista[meio][0]:
            fim = meio
        else:
            inicio = meio + 1
    lista.insert(inicio, (valor, nome))
    return lista

def ord_motorista(tuplaU, ListMotorista):
  list_dis_mu = []
  for TuplaM in ListMotorista:
    dist_mu = dist_euclidiana(tuplaU, TuplaM)
    insertOrd(list_dis_mu, dist_mu, TuplaM[2])
  return list_dis_mu[0][1],list_dis_mu

procurarMotorista = ord_motorista(dis_usuario, dis_motoristas)
print(procurarMotorista[0])
print(procurarMotorista[1])