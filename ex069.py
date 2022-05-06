sexo = ''
resp=''
mulher=masculino=maior=0
while True:
    print('-'*20)
    print('Cadastro da pessoa')
    print('-'*20)
    idade = int(input('Digite sua idade: '))
    sexo = input('Digite o seu sexo:(M/F) ').upper().strip()[0]
    print('-' * 20)
    if sexo in 'Mm':
        masculino+=1
        if idade>=18:
            maior+=1
    elif sexo in 'Ff':
        if idade<20:
            mulher+=1
        if idade >= 18:
            maior += 1
    resp = input('Quer continuar:(S/N) ')
    if resp in 'Nn':
        break
print(f'{maior} Pessoas maior de 18')
print(f'{masculino} Homens cadastrados')
print(f'{mulher} Mulheres com menos de 20 anos')