# saber se numero é primo

num = int(input("digite numero"))
tot = 0
for c in range(1,num + 1):
    if num % c==0:
        print('\033[34m', end='')
        tot = tot+1
    else:
        print('\033[m', end='')
    print('{} '.format(c),end=' ')
print('\n\033[mO numero é divisel por {} vezes'.format(tot))