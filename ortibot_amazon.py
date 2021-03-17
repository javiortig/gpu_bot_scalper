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
link = "https://www.amazon.es/s?k=6700+xt&__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss_2"


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


print("PINCHANDO LAS 6700 DE AMAZON...")
while(True):
    scraper = cloudscraper.create_scraper()
    html = scraper.get(
        link).content
    soup = BeautifulSoup(html, 'html.parser')
    soup = soup.findAll(
        "span", class_="a-size-base-plus a-color-base a-text-normal")
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
                print(bcolors.WARNING +
                      "!!!!!!!!!!!HAY GRAFICA AMAZON!!!!!!!!!!!!!" + bcolors.ENDC)
                playsound('amazon.ogg')
                sleep(2)

    print(bcolors.WARNING + "not found" + bcolors.ENDC)
    print(bcolors.WARNING +"Retrying in " + str(DELAY) + "s..." + bcolors.ENDC)
    sleep(DELAY)
