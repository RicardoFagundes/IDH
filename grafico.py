'''
Created on 30 de nov. de 2021

@author: Ricardo
'''

import matplotlib.pyplot as plt


def leArquivo(nomeDiretorio):  

 

arquivo = open(nomeDiretorio, "r")   
tamanho = arquivo.readlines()   
cont = 0   
dicionario = {}   
while (cont < len(tamanho)):        
if (cont > 9):            
break       
linha = tamanho[cont]       
vetor = linha.split(";")       
dicionario[vetor[0] + "\n" + vetor[1] + "%"] = float(vetor[1])       
cont += 1   
arquivo.close()               

plt.bar(dicionario.keys(),
        dicionario.values())   
plt.show()
leArquivo("MunicipiosExpectativa.txt")
