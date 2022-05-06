#programa para dizer se ano é bissexto

import datetime
ano = int(input('Que ano quer analisar? Coloque 0 para o ano anual: '))
if ano ==0:
    ano = datetime.date.today().year
if ano%4==0 and ano % 100 !=0 or ano % 400 == 0:
    print('O ano {} é bissexto'.format(ano))
else:
    print('O ano {} não é bissexto'.format(ano))