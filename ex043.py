#analisar peso e altura e calcula IMC
#diz abaixo peso(18,5) peso ideal(28.5 até 25) sobrepeso(25 e 30) obesidade(30 até 40) obesidade mórbida (acima de 40)

peso = float(input('Digite o seu peso: '))
altura = float(input('Digite sua altura: '))

imc = (peso/((altura)**2))

if imc<18.5:
    print('Você está abaixo do peso, seu IMC foi igual a {:.2f}'.format(imc))

elif 18.5<imc<25:
    print('Você está no peso ideal, seu IMC foi igual a {:.2f}'.format(imc))

elif 25<imc<30:
    print('Você está sobrepeso, seu IMC foi igual a {:.2f}'.format(imc))

elif 30<imc<40:
    print('Você está na categoria obesidade, seu IMC foi igual a {:.2f}'.format(imc))

else:
    print('Você está na categoria obesidade morbida, seu IMC foi igual a {:.2f}'.format(imc))