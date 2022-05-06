maior = 0
sidade = 0
nomevelho = ''
nomeguria = ''
menor = 0
for s in range(1,4):
    nome = str(input('Nome da pessoa {}:'.format(s))).strip()
    sexo = str(input('Sexo(M ou F): ')).strip()
    idade = int(input('Digite a idade: '))
    sidade = sidade + idade
    if s==1 and sexo in 'Mm':
        maior=idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maior:
        maior = idade
        nomevelho = nome
    if s==1 and sexo in 'Ff':
        menor=idade
        nomeguria = nome
    if sexo in 'Ff' and idade<menor:
        menor = idade
        nomeguria = nome

media = sidade/4
print('\nA média de idade é {}.'.format(media))
print('O homem mais velho tem {} anos e seu nome é {}.'.format(maior,nomevelho))
print('A guria mais nova é a {} com {} anos de idade'.format(nomeguria,menor))