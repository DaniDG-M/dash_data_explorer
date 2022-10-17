import utils


def test_get_data():
    api_handler = utils.BMEApiHandler()

    master = api_handler.get_ticker_master('IBEX') # probamos la parte de obtener el maestro
    print(master.ticker)
    print(
        [{'label': tck, 'value': tck} for tck in master.ticker]
    )

    data_close = api_handler.get_ohlc_data_ticker('IBEX', 'SAN')  # probamos la descarga de datos 
    print(data_close)

test_get_data()

