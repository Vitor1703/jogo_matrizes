lista = []

while True:
    valor = float(input("Digite um valor: "))
    if valor in lista:
        print("Esse valor já existe na lista")
        continue

    if valor != 0:
        lista.append(valor)

    else:
        lista.sort()
        print(lista)
        break