import xml.etree.ElementTree as ET
import requests


def Value_from_BNM():
    data = input("Input data in format dd.mm.yyyy: ")
    url = 'http://www.bnm.md/ro/official_exchange_rates' '?get_xml=1&date=' + data
    respons = requests.get(url)
    with open('export.xml', 'w') as file:
        file.write(respons.text)
    tree = ET.parse('export.xml')
    root = tree.getroot()
    ch = input("Introdu caracterul valutei in registru de sus: ")
    for x in root.findall('Valute'):
        chrCode = x.find('CharCode').text
        val = x.find('Value').text
        if chrCode == ch :
            print(f"Valoarea la {chrCode} pe data: {data} a fost - {val} MDL")


