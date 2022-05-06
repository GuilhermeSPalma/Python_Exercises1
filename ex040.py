#Le duas notas do aluno e faz a média
#Fala se ta aprovado, reprovado, recuperação(5 até 6,9)

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1+nota2)/2

if media>7:
    print('Aprovado na matéria com média {}'.format(media))

elif 5<=media<6.9:
    falta = 14-media
    print('Você está de exame com média {} e precisa tirar {}'.format(media,falta))

elif media<5:
    print('Você está reprovado com média {}'.format(media))