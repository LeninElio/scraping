import requests


def obtener_tiempo(latitud, longitud, fecha):
    """
    Obtener datos de la API de Sunrise Sunset
    """
    url = f'https://api.sunrise-sunset.org/json?lat={latitud}&lng={longitud}&date={fecha}'
    datos_api = requests.get(url, timeout=10).json()
    return datos_api


LATITUD = 36.7201600
LONGITUD = -4.4203400
FECHA = '2023-08-14'

datos = obtener_tiempo(LATITUD, LONGITUD, FECHA)
for dato in datos['results'].items():
    print(dato[0].upper(), ':', dato[1])
