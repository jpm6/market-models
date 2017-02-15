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
            symbol  = col[0].string.replace('.','') 
            name    = col[1].string
            sector  = col[3].string

            sp_symbols.append((symbol, name, sector))

    return sorted(sp_symbols)

def symbol_data(symbol):
    yfd = None
    while not yfd:
        try:
            yfd = Share(symbol)
        except:
            pass

    return sorted(list(yfd.data_set.items()))

def write_current_data():
    with open('data/' + time.strftime('%m-%d-%Y') + '.csv', 'w') as csv_file:

        form = lambda d: list(zip(*clean(d)))

        writer = csv.writer(csv_file)
        writer.writerow(form(symbol_data('T'))[0])

        for security in sp_symbols():
            print(security[0])
            writer.writerow(form(symbol_data(security[0]))[1])

def clean(data):
    f = [line.rstrip('\n') for line in open('filtered_attributes.txt')]
    return [a for a in data if a[0] not in f]


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--data', action='store_true', help='save current company data to $DATE.csv')
    parser.add_argument('-l', '--list', action='store_true', help='list S&P Companies with sectors')
    parser.add_argument('-s', '--sym', type=str, help='print data for given security symbol')
    args = parser.parse_args()

    if args.data: write_current_data()
    if args.list: print(*sp_symbols(), sep='\n')
    if args.sym : print(*symbol_data(args.sym), sep='\n')
