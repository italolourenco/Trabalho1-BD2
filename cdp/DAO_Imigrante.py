from cdp.DAO import DAO
import psycopg2

__author__ = 'Italo'

class DAO_Imigrante(DAO):

    def __init__(self):

        self.con = self.criar_conexao()

    def criar_conexao(self):
        return psycopg2.connect(host='localhost', user='postgres',password=None,dbname='BDImigration')

    def inserir(self, imigrante):