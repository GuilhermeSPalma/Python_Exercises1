#dar medidas do triangulo
# equilatero(lados iguais), isosceles(dois igual), escaleno(todos diferente)

medida1 = int(input('Digite a medida do lado 1: '))
medida2 = int(input('Digite a medida do lado 2: '))
medida3 = int(input('Digite a medida do lado 3: '))

if medida1==medida2 and medida1==medida3 and medida2==medida3:
    print('O triangulo pe equilatero')

elif medida1==medida2 or medida2==medida3:
    print('O triangulo é isosceles')

else:
    print('O triangulo é escaleno')