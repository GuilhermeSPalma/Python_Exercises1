#programa em que o computador sorteia um numero e você advinha

import random
escolha = random.randint(0,5)
chute = int(input('Em número o computador pensou de 0 a 5? '))
if chute == escolha:
    print('Você acertou!!!')
else:
    print('Você errou o número certo era {}!'.format(escolha))
