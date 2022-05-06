#soma dos pares

soma=0
cont=0
for num in range(0,7):
    numero = int(input('Digite um numero: '))
    if numero % 2==0:
        soma = numero+soma
        cont = cont+1
print('A soma dos {} numeros pares foi de {}. '.format(cont,soma))