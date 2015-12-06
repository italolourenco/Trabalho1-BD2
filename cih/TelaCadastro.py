__author__ = 'Italo'
from tkinter import *
from tkinter import ttk

class TelaCadastro():

    def __init__(self, janela_principal, controle):

        self.nome = self.n_documento = self.pais_origem = self.nivel_escolar = self.ultimo_emp = self.religiao = self.grupo_religioso = StringVar()

        janela_principal.title("Cadastro")
        janela_principal.geometry("500x500")
        janela_principal.resizable(0,0)

        frameP = Frame(janela_principal)
        frameP.place(x=0,y=0,relwidth=1,relheight=1)

        titulo = Label(frameP, text ="CRUD - Imigrante")
        separador1 = Frame(height = 2, bd = 1, relief =SUNKEN)
        separador2 = Frame(frameP,height = 2, bd = 1, relief =SUNKEN)

        l_nome = Label(frameP, text = 'Nome :')
        l_documento = Label(frameP, text = "N Documento :")
        l_escolaridade = Label(frameP, text = "Nivel Escolar :")
        l_ultimoEmprego = Label(frameP, text = "Ultimo Emprego :")
        l_paisOrigem = Label(frameP, text = "Pais Origem :")
        l_religiao = Label(frameP, text = "Religiao :")
        l_religiaoGrupo = Label(frameP, text = "Grupo Religioso :")

        txt_nome = Entry(frameP,width=20)
        txt_documento = Entry(frameP,width=20)
        txt_escolaridade = Entry(frameP,width=20)
        txt_ultimoEmprego = Entry(frameP,width=20)
        botao_pais = ttk.Combobox(frameP)
        botao_religiao = ttk.Combobox(frameP)
        botao_religaoGrupo = ttk.Combobox(frameP)


        #Area Pesquisa

        l_pesquisa = Label(frameP, text = "Pesquisa :")
        txt_pesquisa = Entry(frameP)
        botao_pesquisa = Button(frameP, text = "Procurar")

        #Painel Acoes

        painel_butoes = Frame(frameP)
        botao_novo = Button(painel_butoes, text = "Novo")
        botao_inserir = Button(painel_butoes, text = "Inserir")
        botao_alterar = Button(painel_butoes, text = "Alterar")
        botao_apagar = Button(painel_butoes, text = "Apagar")

        titulo.grid(row=0,sticky=W+E+N+S,pady=20)

        l_pesquisa.grid(row=2, column=0, pady=20)
        txt_pesquisa.grid(row=2, column=1, pady=20)
        botao_pesquisa.grid(row=2, column=2, padx=10, pady=20)

        l_nome.grid(row=3, sticky=W, padx=20)
        txt_nome.grid(row=3, column=1, pady=5, sticky=W)
        l_documento.grid(row=4, sticky=W, padx=20)
        txt_documento.grid(row=4, column=1, pady=5, sticky=W)
        l_escolaridade.grid(row=5, sticky=W, padx=20)
        txt_escolaridade.grid(row=5, column=1, pady=5, sticky=W)
        l_ultimoEmprego.grid(row=6, sticky=W, padx=20)
        txt_ultimoEmprego.grid(row=6, column=1, pady=5, sticky=W)
        l_paisOrigem.grid(row=7,sticky=W, padx=20)
        botao_pais.grid(row=7, column=1, pady=5, sticky=W)
        l_religiao.grid(row=8,sticky=W, padx=20)
        botao_religiao.grid(row=8, column=1, pady=5, sticky=W)
        l_religiaoGrupo.grid(row=9,sticky=W, padx=20)
        botao_religaoGrupo.grid(row=9, column=1, pady=5, sticky=W)


        botao_novo.grid(row=1, column=0, pady=10, padx=5)
        botao_inserir.grid(row=1, column=1, pady=10, padx=5)
        botao_alterar.grid(row=1, column=2, pady=10, padx=5)
        botao_apagar.grid(row=1, column=3, pady=10, padx=5)
        separador2.grid(row=10, sticky=W+E, columnspan=3, pady=10)
        painel_butoes.grid(row=12, sticky=W+E+S, column=2, columnspan=1)

        frameP.mainloop()


