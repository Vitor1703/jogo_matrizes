import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
import networkx as nx
import matplotlib.pyplot as plt
from pymongo import MongoClient

oDB = oClient.get_database('fiep')

def fGravar():
    vNovoRegistro = {
        'IDVertice': edID.get(),
        'Origem': edID.get(),
    } 

def fExcluir():
    pass 

def fPreencherGrid():
    pass 

def fExibeGrafo():
    pass 

oJanela = tk.Tk()
oJanela.title("Cadastro de Grafos")
oJanela.geometry("800x450")

# Começa construir a tela
lfCadastro = tk.LabelFrame(oJanela, text=' Dados cadastrais ')
lfCadastro.place(x=5, y=5, width=790, height=330)

# Labels
lbID = tk.Label(lfCadastro, text='ID Vértice:', anchor="e")
lbOrigem = tk.Label(lfCadastro, text='Origem:', anchor="e")
lbDestino = tk.Label(lfCadastro, text='Destino:', anchor="e")

# Posição Labels
lbID.place(x=5, y=5, width=100, height=30)
lbOrigem.place(x=5, y=40, width=100, height=30)
lbDestino.place(x=5, y=75, width=100, height=30)

# Entrys
edID = tk.Entry(lfCadastro)
edOrigem = tk.Entry(lfCadastro)
edDestino = tk.Entry(lfCadastro)

# Posição Entrys
edID.place(x=110, y=5, width=100, height=30)
edOrigem.place(x=110, y=40, width=100, height=30)
edDestino.place(x=110, y=75, width=100, height=30)

oGrid = ttk.Treeview(lfCadastro, columns=('clID','clOrigem','clDestino'), show='headings')

oGrid.heading('clID', text='ID Vértice')
oGrid.heading('clOrigem', text='Origem')
oGrid.heading('clDestino', text='Destino')

oGrid.column([0], minwidth=20, width=50)
oGrid.column([1], minwidth=20, width=50)
oGrid.column([2], minwidth=20, width=50)

oGrid.place(x=2, y=120, width=760, height=150)

oBarraRolagemVerticalGrid = ttk.Scrollbar(lfCadastro, orient ="vertical", command = oGrid.yview) 
oBarraRolagemVerticalGrid.place(x=763, y=120, height= 150) 

btGravar = tk.Button(lfCadastro, text='Gravar', command=fGravar)
btGravar.place(x= 643, y=275, width=120, height=30)

btGravar = tk.Button(lfCadastro, text='Excluir', command=fExcluir)
btGravar.place(x= 500, y=275, width=120, height=30)

lfExibicao = tk.LabelFrame(oJanela, text=' Opções para exibição ')
lfExibicao.place(x=5, y=340, width=500, height=90)

btGrafo = tk.Button(lfExibicao, text='Exibir Grafo', command=fExibeGrafo)
btGrafo.place(x= 360, y=20, width=120, height=30)

vGrafoDirecionado = tk.IntVar()
ckGrafoDirecionado = tk.Checkbutton(lfExibicao, variable=vGrafoDirecionado, text="Arestas Direcionadas", onvalue=1, offvalue=0, anchor="w")
ckGrafoDirecionado.place(x= 5, y=5, width=350, height=30)

vPosicaoAleatoria = tk.IntVar()
ckPosicaoAleatoria = tk.Checkbutton(lfExibicao, variable=vPosicaoAleatoria, text="Posição Aleatória dos Vértices", onvalue=1, offvalue=0, anchor="w")
ckPosicaoAleatoria.place(x= 5, y=35, width=350, height=30)


fPreencherGrid()

oJanela.mainloop()