from datetime import datetime
from datetime import date
import time

def data_hora_atual():
    data_hoje = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    return data_hoje

data_dia_pesquisa = date.today().strftime('%d - %m - %Y')
data_pesquisa = datetime.now().strftime('%Y-%m-%d')

data_hora = datetime.now().strftime('%Y-%m-%d %H-%M-%S')