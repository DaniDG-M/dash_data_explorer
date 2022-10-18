# dash_data_explorer


Test in local:

''bash
1. Construimos la imagen
docker build -t miax-dash-ddorado .
2. Lo ejecutamos
docker run --env MIAX_API_KEY="" -p 8080:8080 miax-dash-ddorado



''bash
Si hemos hecho el docker-compose ya no tenemos que preocuparnos por lo anterior. Solo: 
1. docker-compose build
2. docker-compose up