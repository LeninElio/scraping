import requests


def obtener_datos(username=None, correo=None):
    """
    Obtener datos del endpoint de Duolingo.
    """
    if username:
        url = f'https://www.duolingo.com/2017-06-30/users?username={username}'
    elif correo:
        url = f'https://www.duolingo.com/2017-06-30/users?mail={correo}'
    else:
        return {'message': 'No se ha especificado un username o correo'}

    agente = """Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36""" # noqa: E501
    headers = {
        'User-Agent': f'{agente}'
    }

    response = requests.get(url, headers=headers, verify=True, timeout=10)

    if response.status_code == 200:
        data = response.json()
        return data['users']
    return {'message': 'Error al obtener los datos'}


datos = obtener_datos(username='username')
print(datos)
