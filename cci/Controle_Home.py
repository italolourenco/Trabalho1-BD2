__author__ = 'Italo'

from cih.TelaHome import TelaHome

class Controle_Home():

    def __init__(self, janela, controle):
        self.janela_principal = janela
        self.controle_geral = controle

    def carregar_tela(self):
        TelaHome(self.janela_principal, self)

    def ir_telaCadastro(self):
        self.controle_geral.carregar_cadastro()



