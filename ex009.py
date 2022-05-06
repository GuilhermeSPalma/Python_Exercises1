#calcular a hipotenusa

import math
cato = float(input('Cateto oposto: '))
cata = float(input('Cateto adjacente: '))
hip = math.sqrt(pow(cato,2)+pow(cata,2))
print('Sua hipotenusa foi igual a {:.2f}'.format(hip))
