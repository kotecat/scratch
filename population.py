import requests
import time
from bs4 import BeautifulSoup
from scratchclient import ScratchSession

pop = 'https://countrymeters.info/ru/World'
btc = 'https://www.marketwatch.com/investing/cryptocurrency/btcusd'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}

#!-You DATA-!
session = ScratchSession("youLOGIN", "youPASS")
connection = session.create_cloud_connection(560776491)  #<---project-id

#----> PARSER!!!
def parserp(type):
	full_page_p = requests.get(pop, headers=headers)
	soup_p = BeautifulSoup(full_page_p.content, 'html.parser')

	if type == 1:
		count_p_a = soup_p.findAll("div", {"id": "cp1"})
		return(count_p_a[0].text)
	else:
		count_p_m = soup_p.findAll("div", {"id": "cp2"})
		return(count_p_m[0].text)

def parserbtc():
	full_page_btc = requests.get(btc, headers=headers)
	soup_b = BeautifulSoup(full_page_btc.content, 'html.parser')
	count_btc = soup_b.find_all("bg-quote", {"class": "value", "field": "Last", "format": "0,0."})
	return(count_btc[0].text)	


i = 2

while i >= 1:
	btccc = parserbtc().replace(',', '')
	p = parserp(1).replace(' ', '')
	m = parserp(0).replace(' ', '')

	connection.set_cloud_variable("btc", btccc)
	connection.set_cloud_variable("p", p)
	connection.set_cloud_variable("m", m)

	time.sleep(1) #<--ЗАДЕРЖКА
