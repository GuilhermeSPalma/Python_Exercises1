#analisar maioridade

from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1,8):
    nasc = int(input('Que ano nasceu: '))
    idade = atual - nasc
    if idade>=21:
        totmaior+=1
    else:
        totmenor+=1

print("Tem {} pessoas de maior".format(totmaior))
print("tem {} pessoas de menor".format(totmenor))