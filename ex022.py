#programa para caluclar valor de viagem por km, sendo que acima de 200 o preço muda

dist = int(input('Digite a distância da viagem: '))
if dist>200:
    valor = dist*0.45
elif dist<=200:
    valor = dist*0.5
print('O valor da sua viagem saiu por R${:.2f}'.format(valor))
