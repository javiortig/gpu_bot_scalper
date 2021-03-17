import requests
from bs4 import BeautifulSoup
import cloudscraper
import re

from time import sleep

from playsound import playsound

# pip install cloudscraper
# pip install playsound
# pip install bs4

# TODO: HACER PRUEBA DE Q LE FUNCIONE A LOS CABEZAS LOS BOTS CON LOS MISMOS LINKS

DELAY = 47
link = "https://www.pccomponentes.com/buscar/?query=6700%20XT"


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


print("PINCHANDO LAS 6700 DE PC COMPONENTES...")
while(True):
    scraper = cloudscraper.create_scraper()
    html = scraper.get(
        link).content
    soup = BeautifulSoup(html, 'html.parser')
    soup = soup.findAll(
        "div", class_="c-product-card__content")
    if(not soup):
        print(bcolors.FAIL +"Filter not passed. Retry in 7..." + bcolors.ENDC)
        sleep(7)
        continue
    else:
        print(bcolors.OKGREEN + "Filter passed" + bcolors.ENDC)

    for span in soup:
        result = str(span)

        result = re.search("6700\s*xt", result, re.IGNORECASE)
        if(not result):
            continue
        else:
            print("He encontrado match con: \'" + result[0] + "\'")
            while(True):
                print(bcolors.OKGREEN +
                      "!!!!!!!!!!!HAY GRAFICA PC COMPONENTES!!!!!!!!!!!!!" + bcolors.ENDC)
                playsound('pcComponentes.ogg')
                sleep(2)

    print(bcolors.WARNING + "not found" + bcolors.ENDC)
    print(bcolors.WARNING +"Retrying in " + str(DELAY) + "s..." + bcolors.ENDC)
    sleep(DELAY)
