# 2. Identificar os valores de um conjunto que estão abaixo da 
# média do conjunto

def abaixoMEDIA (conjunto):
    somatotal = media_conj = total = 0
    abaixo_m = []


    for i in conjunto:
        somatotal += i 
        total += 1
        media_conj = somatotal/total
    for i in  conjunto:
        if media_conj > i: 
            abaixo_m.append(i)

    print('--'*30)
    print('Os valores que estão abaixo da média {:.2F} são:{}'.format(media_conj, abaixo_m))
    print('--'*30)



CONJUNTO = [9, 5, 3, 7, 10, 1, 4]
abaixoMEDIA(CONJUNTO)

#A função desse algoritmo é: f(n): 2n