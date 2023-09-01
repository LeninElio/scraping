import asyncio
import csv
import aiohttp
import pandas as pd


async def obtener_datos(usernames):
    """
    Obtener datos
    """
    agente = """Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"""
    headers = {
        'User-Agent': f'{agente}'
    }

    async with aiohttp.ClientSession(headers=headers) as session:
        tasks = []
        for username in usernames:
            url = f'https://www.duolingo.com/2017-06-30/users?username={username}'
            tasks.append(asyncio.ensure_future(obtener_datos_de_usuario(session, url)))

        responses = await asyncio.gather(*tasks)

    return responses


async def obtener_datos_de_usuario(session, url):
    """
    Obtener datos
    """
    async with session.get(url, verify_ssl=True, timeout=10) as response:
        if response.status == 200:
            data = await response.json()
            return data['users']
        return {'message': 'Error al obtener los datos'}


with open('./data/duolingo/duolingo.csv', 'r', encoding='utf-8') as archivo:
    datos = csv.reader(archivo)
    user_names = [dato[1] for dato in datos]


# print(user_names[:4])
# user_names = ['juan', 'maria', 'pepe']

loop = asyncio.get_event_loop()
future = asyncio.ensure_future(obtener_datos(user_names[450:500]))
datos = loop.run_until_complete(future)
print(datos)

respuestas = [dato[0] for dato in datos]
pd.DataFrame(respuestas).to_csv('./data/duolingo/duo_info_5.csv', index=False)
print('Completo...')
