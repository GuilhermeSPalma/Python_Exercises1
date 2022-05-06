
resp ='S'
soma = quant = media = maior = menor = 0
while resp in 'sS':
    num = int(input('Dgitie o numero: '))
    soma += num
    quant += 1
    if quant ==1:
        maior = menor = num
    else:
        if num>maior:
            maior = num
        elif num<menor:
            menor = num
    resp = str(input('Quer continuar? (s/n): ')).upper().strip()[0]
media = soma / quant
print('Acabou')

print('maior valor foi {} e o menor foi {}'.format(maior,menor))
print('A média foi de {:.2f} e foram {} numeros'.format(media,quant))