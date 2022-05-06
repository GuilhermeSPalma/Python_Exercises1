#programa para calcular seno, cosseno, e tangente

import math
ang = float(input('Digite o ângulo: '))
ang = math.radians(ang)
sen = math.sin(ang)
cos = math.cos(ang)
tang = math.tan(ang)
#O :.2f vai colocar duas casa depois da virgula
print('O valor do seno foi de {:.2f}, de cosseno foi de {:.2f} e a tangente {:.2f}.'.format(sen,cos,tang))
