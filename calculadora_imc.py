import tkinter as tk
from tkinter import ttk
from turtle import width


oJanela = tk.Tk()
oJanela.title("APS - Cadastro de pessoa")
oJanela.geometry('400x600')
oJanela.configure(bg='black')
listPessoas = []
pessoa = {}

# Essa função mostra a situação do IMC da pessoa cadastrada
def fSituacaoImc(imc):
    if imc < 17:
        situacao = "Muito abaixo do peso"
        lSituacaoCad['bg'] = '#FFFF66' 
        lSituacaoCad['fg'] = 'black'
    elif imc >= 17 and imc <= 18.49:
        situacao = "Abaixo do peso"
        lSituacaoCad['bg'] = '#FF9933'
        lSituacaoCad['fg'] = 'black'
    elif imc >= 18.5 and imc <= 24.99:
        situacao = "Peso normal"
        lSituacaoCad['bg'] = '#00FF00'
    elif imc >= 25 and imc <= 29.99:
        situacao = "Acima do peso"
        lSituacaoCad['bg'] = '#0080FF'
    elif imc >= 30 and imc <= 34.99:
        situacao = "Obesidade I"
        lSituacaoCad['bg'] = '#FF0000'
    elif imc >= 35 and imc <= 39.99:
        situacao = "Obesidade II (Severa)"
        lSituacaoCad['bg'] = '#990000'
    else:
        situacao = "Obesidade III (Mórbida)"
        lSituacaoCad['bg'] = '#660033'

    return situacao

# Essa função insere dados, calcula o IMC e faz a validação dos dados inseridos
def fInserirDados():
    nome = str(eNome.get())
    genero = str(eGenero.get())
    idade = int(eIdade.get())
    peso = float(ePeso.get())
    altura = float(eAltura.get())

    imc = peso / altura**2

    pessoa['Nome'] = nome
    pessoa['Genero'] = genero
    pessoa['Idade'] = idade
    pessoa['Peso'] = peso
    pessoa['Altura'] = altura
    pessoa['IMC'] = imc
    pessoa['Situacao'] = fSituacaoImc(imc)

    listPessoas.append(pessoa.copy())
    lMensagem['text'] = "Cadastro realizado com sucesso!"
    lMensagem['bg'] = 'green'
    fMostrarDadoCadastrado(nome, genero, idade, peso, altura, imc)
    print(listPessoas)

# Essa função pega os dados cadastrados e adicona nas variáveis
def fMostrarDadoCadastrado(nome, genero, idade, peso, altura, imc):
    lNomeCad['text'] = nome
    lGeneroCad['text'] = genero
    lIdadeCad['text'] = idade
    lPesoCad['text'] = peso
    lAlturaCad['text'] = altura
    lImcCad['text'] = "IMC: {:.2f}".format(imc)
    lSituacaoCad['text'] = fSituacaoImc(imc)

# Labels
lNome = tk.Label(oJanela, text='Nome:', anchor="w", bg= "#00CED1", fg="white", font="normal 12 bold")
lGenero = tk.Label(oJanela, text='Gênero:', anchor="w", bg= "#00CED1", fg="white", font="normal 12 bold")
lIdade = tk.Label(oJanela, text='Idade:', anchor="w", bg= "#00CED1", fg="white", font="normal 12 bold")
lPeso = tk.Label(oJanela, text='Peso:', anchor="w", bg= "#00CED1", fg="white", font="normal 12 bold")
lAltura = tk.Label(oJanela, text='Altura:', anchor="w", bg= "#00CED1", fg="white", font="normal 12 bold")
lMensagem = tk.Label(oJanela, text='Preencha os campos', bd=1, relief=tk.SUNKEN, bg= "#00CED1", fg="white", height=2, font="normal 12 bold")
lLabel = tk.Label(oJanela, text='Dados cadastrados:', anchor="w", fg="white", bg='black', font="normal 12 bold")

# Labels dados inseridos
lNomeCad = tk.Label(oJanela, text='', anchor="w", font="normal 15 bold")
lGeneroCad = tk.Label(oJanela, text='', anchor="w", font="normal 15 bold")
lIdadeCad = tk.Label(oJanela, text='', anchor="w", font="normal 15 bold")
lPesoCad = tk.Label(oJanela, text='', anchor="w", font="normal 15 bold")
lAlturaCad = tk.Label(oJanela, text='', anchor="w", font="normal 15 bold")
lImcCad = tk.Label(oJanela, text='', anchor="w", font="normal 15 bold")
lSituacaoCad = tk.Label(oJanela, text='', anchor="w", fg="white", font="normal 15 bold")

# Entrys
eNome = tk.Entry(oJanela, bg="#FFFFFF", font="normal 12 bold")
eGenero = ttk.Combobox(oJanela, values=["Masculino", "Feminino", "Outros"], font="normal 12 bold")
eIdade = tk.Entry(oJanela, bg="#FFFFFF", font="normal 12 bold")
ePeso = tk.Entry(oJanela, bg="#FFFFFF", font="normal 12 bold")
eAltura = tk.Entry(oJanela, bg="#FFFFFF", font="normal 12 bold")

# Buttons
bInserir = tk.Button(oJanela, text='Inserir', bg="#008080", fg="white", font="normal 15 bold", borderwidth = 0, command=fInserirDados)

# Place labels
lNome.place(x=10, y=5, width=65, height=30)
lGenero.place(x=10, y=40, width=65, height=30)
lIdade.place(x=10, y=75, width=65, height=30)
lPeso.place(x=10, y=110, width=65, height=30)
lAltura.place(x=10, y=145, width=65, height=30)
lMensagem.pack(side=tk.BOTTOM, fill=tk.X)
lLabel.place(x=10, y=240, width=170, height=30)

# Place labels dados inseridos
lNomeCad.place(x=10, y=270, width=155, height=30)
lGeneroCad.place(x=10, y=305, width=155, height=30)
lIdadeCad.place(x=10, y=340, width=155, height=30)
lPesoCad.place(x=10, y=375, width=155, height=30)
lAlturaCad.place(x=10, y=410, width=155, height=30)
lImcCad.place(x=10, y=445, width=155, height=30)
lSituacaoCad.place(x=10, y=480, width=250, height=30)

# Place entrys
eNome.place(x=80, y=5, width=200, height=30)
eGenero.place(x=80, y=40, width=100, height=30)
eIdade.place(x=80, y=75, width=100, height=30)
ePeso.place(x=80, y=110, width=100, height=30)
eAltura.place(x=80, y=145, width=100, height=30)

# Place buttons
bInserir.place(x=80, y=190, width=100, height=30)
print(listPessoas)

oJanela.mainloop()