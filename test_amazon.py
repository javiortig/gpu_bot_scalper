import requests
from bs4 import BeautifulSoup
import cloudscraper
import re

from time import sleep

from playsound import playsound

link = "https://www.amazon.es/s?k=6800+xt&__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss_2"
SLEEP_DELAY = 5

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print(bcolors.OKBLUE)

print("Vamos a testear que funcione bien el bot para AMAZON con la 6800 xt")
print("")
sleep(SLEEP_DELAY)

scraper = cloudscraper.create_scraper()
html = scraper.get(
    link).content
soup = BeautifulSoup(html, 'html.parser')
soup = soup.findAll(
    "span", class_="a-size-base-plus a-color-base a-text-normal")
if(not soup):
    print(bcolors.FAIL + "Hay un error con el link de AMAZON. Cámbialo" + bcolors.ENDC)
    exit()

print("Hemos pasado los filtros de la web")
print("Ahora debería aparecerte uno o varios matches de que se ha encontrado la 6800 xt:")
print("")
sleep(SLEEP_DELAY)

flag = False
for span in soup:
    result = str(span)
    result = re.search("6800\s*xt", result, re.IGNORECASE)
    if(not result):
        continue
    else:
        flag = True
        print("He encontrado match con: \'" + result[0] + "\'")

sleep(SLEEP_DELAY)

if (flag == True):
    print("")
    print("El bot ha podido encontrar resultados")
    sleep(SLEEP_DELAY * 0.8)
    print("Por último, vamos a comprobar que te funcione el sonido de la alerta:")
    print("")
    sleep(SLEEP_DELAY * 0.8)

    print("Ahora mismo deberías estar escuchando algo...")
    playsound('amazon.ogg')
    print("")
    print("Si has escuchado el sonido, tu bot está listo. Ejecútalo")

else:
    print(bcolors.FAIL + "El bot tiene algun error o el link se ha roto. Llama a Orti" + bcolors.ENDC)

print(bcolors.ENDC)
