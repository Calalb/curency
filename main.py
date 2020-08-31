import requests
import json
from os import path
from datetime import date
from Convert_curency.func import Value_from_BNM
import sys


today = str(date.today()) #Primim in format str data curenta
file_name = f"rates_{today}.json" #Creem denumirea fisierului plus data curenta. Pentru a verifica pe viitor daca datele sunt actuale

key = 'cba195725e594e440a6ffc66ee17b79a'
url = 'http://data.fixer.io/api/latest' + '?access_key=' + key

if path.exists(file_name): #Verifica daca exista acest fisier
    file = open(file_name, 'r') #Deschide fisierul in regim de citire
    data = json.loads(file.read()) #Incarca datele din fisier
else:
    respons = requests.get(url) #Transmite o cerere la adresa indicata
    data = json.loads(respons.text) #Incarca datele in format json
    file = open(file_name, 'w') #Creem fisierul rates.json si il deschidem in redim de scriere
    file.write(respons.text) #Scrim in fisierul creeat datele primite cind am trasnmis cererea
    file.close() #Inchidem fisierul creeat

eur = 1.0
mdl = data['rates']['MDL']
usd = data['rates']['USD']
rub = data['rates']['RUB']
def Curency(pN):
    if pN == 'eur':
        return eur
    if pN == 'mdl':
         return mdl
    elif pN == 'usd':
        return usd
    elif pN == 'rub':
        return rub
    else:
        print("Valoare incorecta")

def convertF():
    summ = float(input('Introdu suma: '))
    primar_curency = input('Introdu simbolul valutei curente: ')
    convert_curency = input('Introdu simbolul valutei necesare: ')
    first = Curency(primar_curency)
    second = Curency(convert_curency)
    s = summ * (second/first)
    print(f"Suma este {s} {convert_curency}")
count = -1
while count != 0:
    print(f"Alege optiunea dorita\n 1. Convertire valuta >\n 2. Aflarea ratei istorice >\n 3. Exit >")
    option = int(input("Introdu numarul operatiunii dorite: "))
    if option == 1:
        convertF()
    if option == 2:
        Value_from_BNM()
    if option == 3:
        sys.exit()


