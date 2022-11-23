class No: 
    def __init__(self, dado):
        self.dado = dado
        self.esquerda = None
        self.direita = None  
    
    def __str__(self):
        return str(self.dado)

contador = 0

class ArvoreBinaria:
    def __init__(self, dado=None):
        if dado:
            no = No(dado)
            self.raiz = no 
        else:
            self.raiz = None 
            

    def PasseioEmOrdem(self, pNo=None):
        global contador

        contador += 1

        if pNo is None:
            vVisitandoNo = self.raiz
            print('\nPartindo do nó raiz: ', vVisitandoNo.dado)
        else:
            vVisitandoNo = pNo
            print('Visitando o nó: ', vVisitandoNo.dado)

        if vVisitandoNo.esquerda:
            print('Filho da Esquerda:', vVisitandoNo.esquerda)
            print('Filho da Direita:', vVisitandoNo.direita)
            print()
            self.PasseioEmOrdem(vVisitandoNo.esquerda)
            print('Voltando para o nó:', vVisitandoNo)
            print(contador, vVisitandoNo.dado)
        else: 
            print('Não tem Filho da Esquerda!')

        if vVisitandoNo.direita:
            self.PasseioEmOrdem(vVisitandoNo.direita)
            print('Voltando para o nó:', vVisitandoNo)
        else:
            print('Não tem Filho da Direita!')
            print()
            print(contador, vVisitandoNo.dado)

    def PasseioPreOrdem(self, pNo=None): 
        if pNo is None:
            vVisitandoNo = self.raiz
        else:
            vVisitandoNo = pNo      
            
        print('EXIBINDO VALOR DO NÓ:', (vVisitandoNo)) 

        if vVisitandoNo.esquerda:
            self.PasseioPreOrdem(vVisitandoNo.esquerda)

        if vVisitandoNo.direita: 
            self.PasseioPreOrdem(vVisitandoNo.direita)
    
    def PasseioPosOrdem(self, pNo=None): 
        if pNo is None:
            vVisitandoNo = self.raiz
        else:
            vVisitandoNo = pNo      
            
        if vVisitandoNo.esquerda: 
            self.PasseioPosOrdem(vVisitandoNo.esquerda)

        if vVisitandoNo.direita: 
            self.PasseioPosOrdem(vVisitandoNo.direita) 

        print('EXIBINDO VALOR DO NÓ:', (vVisitandoNo))

    def PasseioEmNivel(self, pNo=None):
        if pNo is None:
            vVisitandoNo = self.raiz
        else:
            vVisitandoNo = pNo

        print('EXIBINDO VALOR DO NÓ:', (vVisitandoNo))

        if vVisitandoNo.esquerda:
            print('EXIBINDO VALOR DO NÓ:', (vVisitandoNo.esquerda))
            self.PasseioEmNivel(vVisitandoNo)
        else:
            print('EXIBINDO VALOR DO NÓ:', vVisitandoNo.direita)

    def PasseioDescrito():
        return None

    def Insere(self, raiz, pNo=None):
        if raiz is None:
            raiz = pNo

        elif raiz.dado < pNo.dado:
            if raiz.direita is None:
                raiz.direita = pNo
            else:
                self.Insere(raiz.direita, pNo)

        else:
            if raiz.esquerda is None:
                raiz.esquerda = pNo
            else:
                self.Insere(raiz.esquerda, pNo)

    def Busca():
        return None

A1 = ArvoreBinaria('Oberdan')

A1.raiz.esquerda = No('Maria') 
A1.raiz.esquerda.esquerda = No('Pedro') 
A1.raiz.esquerda.esquerda.esquerda = No('Joaquim') 
A1.raiz.esquerda.esquerda.direita = No('Márcia') 

A1.raiz.esquerda.direita = No('Paulo') 
A1.raiz.esquerda.direita.esquerda = No('Silvia') 
A1.raiz.esquerda.direita.direita = No('Mário')

A1.raiz.direita = No('José')
A1.raiz.direita.esquerda = No('Tiago')
A1.raiz.direita.direita = No('Bia')

A1.PasseioEmOrdem()

