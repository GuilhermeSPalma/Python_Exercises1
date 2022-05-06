#progressao aritmetica

termo = int(input('Digite o termo: '))
razao = int(input('Digite a razão: '))
numero = termo
cont =1
while cont <=10:
    print('{} -> '.format(numero), end='')
    numero += razao
    cont +=1
print('FIM')