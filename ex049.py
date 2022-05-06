#tabuada do 2
num=int(input('Digite o numero que você gostaria de ver a tabuada: '))
for a in range(0,11):
    result = num*a
    print('{}x{}={}'.format(num,a,result))
print('Fim')