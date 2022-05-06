#programa que vai dizer alguns dados a partir de uma frase que tu der

nome = str(input('Digite o seu nome: ')).strip()

maiuscula = nome.upper()
minuscula = nome.lower()

separar = nome.split()
primeiro_nome = len(separar[0])

juncao = ''.join(separar)
quantidade = len(juncao)

print('Seu nome em maiuscula é {}'.format(maiuscula))
print('Seu nome em minuscula é {}'.format(minuscula))
print('Seu nome tem {} letras'.format(quantidade))
print('Seu primeiro nome é {} e ele possui {} letras'.format(separar[0],primeiro_nome))
