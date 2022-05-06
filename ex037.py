#leia numero inteiro qualquer e peça qual a base de conversão
#1 para binário
#2 para octal
#3 para hexadecimal

numero = int(input('Digite um numero inteiro: '))
print('''Escolha uma base de conversão:
      [1] Binário
      [2] Octal
      [3] Hexadecimal''')
opcao = int(input('Sua opção foi: '))

if opcao == 1:
    print('{} convertido para binário fica {}'.format(numero,bin(numero)[2:]))

elif opcao == 2:
    print('{} convertido para octal fica {}'.format(numero,oct(numero)[2:]))

elif opcao == 3:
    print('{} convertido para hexadecimal fica {}'.format(numero,hex(numero)[2:]))

else:
    print('Nenhuma opção escolhida')