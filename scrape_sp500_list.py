import requests
from bs4 import BeautifulSoup

r = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')

soup = BeautifulSoup(r.text)

table = soup.find('table', {'class': 'wikitable sortable'})

sector_tickers = dict()
for row in table.findAll('tr'):
    if row.findAll('td'):
        sector = str(col[3].string.strip()).lower().replace(' ', '_')
        ticker = str(col[0].string.strip())      
        if sector not in sector_tickers:
            sector_tickers[sector] = list()
        sector_tickers[sector].append(ticker)
