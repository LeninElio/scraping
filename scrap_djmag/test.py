import requests
from bs4 import BeautifulSoup


URL = 'https://djmag.com/top100djs/2008'
datos = requests.get(URL, timeout=10)
soup = BeautifulSoup(datos.text, 'html.parser')

lista_dj = soup.find_all(
    lambda tag: tag.name == 'div' and tag.get('class')
    and 'top100dj-title-bar' in tag.get('class')[0])

for dj in lista_dj:
    top = dj.find('div', class_='top100dj-movement')
    print(
    (dj.find('a')['href'].split('/')[-2],
    dj.find('a').text.strip(),
    top.text.strip(),
    None if top.i is None
    else ('Baja'
          if top.i.get('class')[-1] == 'djmi-solid-arrow-fat-down'
          else 'Sube'), dj.find('a')['href'])
    )
