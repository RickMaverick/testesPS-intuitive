#!/usr/bin/env python
# coding: utf-8

# Importando Bibliotecas

# In[1]:


import os
import shutil
import requests
from bs4 import BeautifulSoup


# Preparando variáveis para uso do Requests e BeautifulSoup

# In[2]:


url_principal = "https://www.gov.br/ans/pt-br/assuntos/consumidor/o-que-o-seu-plano-de-saude-deve-cobrir-1/o-que-e-o-rol-de-procedimentos-e-evento-em-saude"
cabecalho = {'user-agent': 'Mozzila/5.0'}
site = requests.get(url_principal, headers=cabecalho)
html_site = site.text
html_estruturado = BeautifulSoup(html_site, 'html.parser')


# Criando Função para salvar a URL de cada anexo

# In[3]:


def pega_url_anexos():
    html_anexoI_pdf = html_estruturado.find("a", {"href":"https://www.gov.br/ans/pt-br/assuntos/consumidor/o-que-o-seu-plano-de-saude-deve-cobrir-1/Anexo_I_Rol_2021RN_465.2021_RN473_RN478_RN480_RN513_RN536_RN537_RN538_RN539_RN541_RN542_RN544_546_571_577.pdf"})
    url_anexoI_pdf = html_anexoI_pdf["href"]
    html_anexoI_xml = html_estruturado.find("a", {"href": "https://www.gov.br/ans/pt-br/assuntos/consumidor/o-que-o-seu-plano-de-saude-deve-cobrir-1/Anexo_I_Rol_2021RN_465.2021_RN473_RN478_RN480_RN513_RN536_RN537_RN538_RN539_RN541_RN542_RN544_546_571_577.xlsx"})
    url_anexoI_xml = html_anexoI_xml["href"]
    html_anexoII = html_estruturado.find("a", {"href": "https://www.gov.br/ans/pt-br/assuntos/consumidor/o-que-o-seu-plano-de-saude-deve-cobrir-1/Anexo_II_DUT_2021_RN_465.2021_tea.br_RN473_RN477_RN478_RN480_RN513_RN536_RN537_RN538_RN539_RN540_RN541_RN542_RN544_546_550_553_571v2_575_576_577.pdf"})
    url_anexoII = html_anexoII["href"]
    html_anexoIII = html_estruturado.find("a", {"href": "https://www.gov.br/ans/pt-br/arquivos/assuntos/consumidor/o-que-seu-plano-deve-cobrir/Anexo_III_DC_2021_RN_465.2021.v2.pdf"})
    url_anexoIII = html_anexoIII["href"]
    html_anexoIV = html_estruturado.find("a", {"href":"https://www.gov.br/ans/pt-br/arquivos/assuntos/consumidor/o-que-seu-plano-deve-cobrir/Anexo_IV_PROUT_2021_RN_465.2021.v2.pdf"})
    url_anexoIV = html_anexoIV["href"]

    lista_urls = [url_anexoI_pdf, url_anexoI_xml, url_anexoII, url_anexoIII, url_anexoIV]

    return lista_urls


# Criando Função que cria Diretório, baixa os anexos no diretório e zipa diretório com anexos

# In[4]:


def baixa_arquivos():
    diretorio = "anexos"
    if not os.path.exists(diretorio):
        os.makedirs(diretorio)
    for i in range(5): #Baixando arquivos para diretório anexos
        resposta = requests.get(pega_url_anexos()[i])
        if resposta.status_code == 200:
            if i == 0:
                nome_arquivo = f"anexo{i+1}.pdf"  #Nome do arquivo a ser salvo
                caminho_arquivo = os.path.join(diretorio, nome_arquivo)  #Caminho completo do arquivo dentro do diretório "anexos"
                with open(caminho_arquivo, "wb") as arquivo:
                    arquivo.write(resposta.content)
                print(f"Arquivo {nome_arquivo} baixado e salvo com sucesso.")
            elif i == 1:
                nome_arquivo = f"anexo{i}.xlsx"  #Nome do arquivo a ser salvo
                caminho_arquivo = os.path.join(diretorio, nome_arquivo)  #Caminho completo do arquivo dentro do diretório "anexos"
                with open(caminho_arquivo, "wb") as arquivo:
                    arquivo.write(resposta.content)
                print(f"Arquivo {nome_arquivo} baixado e salvo com sucesso.")
            else:
                nome_arquivo = f"anexo{i}.pdf"  #Nome do arquivo a ser salvo
                caminho_arquivo = os.path.join(diretorio, nome_arquivo)  #Caminho completo do arquivo dentro do diretório "anexos"
                with open(caminho_arquivo, "wb") as arquivo:
                    arquivo.write(resposta.content)
                print(f"Arquivo {nome_arquivo} baixado e salvo com sucesso.")
    shutil.make_archive(diretorio, "zip", diretorio)
    print("Pasta ZIP com anexos, criada com sucesso.")


# In[5]:


baixa_arquivos()


# In[ ]:




