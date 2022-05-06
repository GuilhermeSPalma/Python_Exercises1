#tabuada v3

while True:
    n = int(input('Digite o valor para ver a tabuada: '))
    print('-' * 25)
    if n<0:
        break
    for c in range (1,11):
        print(f'{n} x {c}= {n * c}')
    print('-' * 25)
print('Terminou programa')
