__author__ = 'Italo'

from cih.TelaCadastro import TelaCadastro


class Controle_CadastroImigrante():

    def __init__(self, janela, controle):
        self.janela_principal = janela
        self.controle_geral = controle

    def carregar_tela(self):
        TelaCadastro(self.janela_principal,self)