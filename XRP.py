import telebot
import requests
from bs4 import BeautifulSoup
import time
token='1352935786:AAFe1IEDEx22hL2Wn2HxWimXGek6mvOBmmU'
bot = telebot.TeleBot(token)
headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
}

priceusdfixed1 = 0.00
def price():
    global priceusdfixed1
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

    if priceusdfixed1 == priceusdfixed: 
        print('XRP is same: ' + str(priceusdfixed) + ' ' + str(priceusdfixed1))
    else:
        priceusdfixed1=priceusdfixed
        requests.get('https://api.telegram.org/bot{}/sendMessage'.format(token), params=dict(
        chat_id='@pricexrp',
        text=str(xrprub) + '₽ | ' + str(priceusdfixed1) + '$'
        ))

while True:
    time.sleep(1)
    price()
bot.polling()
