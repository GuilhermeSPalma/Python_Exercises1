import random
cont = 0
while True:
    numero = int(input('Digite um valor: '))
    escolha = str(input('Par ou impar(P/I): ')).upper().strip()[0]
    pc = random.randint(0,10)
    soma = numero+pc
    print('Você jogou {} e o computador {}, com soma de {}.'.format(numero,pc,soma))
    if escolha=='P':
        if soma%2==0:
            print('Você acertou!!\n')
            cont+=1
        else:
            print('Você perdeu!')
            break
    elif escolha=='I':
        if soma%2==1:
            print('Você acertou!!\n')
            cont+=1
        else:
            print('Você perdeu!')
            break
print(f'\nGame over! Você ganhou {cont} vezes')