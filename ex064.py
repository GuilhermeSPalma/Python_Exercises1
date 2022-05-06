cont = 0
n = 1
numero = 0
soma = 0
while n!=999:
    n = int(input('Digite um numero [999 para cancelar o algoritmo:'))
    if n<999:
        numero = n
        soma = soma + numero
        cont +=1
print('A soma é {}, a partir de {} interações'.format(soma,cont))