import random

class Matriz:
    def __init__(self, col, row, name):
        self.coluna = col
        self.linha = row
        self.nome = name

    def matrizBot(self):
        matriz = []
        linha = []

        while len(matriz) != self.linha: # Quando o número de elementos da matriz(linhas) forem diferentes da quantidade máxima definida pelo usuário, ele ficará rodando.
            n = random.randint(0,99) # Utilizei random para adicionar os valores
            linha.append(n) # Adiciono n à linha

            if len(linha) == self.coluna: # Se a quantidade de elementos for igual à quantidade de colunas definida pelo usuário :
                matriz.append(linha) # Adiciono a linha à matriz
                linha = []

        return matriz

    def matrizUsuario(self):
        matriz = []
        linha = []

        while len(matriz) != self.linha:
            n = int(input("Digite um número: "))
            linha.append(n)

            if(len(linha) == self.coluna):
                matriz.append(linha)
                linha = []

        return matriz

    def comparaMatriz(self, m1, m2):
        pBot = 0
        pPes = 0

        for l in range(self.linha):
            line = []

            for c in range(self.coluna):
                if m1[l][c] > m2[l][c]:
                    line.append(m1[l][c])
                    pBot += 1
                else:
                    line.append(m2[l][c])
                    pPes += 1

        if pPes > pBot:
            print(f'\nParabéns {self.nome} você ganhou\n')
        elif pPes < pBot:
            print('\nNão foi dessa vez\n')
        else:
            print('\nEmpatou!!\n')

        print(f'\nPontuação {self.nome}: [{pPes}]\nPontuação BOT: [{pBot}]\n')


nomeUsuario = str(input('Olá jogador, digite seu nome: '))


matriz = Matriz(2, 2, nomeUsuario)
m1 = matriz.matrizBot()
m2 = matriz.matrizUsuario()

print()
print('Bot: ', m1)
print('Usuário: ', m2)

compara = matriz.comparaMatriz(m1, m2)
