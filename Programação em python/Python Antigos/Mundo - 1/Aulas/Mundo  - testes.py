#FORMAS DE FAZER PRINTS, UTILIZANDO O (FORMAT)
'''
variavel = 'Douglas'

print('Formas de comportamento {:20}!!!'.format(variavel))
        #posiciona-se a esquerda do espaço
print('Formas de comportamento {:>20}!!!'.format(variavel))
        #Posiciona-se no a direita do espaço
print('Formas de comportamento {:^20}!!!'.format(variavel))
        #Posiciona-se no meio dos espaços

#O valor 20 é o espassamento que vai ocupar

print('Forma de comportamento {:=^20}!'.format(variavel))

#Para quebrar linha no meio do print usa-se [ \n ]

print('Aconteceu isso,\n Depois aconteceu isso tbm, \n E isso aqui')'''

#criar lista com valores específicos
lista= [0]*30
print(lista)