from math import hypot

co = float(input('comprimento do cateto oposto:'))
ca = float(input('comprimento do cateto adjacente:'))
#hi = (co ** 2 + ca ** 2) ** (1/2)
hi = hypot(co, ca)
print('hipotenusa vai medir {:.2f}'.format(hi))