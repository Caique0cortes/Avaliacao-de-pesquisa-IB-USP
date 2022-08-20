"""
@author: Caique Santos Cortes
"""
import xml.etree.ElementTree as ET
import os
import pandas as pd


#Inserir "path"  o diretório onde estão os currículos .XML (a pasta deve ser o nome do departamento) 
path = 'C:\\Users\\User_exemplo\\Departamento'
arquivos = os.listdir(path) #lista todos os arquivos presentes no indereço indicado para path


Dicionarios_final = []
for xml in arquivos:
    Endereço_Curriculo = xml
    endereço = path+'\\'+xml
    
    with open(endereço, "rb") as file:
        tree = ET.parse(file)
        root = tree.getroot()
        Dicionarios = []
        publicados = root.findall("PRODUCAO-BIBLIOGRAFICA/ARTIGOS-PUBLICADOS/ARTIGO-PUBLICADO")
        aceitos = root.findall("PRODUCAO-BIBLIOGRAFICA/ARTIGOS-ACEITOS-PARA-PUBLICACAO/ARTIGO-ACEITO-PARA-PUBLICACAO")
        
        Nome_completo = root.find('DADOS-GERAIS').get('NOME-COMPLETO') 
        Nome_Citação = ((root.find('DADOS-GERAIS').get('NOME-EM-CITACOES-BIBLIOGRAFICAS')).split(';'))[0]
        
        def coletar_dados(lista):  
            for item in lista:
                
                autores = item.findall("AUTORES")
                autors = []
                for autor in autores:
                    x = autor.get('NOME-PARA-CITACAO')
                    autors.append(x)
                    
                    # Inserir o nome do departamento 
                dic = {"Pesquisador": Nome_completo,
                       "Nome de Citação": Nome_Citação,
                       "Departamento": "Nome_do_Departamento",
                       "Titulo do artigo": item.find("DADOS-BASICOS-DO-ARTIGO").attrib["TITULO-DO-ARTIGO"],
                       "Ano de Publicação": item.find("DADOS-BASICOS-DO-ARTIGO").attrib["ANO-DO-ARTIGO"],
                       "País de publicação": item.find("DADOS-BASICOS-DO-ARTIGO").attrib["PAIS-DE-PUBLICACAO"],
                       "DOI": item.find("DADOS-BASICOS-DO-ARTIGO").attrib["DOI"],
                       "Titulo do periódico/revista": item.find("DETALHAMENTO-DO-ARTIGO").attrib["TITULO-DO-PERIODICO-OU-REVISTA"],
                       "ISSN": item.find("DETALHAMENTO-DO-ARTIGO").attrib["ISSN"],
                       "Volume": item.find("DETALHAMENTO-DO-ARTIGO").attrib["VOLUME"],
                       "Fascículo": item.find("DETALHAMENTO-DO-ARTIGO").attrib["FASCICULO"],
                       "Série": item.find("DETALHAMENTO-DO-ARTIGO").attrib["SERIE"],
                       "Página inicial": item.find("DETALHAMENTO-DO-ARTIGO").attrib["PAGINA-INICIAL"],
                       "Página final": item.find("DETALHAMENTO-DO-ARTIGO").attrib["PAGINA-FINAL"],
                       "Local de publicação": item.find("DETALHAMENTO-DO-ARTIGO").attrib["LOCAL-DE-PUBLICACAO"],
                       "Autores": (' ;'.join(autors))
                       }
    
    
                
                Dicionarios.append(dic)
                
        coletar_dados(publicados)
        coletar_dados(aceitos)
        
        Dicionarios_final.append(Dicionarios)



#SALVE CADA DEPARTAMENTO UM POR VEZ

# Botânica = Dicionarios_final
# Ecologia = Dicionarios_final
# Fisiologia = Dicionarios_final
# Genética = Dicionarios_final
# Zoologia = Dicionarios_final


df = pd.DataFrame([item for sublista in Dicionarios_final for item in sublista])

# Para salvar em um arquivo excel descomente a próxima linha:
#df.to_excel('Nome_do_arquivo.xlsx')
