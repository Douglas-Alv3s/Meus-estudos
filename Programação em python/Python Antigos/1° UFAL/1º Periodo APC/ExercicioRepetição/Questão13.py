# 13. Algoritmo que recebe um conjunto de inteiros e dois
# números e verifica se estes dois numeros ocorrem em
# sequência no conjunto

# RECEBE UM CONJUNTO
# VERIFICA SE DOIS ELEMENTOS INFORMADOS OCORREM EM SEQUENCIA.

conj = []
num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))

print('----------------------------------------------------------------------------')

for i in range(5):
    conj.append(int(input(f'Digite o {i+1}º numero do conjunto: ')))
print('')
print('===========================================================================================')


for i in range(5):
    if conj[i] == num1:
        if conj[i+1] == num2:
            print(f'Ocorre a sequencia informada.')
        
            
    else:
        print('Não ocorre')
    