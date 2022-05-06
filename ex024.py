#Programa que voce da 3 numeros e ele diz qual o menor e maior

a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
lista = [a,b,c]
print('\nO maior número é {}'.format(max(lista)))
print('O menor número é {}'.format(min(lista)))