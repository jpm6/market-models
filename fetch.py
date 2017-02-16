import argparse
import csv
import re
import requests
import time

from bs4 import BeautifulSoup
from yahoo_finance import Share


'''
Returns a sorted list of SP 500 Companies tuples in the form:

    (SYMBOL, NAME, SECTOR)
'''
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


'''
Takes in a security symbol, ex: 'FDX'

Returns a dictionary of financial attributes.
'''
def symbol_data(symbol):
    yfd = None
    while not yfd:
        try:
            yfd = Share(symbol)
        except:
            pass

    return yfd.data_set


'''
Takes in a dictionary of a security's financial data.

Converts every attribute to numeric representation and introduces some new attributes.

Returns a sorted list of financial attribute tuples, or an empty list if data missing.
'''
def clean_data(d):
    exchanges   = {'NMS': 0, 'NYQ': 1}
    letters     = {'B': 10 ** 9, 'M': 10 ** 6, 'T': 10 ** 12}

    dy = 'DividendYield'
    eb = 'EBITDA'
    en = 'EPSEstimateNextYear'
    mc = 'MarketCapitalization'
    op = 'Open'
    pb = 'PriceBook'
    pc = 'PriceEPSEstimateCurrentYear'
    pn = 'PriceEPSEstimateNextYear'
    pe = 'PERatio'
    se = 'StockExchange'
    tg = 'OneyrTargetPrice'

    pa = ['PercentChange',
          'PercentChangeFromFiftydayMovingAverage',
          'PercentChangeFromTwoHundreddayMovingAverage',
          'PercentChangeFromYearHigh',
          'PercentChangeFromYearLow' ]
    
    letter_conv     = lambda d,s: float(d[s][:-1]) * letters[d[s][-1]] 
    percent_conv    = lambda d,s: float(d[s].strip('%')) / 100

    d['PercentChangeFromYearHigh'] = d.pop('PercebtChangeFromYearHigh')
    d['.Symbol'] = d.pop('symbol')
    d['.Name'] = d.pop('Name')

    d['OneyrTargetOverCurrent'] = float(d[tg]) / float(d[op]) if d[tg] else 1
    d['PercentChangeAfterHours'] = float(d[op]) / float(d['PreviousClose']) - 1
    
    if re.search('[A-Z]', d[eb]): d[eb] = letter_conv(d,eb) 
    if re.search('[A-Z]', d[mc]): d[mc] = letter_conv(d,mc) 

    d[dy] = d[dy] if d[dy] else 0
    d[se] = exchanges[d[se]] 

    for a in pa: d[a] = percent_conv(d,a)
    for a in [eb, pb, pc, pn, en, pe]:
        if not d[a]: return []

    for a in [l.rstrip('\n') for l in open('attributes.txt') if '#' not in l]: del d[a]

    return sorted(list(d.items()))


'''
Writes the cleaned current financial attributes of all SP 500 companies to {TODAY}.csv
'''
def write_current_data():
    with open('data/' + time.strftime('%m-%d-%Y') + '.csv', 'w') as csv_file:

        form = lambda d: list(zip(*clean_data(d)))

        writer = csv.writer(csv_file)
        writer.writerow(form(symbol_data('T'))[0])

        for security in sp_symbols():
            print(security[0])
            row = form(symbol_data(security[0]))
            if row: writer.writerow(row[1])

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--data', action='store_true', help='save current company data to $DATE.csv')
    parser.add_argument('-l', '--list', action='store_true', help='list S&P Companies with sectors')
    parser.add_argument('-s', '--sym', type=str, help='print data for given security symbol')
    args = parser.parse_args()

    if args.data: write_current_data()
    if args.list: print(*sp_symbols(), sep='\n')
    if args.sym : print(*symbol_data(args.sym).items(), sep='\n')
