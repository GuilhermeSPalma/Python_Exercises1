#programa que exibe aumento do salario dependendo do valor

salario = int(input('Insira o valor do salário R$ '))
if salario>1250:
    valor = salario*1.1
else:
    valor = salario*1.15
print('O seu salario ficou R${:.2f}'.format(valor))