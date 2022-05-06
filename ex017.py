#digitar frase e dar agumas informações

frase = str(input('Digite uma frase: ')).strip().lower()
rept = frase.count('a')

frletra = frase.find('a')+1
ultletra = frase.rfind('a')+1

print('A letra A apareceu {} vezes.'.format(rept))
print('A primeira letra A apareceu na posição {}'.format(frletra))
print('A ultima letra A apareceu na posição {}'.format(ultletra))
