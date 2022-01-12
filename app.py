import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import data as dt
import scrapping_manchetes as manchetes


def generate_table(dataframe, max_rows = 50):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
                html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
                ])for i in range(min(len(dataframe), max_rows))
            ]),
        ])


app = dash.Dash(__name__)
server = app.server

app.layout = html.Div(
    children=[
        html.Div(
            children=[html.H1(
                children='Manchetes do dia', style={'textAlign': 'center', 'fontSize': '200%', 'font-family': 'calibri'}
            )]
        ),
        html.Div(
            html.H2(generate_table(manchetes.gerar_consulta())
        ), style={'font-family': 'calibri'})
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)