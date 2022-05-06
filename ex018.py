#vai analisar o nome completo e dizer o primeiro e ultimo nome

nome = str(input('Digite seu nome completo: ')).strip().lower()
nome = nome.title()
print('Muito prazer em te conhecer!')
separar = nome.split()
ultnome = separar[-1]
print('Seu primeiro nome é {}.'.format(separar[0]))
print('Seu ultimo nome é {}.'.format(ultnome))