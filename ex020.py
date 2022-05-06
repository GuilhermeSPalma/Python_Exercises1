#programa do radar eletronico para calcular multas

velocidade = int(input('Qual a velocidade do carro: '))
if velocidade >80:
    print('Você está acima da velocidade permitida')
    multa = (velocidade-80)*7
    print('Sua multa saiu pelo valor de R${:.2f}'.format(multa))
elif velocidade <=80:
    print('Você está dentro da velocidade permitida')
