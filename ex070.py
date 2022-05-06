
total=cont=mil=maior=menor=0
seguir=''
barato =''
while True:
    nome = str(input('Digite o nome do produto: '))
    valor = int(input('Digite o valor do produto:R$ '))
    total = total + valor
    if cont ==0:
        maior=valor
        menor=valor
        barato=nome
    elif cont!=0:
        if valor>maior:
            maior=valor
        if valor<menor:
            menor=valor
            barato=nome
    cont+=1
    if valor>=1000:
        mil+=1
    seguir = input('Quer continuar(S/N): ')
    if seguir in 'Nn':
        break

print(f'\nO total foi R${total}')
print(f'Temos {mil} produto valendo mais que 1000 reais')
print(f'O mais barato foi {barato} no valor de R${menor}')