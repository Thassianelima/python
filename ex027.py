from random import randint
from time import sleep
computador = randint(0, 5)
print('-=-'*20)
print('Vou pensar em um numero entre 0 e 5, tente adivinhar...')
print('-=-'*20)
jogador = int(input('em que numero eu pensei?'))
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('PARABENS! você conseguiu me vencer')
else:
    print('ganhei! eu pensei o numero {} e não no {}'. format(computador, jogador))