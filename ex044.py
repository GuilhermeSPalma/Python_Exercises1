#preço a pagar normal e outras formas(a partir preço normal e condição de pagamento)
#a vista 10% desconto, cartão 5%, duas vezes no cartão, 3x ou mais no cartão(20% de juros)

valor = float(input('Digite o valor do produto: '))

print('Condição 1: A vista com 10% de desconto.')
print('Condição 2: No cartão com 5% de desconto.')
print('Condição 3: Duas vezes no cartão.')
print('Condição 4: 3x ou mais no cartão(com juros).')

escolha = int(input('Digite a opção que você escolheu: '))

if escolha == 1:
    valor1 = valor*0.90
    print('O valor ficou igual a R${:.2f}'.format(valor1))

elif escolha == 2:
    valor2 = valor*0.95
    print('O valor ficou igual a R${:.2f}'.format(valor2))

elif escolha == 3:
    parcela = valor/2
    print('O valor da parcela ficou R${:.2f} em duas vezes sem juros'.format(parcela))

elif escolha == 4:
    quantidade = int(input('Diga o numero de parcelas que deseja: '))
    valor3 = valor*1.20
    parcela = valor3/quantidade
    print('O preço em {} vezes cada parcela ficou R${:.2f} e o valor total R${:.2f}'.format(quantidade,parcela,valor3))