import pandas as pd
import requests
from bs4 import BeautifulSoup

import data

pd.set_option('display.max_colwidth', 1000)


sites_pesquisa = ['https://g1.globo.com/', 'https://www.metropoles.com/', 'https://www.correiobraziliense.com.br/',
                  'https://www.folha.uol.com.br/', 'https://www.r7.com/',
                  'https://www.nytimes.com/', 'https://brasil.elpais.com/', 'https://www.estadao.com.br/',
                  'https://www.washingtonpost.com/']

termos_pesquisa = ['Bolsonaro', 'Doria', 'Moro', 'Ciro']


def pesquisa_sites(url):

    palavras_consulta = termos_pesquisa
    resultado_consultas = []

    html = requests.get(url).content
    soup = BeautifulSoup(html, 'html.parser')
    manchetes = soup.find_all(href=True)

    for manchete in manchetes:
        if manchete.has_attr('href'):
            link = manchete['href']
            resultado_consultas.append([manchete.text, link])


    df_3 = pd.DataFrame([], columns=["Manchetes", "Palavra_Chave", "DataPesquisa", "Fonte"])

    def pesquisa_palavras(palavra):

        df_1 = pd.DataFrame(resultado_consultas, columns=['Manchetes', 'Links'])
        df_1["Pesquisa"] = df_1["Manchetes"].str.find(palavra)
        pesquisa = df_1["Manchetes"].where(df_1["Pesquisa"] > 0)
        pesquisa = pesquisa.dropna()
        pesquisa = pesquisa.str.strip()
        pesquisa = pesquisa.to_frame()
        pesquisa = pesquisa.assign(Palavra_Chave=palavra, DataPesquisa=data.data_hora_atual(), Fonte=url)
        pesquisa = pesquisa.assign(Link_Consulta=df_1["Links"].where(df_1["Pesquisa"] > 0))

        df_2 = pd.DataFrame(data=pesquisa)

        return df_2

    for palavra in palavras_consulta:
        resultado = pesquisa_palavras(palavra)

        df_3 = pd.concat([df_3, resultado])
        df_3 = df_3.replace('\n', '', regex=True)
        df_3 = df_3.replace("  ", "")


    return df_3


def gerar_consulta():

    df_pesquisa = pd.DataFrame([], columns=["Manchetes", "Palavra_Chave", "DataPesquisa", "Fonte"])

    for url in sites_pesquisa:
        df_pesquisa = pd.concat([df_pesquisa, pesquisa_sites(url)], ignore_index=True)

    df_pesquisa = df_pesquisa.dropna()

    return df_pesquisa