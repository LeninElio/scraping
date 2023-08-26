import os
import time
import csv
import random
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv


def login(driver, username, password):
    """
    Iniciar sesion.
    """
    print("Logging in...")
    time.sleep(5)
    url = ["https://www.duolingo.com/log-in", "https://es.duolingo.com/log-in"]
    url_pre = random.choice(url)
    response = requests.get(url_pre, timeout=10)
    status_code = response.status_code
    print(f"Status code: {status_code}")
    if status_code == 403:
        time.sleep(10)
        print("Retrying login process...")
        login(driver, username, password)
        return ''

    driver.get(url_pre)
    time.sleep(5)
    username_input = driver.find_elements(By.XPATH, '//input[@class="_3Yh_i" and @type="text"]')
    username_input[0].send_keys(username)
    password_input = driver.find_elements(By.XPATH, '//input[@class="_3Yh_i" and @type="password"]')
    password_input[0].send_keys(password)
    password_input[0].send_keys(Keys.ENTER)
    time.sleep(2)
    print("Logged in successfully")


def is_redirected(driver, url):
    """
    Obtener la redireccion.
    """
    driver.get(url)
    time.sleep(1)
    current_url = driver.current_url
    return current_url if current_url != url else None


def obtener_datos(driver, min_, max_):
    """
    Obtener los datos.
    """
    urls = []
    batch_size = 50
    try:
        for i in range(min_, max_):
            page = f"https://www.duolingo.com/u/{i}"
            current_url = is_redirected(driver, page)
            if current_url:
                usuario_e = current_url.split('/')
                if usuario_e[3] == 'profile':
                    print('Encontrado: ', (i, usuario_e[4]))
                    urls.append((i, usuario_e[4]))

                    if len(urls) % batch_size == 0:
                        with open('duolingo.csv', 'a', newline='', encoding='utf-8') as csvfile:
                            csv_writer = csv.writer(csvfile)
                            for url in urls:
                                csv_writer.writerow(url)
                        urls = []
            else:
                continue

        with open('duolingo.csv', 'a', newline='', encoding='utf-8') as csvfile:
            csv_writer = csv.writer(csvfile)
            for url in urls:
                csv_writer.writerow(url)

        driver.quit()
    except Exception as e:
        print(f"Error al procesar {e}")


n = ['--user-agent=Mozilla/5.0', '(KHTML, like Gecko)']
agente = [
    f'{n[0]} (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 {n[1]} Chrome/114.0.5735.90 Safari/537.36',
    f'{n[0]} (Macintosh; Intel Mac OS X 11_6_0) AppleWebKit/537.36 {n[1]} Chrome/110.0.5481.30 Safari/537.36',
    f'{n[0]} (X11; Arch Linux x86_64) AppleWebKit/537.36 {n[1]} Chrome/111.0.5563.41 Safari/537.36'
]


def main(usuario, contrasena):
    """
    Procesar por rangos.
    """
    rangos = [(x, x + 100) for x in range(45464880, 45470000, 100)]
    for rango in rangos:
        options = Options()
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument(random.choice(agente))
        driver_x = webdriver.Chrome(options=options)
        login(driver_x, usuario, contrasena)
        obtener_datos(driver_x, rango[0], rango[1])
        driver_x.quit()
        print('--- Reiniciando proceso... ---')
        time.sleep(30)


if __name__ == "__main__":
    load_dotenv('private/.env')
    user_ = os.getenv('USUARIO')
    password_ = os.getenv('PASSWORD')
    main(user_, password_)
