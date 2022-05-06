#progressão aritmética

primeiro = int(input("o primeiro terimo:"))
razao = int(input("razão: "))
decimo = primeiro + (10-1) * razao
for c in range (primeiro,decimo,razao):
    print("{}".format(c),end=' -> ')
