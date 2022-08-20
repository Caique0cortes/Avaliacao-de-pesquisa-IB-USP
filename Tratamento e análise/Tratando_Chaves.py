import pandas as pd
import unidecode
import re 
from iteration_utilities  import duplicates

#Inserir endereço do arquivo

bage_geral = pd.read_excel('Base_Bibliográfica.xlsx')
chaves = pd.read_excel('Palaras-Chave.xlsx')

#LIMPANDO CHAVES NO DATAFRAME 

chaves['Chaves'] = chaves['Chaves'].replace('[]','NaN')
chaves['Chaves'] = chaves.apply(lambda x: (x[1].replace('\'\'','NaN')), axis = 1)
chaves['Chaves'] = chaves.apply(lambda x: (x[1].replace(',','|')), axis = 1)
chaves['Chaves'] = chaves.apply(lambda x: (x[1].replace('[','')), axis = 1)
chaves['Chaves'] = chaves.apply(lambda x: (x[1].replace(']','')), axis = 1)
chaves['Chaves'] = chaves.apply(lambda x: (x[1].replace('\'','')), axis = 1)

#AGRUPANDO CHAVES POR DEPARTAMENTO ->

chaves = chaves.where(chaves['Chaves'] != 'NaN').dropna() 
chaves = chaves.rename(columns= {'Nome': 'Pesquisador'})

Departamentos = bage_geral.iloc[:,[0,2]] #selecionando coluna 0 e 2
Departamentos = Departamentos.drop_duplicates(subset = 'Pesquisador')
chaves = pd.merge(chaves, Departamentos, how = 'inner', on = 'Pesquisador')

Ecologia = chaves.groupby('Departamento').get_group('Ecologia') #agrupando
Fisiologia = chaves.groupby('Departamento').get_group('Fisiologia')
Botanica = chaves.groupby('Departamento').get_group('Botanica')
Zoologia = chaves.groupby('Departamento').get_group('Zoologia')
Genetica = chaves.groupby('Departamento').get_group('Genética')

Ecologia = str(list(pd.Series(Ecologia['Chaves']))) #coletando uma lista de palavras do grupo departamento e formando um texto
Fisiologia = str(list(pd.Series(Fisiologia['Chaves'])))
Botanica = str(list(pd.Series(Botanica['Chaves'])))
Zoologia = str(list(pd.Series(Zoologia['Chaves'])))
Genetica = str(list(pd.Series(Genetica['Chaves'])))


#LIMPANDO CHAVES NO TEXTO DE CHAVES CRIADO 

Genetica = re.sub(r',','|', Genetica)
Genetica = (re.sub(r'\'|\[|\]|NaN\||NaN',"", Genetica )).lower() #operador (| para ou), retirando (NaN| and NaN and [ and ] and ')

Ecologia = re.sub(r',','|', Ecologia)
Ecologia = (re.sub(r'\'|\[|\]|NaN\||NaN',"", Ecologia )).lower() #operador (| para ou), retirando (NaN| and NaN and [ and ] and ')

Fisiologia = re.sub(r',','|', Fisiologia)
Fisiologia = (re.sub(r'\'|\[|\]|NaN\||NaN',"", Fisiologia )).lower() #operador (| para ou), retirando (NaN| and NaN and [ and ] and ')

Botanica = re.sub(r',','|', Botanica)
Botanica = (re.sub(r'\'|\[|\]|NaN\||NaN',"", Botanica )).lower() #operador (| para ou), retirando (NaN| and NaN and [ and ] and ')

Zoologia = re.sub(r',','|', Zoologia)
Zoologia = (re.sub(r'\'|\[|\]|NaN\||NaN',"", Zoologia )).lower() #operador (| para ou), retirando (NaN| and NaN and [ and ] and ') .lower() deixa em caixa baixa

