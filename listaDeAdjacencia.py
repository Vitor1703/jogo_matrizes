class Grafo:
    def __init__(self, pVertices):
        self.Vertices = pVertices
        self.Grafo = [[] for i in range(self.Vertices)]

    def AdicionaAresta(self, pV1, pV2, pPeso):
        if pV1 == pV2:
            self.Grafo[pV1].append([pV2, pPeso])
        else:
            self.Grafo[pV2].append([pV2, pPeso])
            self.Grafo[pV1].append([pV1, pPeso])


    def MostrarLista(self):
        for i in range(self.Vertices):
            print(f'{i}: ', end=' ')

            for j in self.Grafo[i]:
                print(j, '->', end=' ')
            print()
            
oGrafo1 = Grafo(4)
oGrafo1.AdicionaAresta(0, 1, 2)
oGrafo1.AdicionaAresta(0, 2, 5)
oGrafo1.AdicionaAresta(1, 2, 7)
oGrafo1.AdicionaAresta(0, 0, 1)

oGrafo1.MostrarLista()