__author__ = 'Italo'

from util.Singleton import Singleton
from cci.Controle_CadastroImigrante import Controle_CadastroImigrante
from cci.Controle_Home import Controle_Home
from cci.Controle_Login import Controle_Login




class FactoryFlyWeightControles(Singleton):

    controles = {}
    __instance = None

    def __init__(self,janela,controle):

        self.controles = dict([('Home',Controle_Home(janela,controle)),('Login',Controle_Login(janela,controle)),('Cadastro',Controle_CadastroImigrante(janela,controle))])


    def get_controle(self, controle):
        return self.controles[controle]
