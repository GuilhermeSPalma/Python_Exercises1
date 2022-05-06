#aprovar emprestimo
#pergunta o valor a casa, salario do comprador e quantos anos vai pagar
#Calcula o valor mensal de porestação sabendo que não pode exceder 30% do salário mensal ou será negado

valor = float(input('Qual o valor da casa: '))
salario = float(input('Qual o seu salário: '))
anos = int(input('Quantos anos você deseja pagar: '))

mes = anos*12
prestacao = valor/mes
trintaporcento = salario*0.3

print('Irá pagar R${:.2f} por mês.'.format(prestacao))

if prestacao<=trintaporcento:
    print('Seu emprestimo foi aprovado!!')

else:
    print('Seu emprestimo foi negado')

