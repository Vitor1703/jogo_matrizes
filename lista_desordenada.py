lista = []
valor = None

while valor != 0:
    valor = float(input("Digite um valor: "))

    lista.append(valor)


if 2 in lista:
    print("O valor 2 esta na lista")

lista.remove(0)
print(f"Tamanho da lista: {len(lista)}")
lista.sort(reverse=True)
print(f"Lista desordenada: {lista}")