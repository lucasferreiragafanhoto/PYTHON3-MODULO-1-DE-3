distacia = float(input('qual e a distacia da sua viagem'))
print('voçê esta preste a começar uma viagem de {} km.'.format(distacia))
preço = distacia * 0.50 if distacia <= 200 else distacia * 0.45
print('e o preço da sua passagem será de R$ {:.2f}'.format(preço))