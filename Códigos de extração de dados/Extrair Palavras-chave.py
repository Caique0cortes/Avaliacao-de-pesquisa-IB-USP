# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 23:16:08 2022

@author: Caique Cortes
"""

import xml.etree.ElementTree as ET
import os
import pandas as pd

path = 'C:\\Users\\Usuario_exemplo\\Nome_da_pasta_onde_estão_os_currículos'
arquivos = os.listdir(path)

Chave_geral =[]

for xml in arquivos:
    Endereço_Curriculo = xml
    endereço = path+'\\'+xml
    
    with open(endereço, "rb") as file:
        tree = ET.parse(file)
        root = tree.getroot()
        
        Nome_completo = root.find('DADOS-GERAIS').get('NOME-COMPLETO')
        publicados = root.findall("PRODUCAO-BIBLIOGRAFICA/ARTIGOS-PUBLICADOS/ARTIGO-PUBLICADO")
        aceitos = root.findall("PRODUCAO-BIBLIOGRAFICA/ARTIGOS-ACEITOS-PARA-PUBLICACAO/ARTIGO-ACEITO-PARA-PUBLICACAO")
        Nome_completo = root.find('DADOS-GERAIS').get('NOME-COMPLETO') #get pega a chave presente em dados gerais
        chaves_autor = []
        Chave_unica_autor =[]
        
        def coletar_dados(lista):  
            chaves = []
            
            for artigo in lista:
                if artigo.find("PALAVRAS-CHAVE") is not None:
                    chave = artigo.find("PALAVRAS-CHAVE").attrib #um dicionario
                    chaves.append(chave) 
                    
            for i in chaves:
                chaves_autor.append(list(i.values())) #coletando em lista os valores do dicionario
        
        coletar_dados(publicados)
        coletar_dados(aceitos)
        
        for i in chaves_autor:
            Chave_unica_autor.extend(i) #coletando uma lista de listas e construindo uma lista única
        
        dic = {'Nome': Nome_completo,
               'Chaves': Chave_unica_autor}
        
        Chave_geral.append(dic)
        
df = pd.DataFrame(Chave_geral)
df.to_excel('Chaves.xlsx')
