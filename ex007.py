#calcula quantos litro de tinta por area
larg = float(input('Digite a largura da parede: '))
alt = float(input('Digite a altura da parede: '))
area = larg*alt
tint = area/2
print('A área da sua parede é de {}m², sendo então necessário de {}l de tinta'.format(area,tint))