#validar dados

sexo = str(input('Informa o sexo: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dado invalido. Digite novamente: ')).strip().upper()[0]
print('Sexo {} registrado'.format(sexo))

