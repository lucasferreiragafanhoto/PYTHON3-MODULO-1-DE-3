larg = float(input('largura da parede:'))
alt = float(input('altura da parede:'))

area = larg * alt

print('sua parede tem a dimensão de {}X{} e sua area é de {}m2.'.format(larg, alt, area))

tinta = area / 2

print('para pintar essa parede voçê precisara de {}l de tinta.'.format(tinta))