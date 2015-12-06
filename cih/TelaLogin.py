__author__ = 'Italo'
from tkinter import *


class TelaLogin():

    def __init__(self, janela_principal, controle):

        self.login = StringVar()
        self.senha = StringVar()

        janela_principal.title("Login")
        janela_principal.geometry("250x250")

        frameG = Frame(janela_principal)
        frameG.place(x=0,y=0,relwidth=1,relheight=1)

        frameTOP = Frame(frameG)
        frameTOP.pack(side = TOP)

        frameMeio = Frame(frameG)
        frameMeio.pack(padx=10, pady=50)

        frameFim = Frame(frameG)
        frameFim.pack(side=BOTTOM)

        frameN1 = Frame(frameMeio)
        frameN1.pack(side = BOTTOM)

        textNacao1 = Label(frameN1, text='LOGIN:')
        textNacao1.pack(side = LEFT)

        campNacao1 = Entry(frameN1, textvar = self.login)
        campNacao1.pack()

        frameN2 = Frame(frameG)
        frameN2.pack()

        textNacao2 = Label(frameN2, text='Senha: ')
        textNacao2.pack(side = LEFT)

        campNacao2 = Entry(frameN2,textvar = self.senha)
        campNacao2.pack()

        frameB = Frame(frameG)
        frameB.pack(side = BOTTOM)

        botaoEnviar = Button(frameB, text = 'ENTRAR', height='0', width='10', command = lambda : controle.verificar_login(self.login, self.senha))
        botaoEnviar.pack(side = LEFT)

        frameG.mainloop()


