#programa vai dizer se tem santo no nome da cidade que voce colocar

nome = str(input('Digite o nome de uma cidade: ')).strip().lower()

posse = 'santo' in nome
print('A cidade que você citou possui o nome Santo, True or False:\n-{}'.format(posse))
