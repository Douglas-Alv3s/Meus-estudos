# 7. Algoritmo que tenta quebrar uma senha de 
# quatro dígitos numérico

senha = input('Senha: ')
quebra_senha = ''
a = b = c = d = 0 
contagem = 0

for a in range(10):
    for b in range(10):
        for c in range(10):
            for d in range(10):
                contagem +=1
                quebra_senha = str(a) + str(b) + str(c) + str(d)
                if senha == quebra_senha:
                    print(f'Senha quebrada {quebra_senha} e tentativas {contagem}')


# f(n): 62^n