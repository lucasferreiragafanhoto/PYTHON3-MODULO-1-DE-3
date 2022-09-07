'ifiano' == 0
from datetime import date
ano = int(input('que ano quer analisar? coloque o para analizar o ano atual'))
if ano == 0:
    ano = date.today().year
    if ano % 4 == 0 and ano % 100!= 0 or ano % 400 == 0:
        print('o ano. {} é Bissesto'.format(ano))
    else:
        print('o ano {} não é Bissesto'.format(ano))
