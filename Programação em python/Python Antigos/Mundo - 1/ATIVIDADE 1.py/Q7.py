# 7. Algoritmo que tenta quebrar uma senha de 
# quatro dígitos numérico

def QuebraSenha (num):
    print('=='*40)
    print(f'Senha: {num}')
    a = list(num)
    senha_int = int(''.join(a))
    listaInt = [int(i) for i in num]

    quebra_senha = [0, 0, 0, 0]

    percorrer = -1
    i = 0
    contagem = 00

    print('--'*40)

    
    if senha_int >= 0000 and senha_int <= 9999:
        while listaInt != quebra_senha:
            percorrer += 1
            if listaInt[i] == percorrer:
                quebra_senha[i] = percorrer
                i += 1
                contagem = contagem + percorrer
                percorrer = -1
                print('PROCESSO: ',quebra_senha)
                    
        print('--'*40)
        print(f'A senha informada foi {num} e necessitou de {contagem} tentativas para quebra-la.')
        print('=='*40)
        

numero = (input('Senha[4 Dígitos]: '))
QuebraSenha(numero)

#A função desse algoritmo é: f(n): n