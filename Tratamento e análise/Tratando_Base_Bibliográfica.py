import pandas as pd
import matplotlib.pyplot as plt


#Inserir o endereço correto dos arquivos:
Base_geral = pd.read_excel('Base_Bibliográfica.xlsx')
Datas_pós_doc = pd.read_excel('Datas_de_formação_pós-docs.xlsx')
Datas_Docs = pd.read_excel('Datas_de_formação_Doutorandos.xlsx')
Datas_profs = pd.read_excel('Datas_de_formação_Professores.xlsx')

Unindo_datas = pd.concat([Datas_pós_doc,Datas_Docs])
Unindo_datas = pd.concat([Unindo_datas, Datas_profs])
Base_geral = pd.merge(Base_geral,Unindo_datas, how='left', on='Pesquisador' )

#periodo de publicação na graduação
df_graduandos = Base_geral
df_graduandos = df_graduandos[df_graduandos['Ano de Publicação'] <= df_graduandos['Fim GRADUACAO'] ]
n_public_graduandos = df_graduandos['Nome'].value_counts()

#periodo de publicação no mestrado
df_pesquisadores = Base_geral
df_pesquisadores['Teste para mestrado'] = df_pesquisadores['Ano de Publicação'].ge(df_pesquisadores['Inicio MESTRADO']) & df_pesquisadores['Ano de Publicação'].le(df_pesquisadores['Fim MESTRADO'])
df_pesquisadores = df_pesquisadores.where(df_pesquisadores['Teste para mestrado'] == True).dropna(how ='all')
N_que_publicou= df_pesquisadores['Nome'].value_counts()


#periodo de publicação após o vínculo com o IB
df = Base_geral

df_após_vinculo = df[df['Ano de Publicação'] >= df['Inicio']]
df_após_vinculo['Public. por período após vínculo'] = df_após_vinculo.apply(lambda x: x['Ano de Publicação'] - x['Inicio'], axis = 1)

df_antes_do_vinculo = df[df['Ano de Publicação'] < df['Inicio']]
df_antes_do_vinculo['Public. por período antes do vínculo'] = df_antes_do_vinculo.apply(lambda x: x['Ano de Publicação'] - x['Inicio'], axis = 1)


#Publicados pelos doutorandos durante graduação
Doutorandos = Datas_Docs['Nome'].tolist() #gerando uma lista de quem são os doutorandos
Doutorandos_na_graduacao = df_graduandos[df_graduandos['Nome'].isin(Doutorandos)] #filtrando o dataframe entre aqueles que publicaram na graduação
N_doutorando_que_publicou_na_grad = Doutorandos_na_graduacao['Nome'].value_counts()  #deixando apenas os doutorandos que publicaram na graduação nesse novo dataframe
Média_docs_graduação = N_doutorando_que_publicou_na_grad.sum()/len(Doutorandos) #soma de publicações dividido pelo número de doutorandos

#Publicados pelos Pós-docs durante graduação
Pos_doutorandos = (Datas_pós_doc['Nome'].tolist())
Pós_docs_na_graduacao = df_graduandos[df_graduandos['Nome'].isin(Pos_doutorandos)] #buscando pelos pós-doutorandos no dataframe de publicações na graduação
N_pós_doc_que_publicou_na_grad = Pós_docs_na_graduacao['Nome'].value_counts()  #value_counts conta o número de vezes que determinado nome ocorre na coluna
Média_pos_docs_graduacao = N_pós_doc_que_publicou_na_grad.sum()/len(Pos_doutorandos)

#Publicados pelos professores durante graduação
Professores = (Datas_profs['Nome'].tolist())
Professores_na_graduacao = df_graduandos[df_graduandos['Nome'].isin(Professores)]
N_professor_que_publicou_na_grad = Professores_na_graduacao['Nome'].value_counts()
Média_professor_graduação = N_professor_que_publicou_na_grad.sum()/len(Professores)



#Publicados pelos doutorandos no mestrado
Doutorandos_no_mestrado = df_pesquisadores[df_pesquisadores['Nome'].isin(Doutorandos)]
N_doutorando_que_publicou_no_mest = Doutorandos_no_mestrado['Nome'].value_counts() #teste N_doutorando_que_publicou e veja
Média_docs_mestrad = N_doutorando_que_publicou_no_mest.sum()/len(Doutorandos)    #value_counts está retornando o nome e o número de publicações de dado autor

#Publicados pelos pós-doutorandos no mestrado
pos_doutor_no_mestrado = df_pesquisadores[df_pesquisadores['Nome'].isin(Pos_doutorandos)]
N_pos_doutor_que_publicou_no_mest = pos_doutor_no_mestrado['Nome'].value_counts() 
Média_pos_docs_mestrado = N_pos_doutor_que_publicou_no_mest.sum()/len(Pos_doutorandos)

#Publicados pelos professores no mestrado
professores_no_mestrado = df_pesquisadores[df_pesquisadores['Nome'].isin(Professores)]
N_professor_que_publicou_no_mest = professores_no_mestrado['Nome'].value_counts() 
Média_professores_mestrado = N_professor_que_publicou_no_mest.sum()/len(Professores)



#publicações de doutorandos antes do vínculo
doutorandos_antes = df_antes_do_vinculo[df_antes_do_vinculo['Nome'].isin(Doutorandos)]
publicados_doutorandos_antes = doutorandos_antes['Nome'].value_counts()
resultado_antes_doutorandos = publicados_doutorandos_antes.sum()/len(Doutorandos)

#publicações de pos-docs antes do vínculo
pos_docs_antes = df_antes_do_vinculo[df_antes_do_vinculo['Nome'].isin(Pos_doutorandos)]
publicados_pos_docs_antes = pos_docs_antes['Nome'].value_counts()
resultado_antes_pos_docs = publicados_pos_docs_antes.sum()/len(Pos_doutorandos)

#publicações de professores antes do vínculo
professores_antes = df_antes_do_vinculo[df_antes_do_vinculo['Nome'].isin(Professores)]
publicados_professores_antes = professores_antes['Nome'].value_counts()
resultado_antes_prof = publicados_professores_antes.sum()/len(Professores)


#doutorandos apos vinculo
doutorandos_apos_vinculo = df_após_vinculo[df_após_vinculo['Nome'].isin(Doutorandos)]
média_artigo_docs = doutorandos_apos_vinculo['Nome'].value_counts().sum()/len(Doutorandos)


#pós doutorandos após vinculo
pos_doutorandos_apos_vinculo = df_após_vinculo[df_após_vinculo['Nome'].isin(Pos_doutorandos)]
média_artigo_pos_docs = pos_doutorandos_apos_vinculo['Nome'].value_counts().sum()/len(Pos_doutorandos)

#professores_após_vinculo
professores_apos_vinculo = df_após_vinculo[df_após_vinculo['Nome'].isin(Professores)]
média_artigo_professores = professores_apos_vinculo['Nome'].value_counts().sum()/len(Professores)









#formula usada para calcular o menor período até a publicação do primeiro artigo após vinculo:
média_do_menor_intervalo = []
for i,j in professores_apos_vinculo.groupby('Nome')['Public. por período após vínculo']:
  média_do_menor_intervalo.append(j.min())
sum(média_do_menor_intervalo)/len(média_do_menor_intervalo)


#ENCONTRANDO A FREQUÊNCIA DE PUBLICAÇÃO ANUAL APÓS VINCULO AO IB
#para professores
#posterirmente substuir "professores_apos_vinculo" pelo correspondente aos pós-docs e doutorandos
new_df = pd.DataFrame(doutorandos_apos_vinculo['Nome'].value_counts()).reset_index().rename(columns={'Nome':'Artigos','index':'Nome'})
base_com_vinculo = doutorandos_apos_vinculo[['Inicio','Nome']]
new_df = pd.merge(new_df, base_com_vinculo, how='left', on='Nome')
new_df = new_df.drop_duplicates('Nome')

new_df['Tempo'] = 2022 -new_df['Inicio']
new_df['Frequência publicacao'] = new_df['Artigos']/new_df['Tempo']
new_df['Frequência publicacao'].sum()/new_df.shape[0]











#Criando gráfico boxplot da produção entre homens e mulheres

base_mulheres = pd.DataFrame((Base_geral.groupby('Gênero').get_group('F')).value_counts('Nome').reset_index().rename(columns={0:'Artigos'}))
base_homens = pd.DataFrame((Base_geral.groupby('Gênero').get_group('M')).value_counts('Nome').reset_index().rename(columns={0:'Artigos'}))

box = plt.boxplot([base_mulheres['Artigos'], base_homens['Artigos']], labels=['Mulheres', 'Homens'], patch_artist=True )

colors = ['firebrick', 'springgreen']
 
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

plt.title('Produção de artigos cientificos entre mulheres e homens')
plt.show() 