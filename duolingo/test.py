import csv


with open('data/duolingo/output.csv', 'r', encoding='utf-8') as archivo:
    enlace = csv.reader(archivo)
    for usuario in enlace:
        # print(usuario)
        nombre_us = usuario[1].split('/')
        if nombre_us[3] == 'profile':
            print(usuario[0], nombre_us[4])
