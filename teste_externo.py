import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from dash.dependencies import Input, Output
import scrapping_manchetes as manchetes

app = dash.Dash(__name__)

lista_dicionario = [
  {'label':'Globo.com', 'value': 'https://g1.globo.com/},
  {'label': 'Metropoles', 'value': 'https://www.metropoles.com/'},
  {'label': 'Correio Braziliense', 'value': 'https://www.correiobraziliense.com.br/'},
  {'label':'Folha de São Paulo', 'value':'https://www.folha.uol.com.br/'}, 
  {'label':'R7', 'value':'https://www.r7.com/'},
  {'label':'New York Times', 'value':'https://www.nytimes.com/'},
  {'label':'Estadão', 'value':'https://www.estadao.com.br/'},
  {'label':'Washington Post', 'value':'https://www.washingtonpost.com/'}
]

app.layput = html.Div(
  [
    html.Table([
      html.Thead(
        html.Tr('Fontes pesquisadas')
        ),
      html.Tbody([
        html.Td(
        dcc.Checklist(
          options = 
            lista_dicionario
         ),
        
  
  ]
 )
 
