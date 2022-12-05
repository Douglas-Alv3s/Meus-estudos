# 1. Em um trabalho escolar, um professor de matemática pediu para que os alunos escrevessem
# expressões aritméticas de forma a exercitar tal conteúdo. Em sala de aula foi dito que uma expressão
# aritmética bem formada obedece as seguintes exigências:
# • todo parênteses, colchetes ou chaves que for aberto deve ser fechado;
# • nenhum parênteses, colchetes ou chaves pode ser fechado sem antes ter sido aberto;
# • deve haver correspondência na ordem de abertura e fechamento de parênteses, colchetes ou chaves.
# Escreva um programa que recebe como entrada uma expressão aritmética e imprime sim” se a
# expressão estiver correta e não” caso contrário. Você pode assumir que os operadores e operandos
# estão escritos corretamente, pois o objetivo é verificar a abertura e fechamento de colchetes, parênteses
# e chaves. Implemente a estrutura de dados pilha da forma mais adequada para resolver o problema.


# def Verificar_Expressão_Aritmetica(Expressão):
    
#     verifica_expr= []

#     for simbolo in Expressão:
#         if simbolo == '(' or simbolo == '{' or simbolo == '[':
#             verifica_expr.append('!')
#         elif simbolo == ')' or simbolo == '}' or simbolo == ']':
#             print(len(verifica_expr))
#             if len(verifica_expr) > 0:
#                 verifica_expr.pop()
#             else:
#                 verifica_expr.append('!!')
#                 break
#     if len(verifica_expr) == 0:
#         print('Sim')
#     else:
#         print('Não')

# Verificar_Expressão_Aritmetica(Expressão = '{[()))]}')
class Função:
    def __init__(self, expressão):
        self.expressão = expressão

    def Verificar_Expressão_Aritmetica(self):
        verifica_expr = []
        for simbolo in self.expressão:
            if simbolo == '(' or simbolo == '{' or simbolo == '[':
                verifica_expr.append('!')
            elif simbolo == ')' or simbolo == '}' or simbolo == ']':
                if len(verifica_expr) > 0:
                    verifica_expr.pop()
                else:
                    verifica_expr.append('!!')
                    break
        if len(verifica_expr) == 0:
            print(f'{self.expressão} | Sim')
        else:
            print(f'{self.expressão} | Não')



função1 = Função('(1 + 2) + (3 + 4)')
função1.Verificar_Expressão_Aritmetica()

função2 =  Função('{[(1 + 2) + (3 + 4)]}')
função2.Verificar_Expressão_Aritmetica()

função3 =  Função('[()()]')
função3.Verificar_Expressão_Aritmetica()

função4 =  Função('{[()()]}')
função4.Verificar_Expressão_Aritmetica()

função5 =  Função('((')
função5.Verificar_Expressão_Aritmetica()

função6 =  Função('[()()[')
função6.Verificar_Expressão_Aritmetica()

função7 =  Função("{[()))]}")
função7.Verificar_Expressão_Aritmetica()
