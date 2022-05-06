#programa para sortear uma sequencia de uma lista

#eu 1
'''import random
n1 = str(input('Priemira pessoa: '))
n2 = str(input('Segunda pessoa: '))
n3 = str(input('Terceira pessoa: '))
n4 = str(input('Quarta pessoa: '))
lista = [n1,n2,n3,n4]
seq = random.sample(lista, k=4)
print('A sequência será \n{}'.format(seq))'''

#eu2: melhor esse
import random
n1 = str(input('Priemira pessoa: '))
n2 = str(input('Segunda pessoa: '))
n3 = str(input('Terceira pessoa: '))
n4 = str(input('Quarta pessoa: '))
#lista deve ser em colchete
lista = [n1,n2,n3,n4]
random.shuffle(lista)
print('A sequência será \n{}'.format(lista))