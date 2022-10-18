import utils # importo el fichero con las funciones


def test_get_data():
    api_handler = utils.BMEApiHandler() # invoco la clase BMEApiHandler del fichero utils

    master = api_handler.get_ticker_master('IBEX') # probamos la parte de obtener el maestro, con "IBEX" en este caso
    print(master.ticker)
    print(
        [{'label': tck, 'value': tck} for tck in master.ticker]
    )

    # data_close = api_handler.get_ohlc_data_ticker('IBEX', 'SAN')  # probamos la descarga de datos, con "IBEX" y "SAN" 
    # print(data_close)

test_get_data()

