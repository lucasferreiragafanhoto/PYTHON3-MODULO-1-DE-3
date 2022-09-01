frase = str(input('digite uma frase:'.upper().strip()))

print('a letra aparece {} vezes na frase'.format(frase.count('A')))

print('a primeira letra apareceu na posição {}'.format(frase.find('A')+1))

print('A útima letra A aparece na posição {}'.format(frase.rfind('A')+1))


