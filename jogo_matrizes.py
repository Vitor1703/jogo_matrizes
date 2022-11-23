import random

class Matriz:
    def _init_(self, row, col, name):
        self.linha = row
        self.coluna = col
        self.nome = name

    def matrizBot(self):
        matriz = []
        linha = []

        while len(matriz) != self.linha:
            n = random.randint(0,99)
            linha.append

            if len(linha) == self.coluna:
                matriz.append(linha)
                linha = []

        return matriz

    def matrizJogador(self):
        matriz = []
        linha = []

        print()
        print(f'OK {self.nome}, agora vamos adicionar os valores em sua matriz {self.linha}/{self.coluna}')
        print()

        while len(matriz) != self.linha:
            n = int(input('Digite o valor(De 0 a 99): '))
            linha.append

            if(len(linha) == self.coluna):
                matriz.append(linha)
                linha = []

        return matriz

    def comparaMatriz(self, m1, m2):
        pBot = 0
        pPes = 0

        for l in range(self.linha):
            for c in range(self.coluna):
                if m1[l][c] > m2[l][c]:
                    pBot += 1
                else:
                    pPes += 1

        if pPes > pBot:
            print(f'\nParabéns {self.nome} você ganhou\n')
        elif pPes < pBot:
            print('\nNão foi dessa vez\n')
        else:
            print('\nEmpatou!!\n')

        print(f'\nPontuação {self.nome}: [{pPes}]\nPontuação BOT: [{pBot}]\n')

nomeJogador = str(input('Olá jogador, digite seu nome --> '))
linhas = int(input('Digite a quantidade de linhas da sua MATRIZ --> '))
colunas = int(input('Digite a quantidade de colunas da sua MATRIZ --> '))

matriz = Matriz(linhas, colunas, nomeJogador)
matrizBot = matriz.matrizBot()
matrizJogador = matriz.matrizJogador()

print()
print(f'Matriz BOT --> {matrizBot}')
print(f'Matriz {nomeJogador} --> {matrizJogador}')

matriz.comparaMatriz(matrizBot, matrizJogador)