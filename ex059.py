n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao !=5:
    print('''    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa''')
    opcao = int(input('\nQual opção: '))
    if opcao ==1:
        soma = n1+n2
        print('A soma é {}'.format(soma))
    elif opcao==2:
        mult = n1*n2
        print('A multiplicação é {}.'.format(mult))
    elif opcao==3:
        if n1>n2:
            maior=n1
        if n2>n1:
            maior=n2
        print('O maior número é {}'.format(maior))
    elif opcao==4:
        print('informe os números novamente')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao==5:
        print('Finalizar\n-----------------')
    else:
        print('opção invalida')
print('Fim do programa')