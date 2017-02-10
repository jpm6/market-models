# 4133 Project
An SVM Classifier trained on S&P 500 financial data.

## Requirements
The project is written in Python 3.  It uses the following packages:

- [requests](http://docs.python-requests.org/en/master/)
- [bs4](https://www.crummy.com/software/BeautifulSoup/)
- [yahoo_finance](https://pypi.python.org/pypi/yahoo-finance)

### HTTPS Clone
```
git clone https://gitlab.com/jpm/4133_Project.git
```
### SSH Clone
```
git clone git@gitlab.com:jpm/4133_Project.git
```

## Options
`python fetch.py -h` prints:
```
usage: fetch.py [-h] [-s SYM] [-d]

optional arguments:
  -h, --help         show this help message and exit
  -s SYM, --sym SYM  print data for given security symbol
  -d, --data         save current security data to $DATE.csv

```

