from math import radians, sin, cos, tan
angulo = float(input('degite o angulo que voçe deseja:'))
seno = sin(radians(angulo))
print('o angulo de {:.2f} tem o seno de {:.2f}'.format(angulo, seno))
cosseno = cos(radians(angulo))
print('o angulo de {:.2f} tem o cosseno de {:.2f}'.format(angulo, cosseno))
tangente = tan(radians(angulo))
print('o angulo de {} tem o tangente de {:.2f}'.format(angulo, tangente))