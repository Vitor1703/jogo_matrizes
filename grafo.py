class Grafo:
    def __init__(self, pVertices):
        self.Vertices = pVertices
        self.Grafo = []

        for i in range(pVertices):
            vNovaLinha = []
            for j in range(pVertices):
                vNovaLinha.append(0) 

            self.Grafo.append(vNovaLinha)

    def MostraMatriz(self):
        print('A Matriz de Adjacência é: ')

        for i in range(self.Vertices):
            print(self.Grafo[i])

    def verificaEuleriano(self):
        vContador = 0

        for i in range(self.Vertices):
            vGrau = 0

            for j in range(self.Vertices):
                if self.Grafo[i][j] != 0:
                    vGrau = vGrau + self.Grafo[i][j] 
            
            if vGrau % 2 != 0:
                vContador += 1
            
            print(f'Vértice {i} tem grau {vGrau}')

        if vContador == 0:
            print('Este é um grafo EULERIANO!')
        elif vContador == 2:
            print('Este é um grado SEMI-EULERIANO!')
        else:
            print('Não é um grafo EULERIANO!')

    def AdicionarAresta(self, pV1, pV2, pPeso): 
        self.Grafo[pV1][pV2] += pPeso
        self.Grafo[pV2][pV1] += pPeso

vVertices = int(input('Quantos vértices(grau) tem seu Grafo?'))
oGrafo1 = Grafo(vVertices)
oGrafo1.MostraMatriz()

vArestas = int(input('Quantas arestas tem o Grafo?'))
for i in range(vArestas):
    vV1 = int(input('De qual vértice sai a aresta? '))
    vV2 = int(input('Para qual vértice vai a aresta? '))
    vPeso = int(input('Qual o peso desta aresta? ')) 
    oGrafo1.AdicionarAresta(vV1, vV2, vPeso)
    print()

print()
oGrafo1.MostraMatriz()
oGrafo1.verificaEuleriano()

