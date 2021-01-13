import requests
from bs4 import BeautifulSoup

#def get_html(url):
#    response = requests.get(url)
#    return response.text
#
#def get_price(html)
headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
}
urlusd = 'https://coinmarketcap.com/ru/currencies/xrp/'
rusd = requests.get(urlusd, headers = headers)
urlrub = 'https://ru.investing.com/currencies/usd-rub'
rrub = requests.get(urlrub, headers = headers)

soupusd = BeautifulSoup(rusd.text, features='html.parser')
priceusd = soupusd.find('div', class_ = 'priceValue___11gHJ')
souprub = BeautifulSoup(rrub.text, features='html.parser')
pricerub = souprub.find('span',class_='arial_26 inlineblock pid-2186-last')
priceusdfixed = priceusd.text[1:]
pricerub = pricerub.text.replace(',', '.')
priceusdfixed = float(priceusdfixed)
pricerub = float(pricerub)
xrprub = round(priceusdfixed*pricerub,2)
print(xrprub)




