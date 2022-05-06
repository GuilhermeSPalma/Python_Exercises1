#jogo de sorteio de numero

from random import randint

numero = randint (1,10)
s=0
print('Será sorteado um número, tente advinhar')
acertou = False
while not acertou:
    resposta = int(input('Digite o palpite: '))
    s = s+1
    if resposta ==numero:
        acertou = True
    else:
        if resposta < numero:
            print('É mais')
        elif resposta > numero:
            print('É menos')
print('A resposta era {} e você encontrou em {} tentativas'.format(numero,s))