#analisar ano de nascimento e dizer que categoria
#0 mirim, 14 infantil, 19 junior, 20 senior, acima master

ano_atual = 2020
anopessoa = int(input('Digite o ano em que você nasceu: '))
idade = ano_atual - anopessoa

if idade<=9:
    print('Voce entra na categoria mirim.')

elif idade<=14:
    print('Você está na categoria infantil.')

elif idade<=19:
    print('Você está na categoria junior.')

elif idade==20:
    print('Você está na categoria senior.')

elif idade>20:
    print('Você está na categoria master.')