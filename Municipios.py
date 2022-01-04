'''
Created on 26 de nov. de 2021

@author: Ricardo
'''


class Idh:
    Ano = None
    Codigo_Federacao = None
    Nome_Federacao = None
    Codigo_Municipio = None
    Nome_Municipio = None
    Espectativa_Vida_Nascer = None
    Mortalidade_infantil = None

    def __init__(self):
        self.Ano = 0
        self.Codigo_Federacao = 0
        self.Nome_Federacao = ""
        self.Codigo_Municipio = 0
        self.Nome_Municipio = ""
        self.Espectativa_Vida_Nascer = 0.0
        self.Mortalidade_infantil = 0.0
