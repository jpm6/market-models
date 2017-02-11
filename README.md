# 4133 Project
An SVM Classifier trained on S&P 500 financial data.

### HTTPS Clone
```
git clone https://gitlab.com/jpm/4133_Project.git
```
### SSH Clone
```
git clone git@gitlab.com:jpm/4133_Project.git
```

## Requirements
The project is written in Python 3.  It uses the following packages:

- [requests](http://docs.python-requests.org/en/master/)
- [bs4](https://www.crummy.com/software/BeautifulSoup/)
- [yahoo_finance](https://pypi.python.org/pypi/yahoo-finance)

## Options
`python fetch.py -h` prints:
```
usage: fetch.py [-h] [-s SYM] [-d]

optional arguments:
  -h, --help         show this help message and exit
  -d, --data         save current company data to $DATE.csv
  -l, --list         list S&P Companies with sectors
  -s SYM, --sym SYM  print data for given security symbol

```

