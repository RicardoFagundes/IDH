# -*- coding: latin-1 -*-
'''
Created on 26 de nov. de 2021

@author: Ricardo
'''

from Municipios import Idh


def leArquivo(nome_diretorio):
    arquivo = open(nome_diretorio, "r")
    tamanho = arquivo.readlines()
    cont = 0
    lista_idh = []

    while (cont < len(tamanho)):
        if (cont == 0):
            cont += 1
            continue

        linha = tamanho[cont]
        vetor = linha.split(";")
        municipios = Idh()
        municipios.ano = int(vetor[0])
        municipios.Codigo_Federacao = vetor[1]
        municipios.Nome_Federacao = vetor[2]
        municipios.Codigo_Municipio = vetor[3]
        municipios.Nome_Municipio = vetor[4]
        municipios.Espectativa_Vida_Nascer = float(vetor[5].replace(",", "."))
        municipios.Mortalidade_infantil = float(vetor[6].replace(",", "."))
        cont += 1
        lista_idh.append(municipios)

    arquivo.close()
    return lista_idh


lista_processada = leArquivo("IDH2010.csv")
