from random import randint
from time import sleep

computador = randint(0, 5)
print('-=-'*20)
print('vai pensar em um número entre 0 e 5 tente  adivinhar...')
print('-=-'*20)
jogador = int(input('em que numero eu pensei?'))
print('processado...')
sleep(2)
if jogador == computador:
    print('parabens ! voçê conseguiu me vencer!')

