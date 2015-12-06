__author__ = 'Italo'
from tkinter import *

class TelaHome():

    def __init__(self, janela_principal, controle):

        janela_principal.title("Home")
        janela_principal.geometry("550x550")
        janela_principal.resizable(0,0)

        frameP = Frame(janela_principal)
        frameP.place(x=0,y=0,relwidth=1,relheight=1)

        Frame(janela_principal,width=0,height=200).grid(row=0,column=0, rowspan = 2)
        Button(janela_principal, width=18, height=3, text = 'Cadastrar', command = lambda : controle.ir_telaCadastro()   ).grid(row = 1, column=2)
        Button(janela_principal, width=18, height=3,text = 'Procurar').grid(row = 1, column=3)
        Button(janela_principal, width=18, height=3,text = 'Area').grid(row = 1, column=4)
        Button(janela_principal, width=20, height=3,text = 'Estatisticas').grid(row = 1, column=5)

        frameP.mainloop()
