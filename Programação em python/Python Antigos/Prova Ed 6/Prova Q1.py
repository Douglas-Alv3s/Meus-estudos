class Table:
    table = []
    m = 0
    tamanho = 0

    
    def __init__(self, m):
        self.table = [('L', '')]*m
        self.m = m

    
    def estaCheia(self):
        return self.tamanho == self.m

    def estaVazia(self):
        return self.tamanho == 0

    def hash_1(self, num):
        num_d = [int(a) for a in str(num)]
        if len(num_d) == 4:
            a = str(num_d[0]) + str(num_d[1])
            b = str(num_d[2]) + str(num_d[3])
            soma = int(a) + int(b)
            resultado = soma % m
            print(resultado)
            return resultado
        else:
            return num % 10
        
    
    def inserir_1(self,x):
        if not self.estaCheia():
            h = self.hash_1(x)
            if self.table[h][0] != 'O':
                self.table[h] = ('O',x)
                self.tamanho +=1
            else:
                j = 1
                while self.table[self.hash_1(h+j)][0] == 'O':
                    j +=1
                self.table[self.hash_1(h+j)] = ('O',x)
                self.tamanho +=1

    def hash_2(self, num):
        num_d = [int(a) for a in str(num)]
        if len(num_d) == 4:
            a = str(num_d[0]) + str(num_d[1])
            b = str(num_d[2]) + str(num_d[3])
            mult = int(a) * int(b)
            resultado = mult % m
            return resultado
        else:
            return num % 10 

    def inserir_2(self,x):
        if not self.estaCheia():
            h = self.hash_2(x)
            if self.table[h][0] != 'O':
                self.table[h] = ('O',x)
                self.tamanho +=1
            else:
                j = 1
                while self.table[self.hash_2(h+j)][0] == 'O':
                    j +=1
                self.table[self.hash_2(h+j)] = ('O',x)
                self.tamanho +=1

    def remover(self, x):
        if not self.estaVazia():
            h = self.hash_1(x)
            if self.table[h][1] == x:
                self.table[h] = ('R', '')
                self.tamanho -= 1
            else:
                j = 1
                while j < self.m and self.table[self.hash_1(h+j)][0] != 'L' and self.table[self.hash_1(h+j)][1] != x:
                    j += 1
                if j == self.m or self.table[self.hash_1(h+j)][0] == 'L':
                    print('elemento nao existe')
                else:
                    self.table[self.hash_1(h+j)] = ('R', '')
                    self.tamanho -= 1


    def imprimir(self):
        for i in range(self.m):
            print(i, '|', self.table[i][0], '|', self.table[i][1])
        print('---')


######## EXECUÇÃO ############
m = 10

Metodo_1 = Table(m)
print('...Primeira Função...')
Metodo_1.inserir_1(1513)
Metodo_1.inserir_1(9402)
Metodo_1.inserir_1(5591)
Metodo_1.inserir_1(4792)
Metodo_1.inserir_1(8753)
Metodo_1.inserir_1(4496)
Metodo_1.inserir_1(9999)
Metodo_1.inserir_1(1234)
Metodo_1.imprimir()


Metodo_2 = Table(m)
print('...Segunda Função...')
Metodo_2.inserir_2(1513)
Metodo_2.inserir_2(9402)
Metodo_2.inserir_2(5591)
Metodo_2.inserir_2(4792)
Metodo_2.inserir_2(8753)
Metodo_2.inserir_2(4496)
Metodo_2.inserir_2(9999)
Metodo_2.inserir_2(1234)
Metodo_2.imprimir()