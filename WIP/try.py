import requests
from bs4 import BeautifulSoup as bs



def connection(url):
    r = requests.get(url)
    soup=bs(r.text, 'lxml')
    #ev_mon=soup.find_all('a', class_='event-month')
    #ev_day=soup.find_all('span', class_='event-day.innlink')
    ev_name=soup.find_all('h3', class_='lines lines2')
    ev_disc=soup.find_all('div', class_='lines lines4 mb-2')

try:
 connection('https://gorodzovet.ru/samara/2024/march/')
except Exception as e: print(f'Ошибка вида: {e}.....') #общая обработа ошибок