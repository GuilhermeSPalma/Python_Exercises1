#programa para verificar o que consiste na variavel que você colocou
v = input('Print the varaiable: ')
print('Your variable is upper:', v.isupper())
print('Your variable is a number:', v.isnumeric())
print('Your variable is a letter:', v.isalpha())
print('Your variable is a space:', v.isspace())
print('Your variable is a title:', v.istitle())