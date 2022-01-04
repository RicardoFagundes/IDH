'''
Created on 30 de nov. de 2021

@author: Ricardo
'''
from typing import List, Any
import numpy as np
import matplotlib.pyplot as plt
from Municipios import Idh
#from Teste import municipio


def leArquivo(nomeDiretorio):
    arquivo = open(nomeDiretorio, "r")
    tamanho = arquivo.readlines()
    cont = 0
    lista_municipios = []

    dicionario = {}
    while (cont < len(tamanho)):
        if (cont > 9):
            break
        linha = tamanho[cont]
        vetor = linha.split(";")
        municipio = Idh()
        dicionario[vetor[0]] = float(vetor[1])
        cont += 1

        
    arquivo.close()  
    print(dicionario)
    plt.bar(dicionario.keys(),  dicionario.values())
    plt.show()

leArquivo("MuniciposExpectativa.txt")





    
