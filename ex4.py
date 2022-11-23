lista = []
listaPar = []
listaImpar = []

for i in range(10):
    valor = float(input("Digite um valor: "))

    lista.append(valor)

    if valor % 2 != 0:
        listaImpar.append(valor)
    else:
        listaPar.append(valor)

print(f"Lista geral: {lista}")
print(f"Lista dos pares: {listaPar}")
print(f"Lista impares: {listaImpar}")