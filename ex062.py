#progressao aritmetica

termo = int(input('Digite o termo: '))
razao = int(input('Digite a razão: '))
numero = termo
cont =1
total = 0
mais =10
while mais !=0:
    total += mais
    while cont <=total:
        print('{} -> '.format(numero), end='')
        numero += razao
        cont +=1
    print('Pausa')
    mais = int(input('Quantos termos a mais: '))
print('FIM')