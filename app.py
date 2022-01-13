import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import data as dt
import scrapping_manchetes as manchetes
import plotly.express as px
import dash_bootstrap_components as dbc


def generate_table(dataframe, max_rows = 50):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns],
                    style={'border': '1px solid',
                           'font-family': 'calibri'})
        ),
        html.Tbody([
                html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
                ])for i in range(min(len(dataframe), max_rows))
            ], style = {'border': '1px solid', 'font-family': 'calibri'}),
        ])


def generate_pie(dataframe, id, names, values):
    return html.Div(children=[
        dcc.Graph(id=id, figure=px.pie(dataframe, names = names, values = values),
                  style={'display':'inline-block'})
    ])


app = dash.Dash(__name__)
server = app.server
app.config.external_stylesheets = [dbc.themes.MINTY]

df_manchetes = manchetes.gerar_consulta()
grupo = pd.DataFrame(df_manchetes.groupby('Fonte').count()).reset_index()
df_manchetes = df_manchetes.drop(columns=['Fonte', 'DataPesquisa'])



app.layout = html.Div(
    children=[
        html.Div(
            children=[html.H1(
                children='Manchetes do dia',
                style={'textAlign': 'center', 'font-family': 'calibri'}
            )]
        ),
        html.Div([
            html.Plaintext(children=' Pesquisa nos principais portais de notícias '
                                    'dos principais pré-candidatos à Presidência da República: '
                                    '{0}'.format(manchetes.termos_pesquisa), style={'font-family': 'calibri'})
        ]),
        html.Div([
            html.Plaintext(
                children= 'Portais pesquisados {0}'.format(manchetes.sites_pesquisa),
                style={'font-family': 'calibri', 'padding': 10, 'font-size': '100%'}
            )
        ]),
        html.Div([
            html.Table([
                html.Tbody([
                    html.Tr([generate_pie(grupo, 'pie_fontes', 'Fonte', 'Manchetes'), generate_table(df_manchetes)]),
                    ], style={'padding': 10, 'textAlign': 'center'})
                ])
            ])
        ])


if __name__ == '__main__':
    app.run_server(debug=True)