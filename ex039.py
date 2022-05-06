#Le a idade de um homem
#Se ainda vai ter que se alistar
#She é hora de se alistar
#Passou do tempo
#Falta que falta ou passou

idade = int(input('Digite a sua idade: '))

alistamento = 18

if idade<alistamento:
    falta = alistamento-idade
    print('Você ainda tem que se alistar em {} anos'.format(falta))

elif idade>alistamento:
    foi = idade-alistamento
    print('Você ja deveria ter se alistado em {} anos'.format(foi))
