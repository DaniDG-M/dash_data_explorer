import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
import plotly.express as px
import pandas as pd
import utils # importo el fichero con las funciones


app = dash.Dash(__name__)

ah = utils.BMEApiHandler()

# Lo primero que definimos es el LAYOUT. 
app.layout = html.Div( # el tag Div aplica a todo el bloque que tiene debajo. Cambia estilo y formatos. 
    children=[
        html.H1('MIAX Data Explorer'), # el tag H1 es para añadir un Titulo
        html.P('Miax API'), # el tag P es para generar un párrafo
        dcc.Dropdown( # dcc = DASH Core Components. En este caso usamos el dropdown. 
            id='menu-index',
            options=[
                {'label': 'IBEX', 'value': 'IBEX'},
                {'label': 'DAX', 'value': 'DAX'},
                {'label': 'EUROSTOXX', 'value': 'EUROSTOXX'},
            ],
            value='IBEX' # este es el valor predeterminado que vamos a ver al inicio
        ),
        dcc.Dropdown(
            id='menu-ticker', # de momento lo pongo el ID pero las opciones en si las coge luego
        ),
        dcc.Graph( # aqui usamos el graph component de DASH
            id='example-graph', # de moemnto le pongo el ID y el grafico lo hago luego
        )
    ]
)



@app.callback( # primer callback. no tengo que poner siempre lo de "component..."
    Output(component_id='menu-ticker', component_property='options'), # Salen las opciones de "menu-ticker"
    Input(component_id='menu-index', component_property='value') # Entra el valor de "menu-index", primer dropdown
)
def change_ticker_menu_options(market): # funcion para sacar los ticker segun el mercado
    master = ah.get_ticker_master(market=market) # usamos la funcion que está en "utils.py"
    ticker_options = [
        {'label': tck, 'value': tck} # convertimos la SERIE en un diccionario. Tanto la CLAVE como el VALOR serán los tickers.
        for tck in master.ticker # master.ticker es una SERIE con los tickers del mercado
    ]
    return ticker_options # diccionario con los tickers


@app.callback( # Segundo Callback. Recibe como Input el Output del anterior. 
    Output('menu-ticker', 'value'), # sale el TICKER. Por definición el primero de la Serie. Luego se puede seleccionar. 
    Input('menu-ticker', 'options'), # srgundo dropdown
)
def select_tck(ticker_options):
    return ticker_options[0]['value'] # por definición, sacamos el primer TICKER del mercado seleccionado. 


@app.callback( # Tercer CallBack. 
    Output('example-graph', 'figure'), # Nos devuelve el GRAFICO con los datos que le hemos metido
    State('menu-index', 'value'),
    Input('menu-ticker', 'value'), # Entra el TICKER que hayamos seleccionado en el segundo dropdown. 
)
def change_figure(market, tck): # recibe el mercado y el ticker de los apartados anteriores
    data = ah.get_close_data_ticker(market=market, ticker=tck)
    fig = px.line(data) # Gráfico de Plotly.Express. Coge los datos que salen de la funcion para hacer un grafico de linea
    return fig


if __name__ == "__main__":
    app.run_server(host="0.0.0.0", debug=False, port=8080)