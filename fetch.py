import argparse
import csv
import requests
import time

from bs4 import BeautifulSoup
from yahoo_finance import Share

def sp_symbols():
    response = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    soup     = BeautifulSoup(response.text, "html.parser")
    table    = soup.find('table', {'class': 'wikitable sortable'})

    sp_symbols = []

    for row in table.findAll('tr'):
        col = row.findAll('td')
        if col:
            sector = str(col[3].string.strip()).lower().replace(' ', '_')
            symbol = str(col[0].string.strip())      

            sp_symbols.append((symbol,sector))

    return sorted(sp_symbols)

def symbol_data(symbol):
    yfd = None
    while not yfd:
        try:
            yfd = Share(symbol)
        except:
            pass

    return list(yfd.data_set.items())

def write_current_data():
    with open(time.strftime('%m-%d-%Y') + '.csv', 'w') as csv_file:

        form = lambda d: list(zip(*sorted(d)))

        writer = csv.writer(csv_file)
        writer.writerow(form(symbol_data('T')[0]))

        for security in sp_symbols():
            print(security[0])
            writer.writerow(form(symbol_data(security[0]))[1])

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--sym', type=str, help='the ticker of an SP 500 stock')
    parser.add_argument('-d', '--data', action='store_true', help='fetch current data all stocks')
    args = parser.parse_args()

    if args.sym: print(*symbol_data(args.sym), sep='\n')
    
    if args.data: write_current_data()
