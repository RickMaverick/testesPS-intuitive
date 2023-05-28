#!/usr/bin/env python
# coding: utf-8

# Importando Bilbiotecas

# In[1]:


import tabula
import os
import zipfile
import pandas as pd


# Criando Lista com tabelas do AnexoI

# In[2]:


meu_nome = 'Ricardo Temple'
caminho_arquivo_pdf = 'anexos/anexo1.pdf'

lista_tabelas = tabula.read_pdf(caminho_arquivo_pdf, pages='3-180') #lista


# Separando tabelas com problemas das que estão corretas

# In[3]:


lista_tabelas_corretas = []
lista_tabelas_incorretas = []

contador = 0

for tabela in lista_tabelas:
    contador+=1
    if tabela.shape == (19,13):
        tabela = tabela.fillna("") #Removendo Nan
        lista_tabelas_corretas.append(tabela)
    else:
        lista_tabelas_incorretas.append(tabela)


# Concatenando as tabelas que estão corretas

# In[4]:


df_concatenado = pd.DataFrame()
for tabela in lista_tabelas_corretas:
    df_concatenado = pd.concat([df_concatenado, tabela], axis=0)

display(df_concatenado)


# Salvando tabela em arquivo csv

# In[5]:


df_concatenado.to_csv('TabelasAnexoI.csv', index=False)

with zipfile.ZipFile(f'Teste_{meu_nome}.zip', 'w') as zipf:
    zipf.write('TabelasAnexoI.csv')


# Tratando Dados das tabelas com erros

# In[6]:


contador = 0
for tabela in lista_tabelas_incorretas:
    ##TRATAMENTO DO ERRO: Titulo das colunas na linha 1
    if tabela.columns[0] == 'PROCEDIMENTO':
        tabela.columns = tabela.iloc[0]
        tabela = tabela[1:]
    else:
        print(f"TABELA {contador}")
        display(tabela)
        contador+=1

