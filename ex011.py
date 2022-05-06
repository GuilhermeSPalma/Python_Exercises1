#programa para pegar nome aleatorio em uma lista

#eu
import random
n1 = str(input('Primeira pessoa: '))
n2 = str(input('Segunda pessoa: '))
n3 = str(input('Terceira pessoa: '))
n4 = str(input('Quarta pessoa: '))
galera = [n1,n2,n3,n4]
sh =  random.choice(galera)
print('O ganhador foi {}!'.format(sh))