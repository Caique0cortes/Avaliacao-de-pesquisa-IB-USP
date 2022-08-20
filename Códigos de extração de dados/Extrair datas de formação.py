# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 18:13:31 2022

@author: caique cortes
"""

import xml.etree.ElementTree as ET
import os
import pandas as pd

path = 'C:\\Users\\Usuario_exemplo\\Nome_da_pasta_onde_estão_os_currículos'
arquivos = os.listdir(path)
Dicionarios = []

for xml in arquivos:
    Endereço_Curriculo = xml
    endereço = path+'\\'+xml
    
    with open(endereço, "rb") as file:
        tree = ET.parse(file)
        root = tree.getroot()
        
        Nome_completo = root.find('DADOS-GERAIS').get('NOME-COMPLETO')
        
        Graus = ['GRADUACAO','MESTRADO','DOUTORADO','POS-DOUTORADO']
        dic = {'Nome': Nome_completo}
        
        for i in Graus:
            if root.find('DADOS-GERAIS/FORMACAO-ACADEMICA-TITULACAO/%s' %(i)) is not None:
                Data_inicio = root.find('DADOS-GERAIS/FORMACAO-ACADEMICA-TITULACAO/%s' %(i)).get('ANO-DE-INICIO')
                Data_Fim = root.find('DADOS-GERAIS/FORMACAO-ACADEMICA-TITULACAO/%s' %(i)).get('ANO-DE-CONCLUSAO')
                temporary_dic = {'Inicio %s'%(i): Data_inicio,
                                 'Fim %s'%(i): Data_Fim}
                
                dic.update(temporary_dic)
        
        Dicionarios.append(dic)

df= pd.DataFrame(Dicionarios)

df.to_excel('Nome_do_arquivo.xlsx')