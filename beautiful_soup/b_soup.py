import requests
from bs4 import BeautifulSoup


# Verificar la version instalada
# import bs4
# print(bs4.__version__)
# print(requests.__version__)

BASE_URL = 'https://scrapepark.org/spanish/'
pedido_obtenido = requests.get(BASE_URL, timeout=10)

# Verificar el estado de la respuesta
print('Estado del pedido: ', pedido_obtenido.status_code)

html_obtenido = pedido_obtenido.text

# html.parser es el parser por defecto
# https://es.wikipedia.org/wiki/Analizador_sint%C3%A1ctico
soup = BeautifulSoup(html_obtenido, 'html.parser')

# primer_h2 = soup.find('h2')
# print(primer_h2.text)

todos_h2 = soup.find_all('h2')
for h2 in todos_h2:
    print('Con espacio:', h2.text)

# respuesta de texto sin espacios
for h2 in todos_h2:
    print('Sin espacio:', h2.get_text(strip=True))

# Atributos de las etiquetas
divs = soup.find_all('div', class_='heading-container heading-center')
for div in divs:
    print(div.get_text(strip=True))

# Busqueda de imagenes
imagenes = soup.find_all(src = True)
for imagen in imagenes:
    if imagen['src'].endswith('.png'):
        print(imagen['src'])

# Descargar las imagenes
for imagen in imagenes:
    if imagen['src'].endswith('.png'):
        nombre = imagen['src'].split('/')[-1]
        print('Descargando:', nombre)
        with open(f'./data/soup/{nombre}', 'wb') as archivo:
            ruta = f"https://scrapepark.org/{'/'.join(imagen['src'].split('/')[-2:])}"
            ruta_imagen = requests.get(ruta, timeout=10)
            archivo.write(ruta_imagen.content)
