__author__ = 'Italo'

from cih.TelaLogin import TelaLogin


class Controle_Login():

    def __init__(self, janela, controle):
        self.janela_principal = janela
        self.controle_geral = controle

    def carregar_tela(self):
        TelaLogin(self.janela_principal,self)

    def verificar_login(self, login , senha):
        self.controle_geral.carregar_home()



