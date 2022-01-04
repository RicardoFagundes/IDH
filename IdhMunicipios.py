'''
Created on 30 de nov. de 2021

@author: Ricardo
'''
from typing import List, Any
import matplotlib.pyplot as plt
from Municipios import Idh


def leArquivo(nomeDiretorio):
    arquivo = open(nomeDiretorio, "r", encoding="utf8")
    tamanho = arquivo.readlines()
    cont = 0
    lista_municipios = []

    dicionario = {}
    while (cont < len(tamanho)):
        if (cont == 0):
            cont += 1
            continue
        linha = tamanho[cont]
        vetor = linha.split(";")
        municipio = Idh()
        municipio.ano = int(vetor[0])
        municipio.Codigo_Federacao = vetor[1]
        municipio.Nome_Federacao = vetor[2]
        municipio.Codigo_Municipio = int(vetor[3])
        municipio.Nome_Municipio = vetor[4]
        municipio.Espectativa_Vida_Nascer = float(vetor[5].replace(",", "."))
        municipio.Mortalidade_infantil = float(vetor[6].replace(",", "."))
        dicionario[vetor[0]] = float(vetor[0])
        cont += 1

        lista_municipios.append(municipio)

    arquivo.close()
   

    return lista_municipios


arquivo_entrada = "Dados\IDH2010.csv"
arquivo_saida_vida = "Dados\MuniciposExpectativa.txt"
arquivo_saida_mortalidade = "Dados\MuniciposMortalidade.txt"

lista_processada = leArquivo(arquivo_entrada)
lista_mortalidade = lista_processada
lista_processada.sort(key=lambda idh: idh.Espectativa_Vida_Nascer)
lista_mortalidade.sort(key=lambda idh: idh.Mortalidade_infantil)
arquivo_mortalidade = open(arquivo_saida_mortalidade, "w+")
arquivo_vida = open(arquivo_saida_vida, "w+")


for dados in lista_processada:
    arquivo_mortalidade.write("O Municipio " + dados.Nome_Municipio + " possui indice de Mortalidade Infantil = " + str(
        dados.Mortalidade_infantil) + "% \n")
           

for dados in lista_processada:
    arquivo_vida.write(dados.Nome_Municipio + "; " + str(dados.Espectativa_Vida_Nascer) + "\n")

 


arquivo_vida.close()
arquivo_mortalidade.close()
