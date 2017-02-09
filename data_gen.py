import csv
import requests

from bs4 import BeautifulSoup
from yahoo_finance import Share

r = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')

soup = BeautifulSoup(r.text, "html.parser")

table = soup.find('table', {'class': 'wikitable sortable'})

sp500 = list()
for row in table.findAll('tr'):
    col = row.findAll('td')
    if col:
        sector = str(col[3].string.strip()).lower().replace(' ', '_')
        ticker = str(col[0].string.strip())      
        sp500.append((ticker,sector))

sp500.sort()

def retrieve(symbol):
    yfd = None
    while not yfd:
        try:
            # connect
            yfd = Share(symbol)
        except:
            pass

    return list(zip(*sorted(list(yfd.data_set.items()))))

with open('data_set.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(retrieve('T')[0])
    for security in sp500:
        print(security[0])
        writer.writerow(retrieve(security[0])[1])
