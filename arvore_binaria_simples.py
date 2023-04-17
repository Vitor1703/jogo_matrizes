class No:
    def __init__(self, dado):
        self.valor = dado
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.valor)


class ArvoreBinaria:
    def __init__(self, dado = None):
        if dado:
            node = No(dado)
            self.root = node
        else:
            self.root = None

oArvore1 = ArvoreBinaria('Oberdan')
oArvore1.root.left = No('Maria')
oArvore1.root.right = No('José')
oArvore1.root.left.left = No('Pedro')
oArvore1.root.left.right = No('Paulo')
oArvore1.root.right.left = No('Tiago')
oArvore1.root.right.right = No('Bia')
oArvore1.root.left.left.left = No('Joaquim')
oArvore1.root.left.left.right = No('Márcia')
oArvore1.root.right.left.left = No('Silvia')
oArvore1.root.right.right.right = No('Mario')

print(f'                                 {oArvore1.root}\n')
print(f'                  {oArvore1.root.left}                            {oArvore1.root.right}\n')
print(f'        {oArvore1.root.left.left}                {oArvore1.root.left.right}       {oArvore1.root.right.left}              {oArvore1.root.right.right}\n')
print(f'{oArvore1.root.left.left.left}       {oArvore1.root.left.left.right}   {oArvore1.root.right.left.left}       {oArvore1.root.right.right.right}\n')
