import requests
from bs4 import BeautifulSoup
import pandas as pd


def scrape_djmag_simple(anio):
    """
    Datos de la lista de DJMag por año.
    """
    url = f'https://djmag.com/top100djs/{anio}'
    datos = requests.get(url, timeout=10)
    soup = BeautifulSoup(datos.text, 'html.parser')

    posiciones = soup.find_all('div', class_='top100dj-name')
    lista = [
        (
        anio, posicion.text.strip(),
        posicion.find('a')['href'].split('/')[-2],
        posicion.find('a')['href'])
        for posicion in posiciones
        ]
    return lista


def scrape_djmag_completo(anio):
    """
    Datos de la lista de DJMag por año.
    """
    url = f'https://djmag.com/top100djs/{anio}'
    datos = requests.get(url, timeout=10)
    soup = BeautifulSoup(datos.text, 'html.parser')

    lista_dj = soup.find_all(
    lambda tag: tag.name == 'div' and tag.get('class')
    and 'top100dj-title-bar' in tag.get('class')[0])

    lista = []
    for dj_data in lista_dj:
        top = dj_data.find('div', class_='top100dj-movement')
        lista.append((anio, dj_data.find('a')['href'].split('/')[-2],
        dj_data.find('a').text.strip(),
        top.text.strip(),
        None if top.i is None
        else ('Baja'
            if top.i.get('class')[-1] == 'djmi-solid-arrow-fat-down'
            else 'Sube'),
        dj_data.find('a')['href']))

    return lista


todos = []
for i in range(2004, 2023):
    print(f'Extrayendo datos del año: {i}')
    por_anio = scrape_djmag_completo(i)
    todos.extend(por_anio)


columnas = ['anio', 'posicion', 'nombre_dj', 'movimiento', 'variacion', 'url']
df = pd.DataFrame(todos, columns=columnas)
df.to_csv('./data/djmag/djmag_completo.csv', index=False)
