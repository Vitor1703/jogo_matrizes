from operator import index

lista = []
maiorValor = None
menorValor = None

for i in range(5):
    valores = int(input(f"Digite o valor {i}: "))
    lista.append(valores)
    
    for i in range(len(lista)):
        if i == 0:
            maiorValor = lista[i]
            menorValor = lista[i]
        
        if lista[i] > maiorValor:
            maiorValor = lista[i]

        if lista[i] < menorValor:
            menorValor = lista[i]

print(f"Lista de dados: {lista}")
print(f"O maior valor da lista é: {maiorValor}")
print(f"O index do maior valor é: {lista.index(maiorValor)}")
print(f"O menor valor da lista é: {menorValor}")
print(f"O index do menor valor é: {lista.index(menorValor)}")
