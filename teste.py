class No: 
    def __init__(self, dado):
        self.data = dado
        self.Esquerda = None
        self.Direita = None  
    
    def __str__(self):
        return str(self.data)

# **Método criado para agilizar a definição de 2 filhos ao mesmo tempo 
    def setaFilhos(self, pEsquerda, pDireita):
        self.Esquerda = pEsquerda
        self.Direita = pDireita        

class ArvoreBinaria:
    def __init__(self, dado=None):
        if dado:
            node = No(dado)
            self.root = node 
        else:
            self.root = None 

#** Inserir aqui os códigos para balanceamento **
    def Altura(self, pNo=None):
        if pNo is None:
            vVisitandoNo = self.root
        else:
            vVisitandoNo = pNo

        vAlturaEsquerda = 0

        if vVisitandoNo.Esquerda:
            vAlturaEsquerda = self.Altura(vVisitandoNo)
        
        vAlturaDireita = 0
        
        if vVisitandoNo.Direita:
            vAlturaDireita = self.Altura(vVisitandoNo)

        return 1 + max(vAlturaEsquerda, vAlturaDireita)

    def Balanco(self, pNo=None):
        if pNo is None:
            vVisitandoNo = self.root
        else:
            vVisitandoNo = pNo

        vAlturaEsquerda = 0

        if vVisitandoNo.Esquerda:
            vAlturaEsquerda = self.Altura(vVisitandoNo.Esquerda)

        vAlturaDireita = 0

        if vVisitandoNo.Direita:
            vAlturaDireita = self.Altura(vVisitandoNo.Direita)

        return vAlturaEsquerda - vAlturaDireita

    def ExecutaBalanco(self, pNo=None):
        vBalanco = self.Balanco(pNo)

        if vBalanco > 1:
            if self.Balanco(pNo.Esquerda) > 0:
                self.RotacaoDireita(pNo)
            else:
                self.RotacaoEsquerdaDireita(pNo)
        elif vBalanco < -1:
            if self.Balanco(pNo.Direita) < 0:
                self.RotacaoEsquerda(pNo)
            else:
                self.RotacaoDireitaEsquerda(pNo)

    def RotacaoEsquerda(self, pNo=No):
        pNo.data, pNo.Direita.data = pNo.Direita.data, pNo.data
        vOldEsquerda = pNo.Esquerda
        pNo.setaFilhos(pNo.Direita, pNo.Direita.Direita)
        pNo.Esquerda.setaFilhos(vOldEsquerda, pNo.Esquerda.Esquerda)

    def RotacaoDireita(self, pNo=No):
        pNo.data, pNo.Esquerda.data = pNo.Esquerda.data, pNo.data
        vOldDireita = pNo.Direita
        pNo.setaFilhos(pNo.Esquerda.Esquerda, pNo.Esquerda)
        pNo.Direita.setaFilhos(pNo.Direita.Direita, vOldDireita)

    def RotacaoEsquerdaDireita(self, pNo=No):
        self.RotacaoEsquerda(pNo.Esquerda)
        self.RotacaoDireita(pNo)

    def RotacaoDireitaEsquerda(self, pNo=No):
        self.RotacaoDireita(pNo.Direita)
        self.RotacaoEsquerda(pNo)

    def PasseioEmOrdem(self, pNo=None): 
        if pNo is None:
            vVisitandoNo    = self.root
            print('Partindo do nó raiz', self.root.data)
            print('Altura: ', self.Altura(vVisitandoNo))
            print('Balanço: ', self.Balanco(vVisitandoNo))
        else:
            vVisitandoNo    = pNo 
            print('Visitando o nó:', pNo.data)
            print('Altura: ', self.Altura(vVisitandoNo))
            print('Balanço: ', self.Balanco(vVisitandoNo))

        if vVisitandoNo.Esquerda: 
            print('Filho da Esquerda:', vVisitandoNo.Esquerda)
        else: 
            print('Não tem Filho da Esquerda!')

        if vVisitandoNo.Direita:
            print('Filho da Direita:', vVisitandoNo.Direita)
        else: 
            print('Não tem Filho da Direita!')

        print()

        if vVisitandoNo.Esquerda: 
            self.PasseioEmOrdem(vVisitandoNo.Esquerda)
            print('Voltando para o nó:', vVisitandoNo, '\n')        
        
        if vVisitandoNo.Direita: 
            self.PasseioEmOrdem(vVisitandoNo.Direita)
            print('Voltando para o nó:', vVisitandoNo, '\n')        

    def inserir(self, pValor):
        vNoPai = None                   
        vNoSendoVisitado = self.root    
        
        while (vNoSendoVisitado):       
            vNoPai = vNoSendoVisitado   
            if pValor < vNoSendoVisitado.data:  
                vNoSendoVisitado = vNoSendoVisitado.Esquerda 
            else:                               
                vNoSendoVisitado = vNoSendoVisitado.Direita 
        
        if vNoPai is None:              
            self.root = No(pValor)

        elif pValor < vNoPai.data:      
            vNoPai.Esquerda = No(pValor)
        else:                           
            vNoPai.Direita = No(pValor)
        
        #Chama o método que balanceia a árvore a cada inserção 
        self.ExecutaBalanco(self.root)
                
oArvore1 = ArvoreBinaria() 

while True:
    vValor = input('Entre com um valor para adicionar na árvore:')
    if vValor == '-':
        break
    else:
        oArvore1.inserir(int(vValor))

oArvore1.PasseioEmOrdem() 