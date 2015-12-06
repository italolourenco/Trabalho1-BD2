__author__ = 'Italo'

from util.FactoryFlyWeightControles import FactoryFlyWeightControles

from tkinter import *
import tkMessageBox

class Controle_Geral():

    def criar_tela(self):
        self.janela_principal = Tk()

    def iniciar_prog(self):
        self.criar_tela()
        self.carregar_controles()
        self.carregar_login()

    def carregar_controles(self):
        self.controle_factory = FactoryFlyWeightControles(self.janela_principal,self)

    def carregar_login(self):
        ctrl_login = self.controle_factory.get_controle("Login")
        ctrl_login.carregar_tela()

    def carregar_home(self):
        ctrl_home = self.controle_factory.get_controle("Home")
        ctrl_home.carregar_tela()

    def carregar_cadastro(self):
        ctrl_cadastro = self.controle_factory.get_controle("Cadastro")
        ctrl_cadastro.carregar_tela()
