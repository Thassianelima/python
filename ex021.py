nome = str(input('digite seu nome completo')).strip()
print('analisando seu nome')
print(' seu nome em maiuscula é {}'.format(nome.upper()))
print('seu nome em minuscula é {}'.format(nome.lower()))
print('seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))
print('seu primeiro nome tem {} letras'.format(nome.find(' ')))