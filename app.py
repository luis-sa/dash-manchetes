import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import data as dt
import dash_bootstrap_components as dbc


df_1 = pd.DataFrame(data = pd.read_excel(r'"C:\Users\luiss\PycharmProjects\dash_manchetes\manchetes.xlsx"',
                     sheet_name='manchetes {0}'.format(dt.data_pesquisa)), columns=['Manchetes', 'Palavra_Chave',
                                                                                    'DataPesquisa', 'Fonte', 'Link_Consulta'])
df_1 = df_1.drop(columns=['Palavra_Chave', 'DataPesquisa'])



def generate_table(dataframe, max_rows = 50):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
                html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
                ])for i in range(min(len(dataframe), max_rows))
            ])
        ])


app = dash.Dash(__name__)

app.layout = html.Div(
    children=[
        html.Div(
            children=[html.H1(
                children='Manchetes do dia', style={'textAlign': 'center', 'fontSize': '200%'}
            )]
        ),
        html.Div(
            generate_table(df_1)
        )
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)