

numero = int(input('Digite o número que gostaria de ver o fatorial: '))
n=numero
mult = 1
print('Calculando fatorial {}!= '.format(numero),end='')
while n>0:
    print('{}'.format(n), end='')
    print(' x ' if n>1 else' = ', end='')
    mult = mult * n
    n = n -1
print('{}'.format(mult))