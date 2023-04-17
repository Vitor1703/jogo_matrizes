# Student: Vitor Hugo Cavalcanti Ramos
# Teacher: Anderson Oberdan
# Content: Atividade lista de incidência

#--------------------------------------#

# Variavel: v
# Parâmetro: i
# Atributo: t
# Métodos: o

#--------------------------------------#

class Grafo:
    def __init__(self, iVertices, iArestas):
        self.tVertices = iVertices
        self.tGrafo = []

        for i in range(iVertices):
            vNovaLinha = []

            for j in range(iArestas):
                vNovaLinha.append(0) 

            self.tGrafo.append(vNovaLinha)

    def oMostrarMatrizInicio(self):
        print('A matriz de Incidências INICIAL é:')

        for i in range(self.tVertices):
            print('Vértice', i, self.tGrafo[i])

    def oMostrarMatrizFim(self):
        print('A matriz de Incidências FINAL é:')

        for i in range(self.tVertices):
            print('Vértice', i, self.tGrafo[i])


    def oAdicionarArestas(self):
        for i in range(vArestas):
            vV1 = int(input('De qual vértice SAI esta aresta? '))
            vV2 = int(input('De qual vértice INCIDE esta aresta? '))

            self.tGrafo[vV1][i] = -1
            self.tGrafo[vV2][i] = 1

vVertices = int(input('Quantos vértices (pontos) tem seu Grafo? '))
vArestas = int(input('Quantas arestas (traços) tem seu Grafo? '))

print()
tGrafo1 = Grafo(vVertices, vArestas)
tGrafo1.oMostrarMatrizInicio()
print()
tGrafo1.oAdicionarArestas()
print()
tGrafo1.oMostrarMatrizFim()

        