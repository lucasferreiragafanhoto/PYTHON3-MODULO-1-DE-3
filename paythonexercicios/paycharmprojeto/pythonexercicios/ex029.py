
velocidade: float = float(input('qual é a velocidade atual do carro?'))
if velocidade > 80:
    print('MULTADO! voçê excedeu o limite permitidido que e de 80 km/h')
    multa: float = (velocidade - 80) * 7
    print('voçê deve pegar uma multa de  {} R$!'.format(multa))
    print('tenha um bom dia ! dirija com seguraça!')



