dis_usuario = [5,5, 'Douglas']
dis_motoristas = [[5,10, 'Ana'], [8,5, 'Irineu'], [12,4, 'Jacob'], [2,5, 'Ryuki'], [5,4, 'Kira'], [2,2, 'Naruto']]

def dist_euclidiana(U, M):
  Xu = U[0]
  Yu = U[1]
  Xm = M[0]
  Ym = M[1]
  distancia = ((Xu - Xm)**2) + ((Yu - Ym)**2)
  return  distancia ** 0.5

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

def ordenar_motorista(U, ListMotorista):
  list_dis_mu = []
  for M in ListMotorista:
    dist_mu = dist_euclidiana(U, M)
    insertOrd(list_dis_mu, dist_mu, M[2])
  return list_dis_mu[0][1],list_dis_mu

procurarMotorista = ordenar_motorista(dis_usuario, dis_motoristas)

print('--'*40)
print('--'*40)
print(f'O motorista mais perto do usuario {dis_usuario[2]} foi o motorista [{procurarMotorista[0]}]')
print('--'*40)
print(f'A distância dos motorista em relação ao usuario {dis_usuario[2]} é\n {procurarMotorista[1]}')
print('--'*40)
print('--'*40)