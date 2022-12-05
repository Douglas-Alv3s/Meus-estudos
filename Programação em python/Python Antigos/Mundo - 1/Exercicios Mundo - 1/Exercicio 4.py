# Dissecando uma Variavel

coisa = input('Digite qualquer coisa do teclado: ')

print('É numerico?', coisa.isnumeric())
print('É do alfabeto?', coisa.isalpha())
print('É do alfabeto e numerico? ',coisa.isalnum())
print('É um numero decimal? ',coisa.isdecimal())
print('É espaço? ',coisa.isspace())
print('É pintável? ',coisa.isprintable())
print('É maiúsculo?' ,coisa.isupper())
print('É minusculo?',coisa.islower())
