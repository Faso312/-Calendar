import requests
from bs4 import BeautifulSoup as bs



def true_connect(url):
    soup=bs(requests.get(url).text, 'html.parse')
    main_block=soup.find_all('div', class_='row eventsWrapper') #+
    for row_nm, event in enumerate(main_block, start=1): 
        for block_nm, data in enumerate(event, start=1): 
            ev_name=data.find('h3', class_='lines lines2').text
            ev_disc=data.find('div', class_='lines lines4 mb-2').text
            ev_dt_m=data.find('div', class_='event-date').text #перебрать по пробелам
            ev_tags=data.find('div', class_='event-tags').text #перебрать по предлогам, пробелам
            ev_link=''.join(['https://gorodzovet.ru/',data.find('div', class_='innlink event-link save-click').get('data-link')])
            try: ev_price=data.find('span', class_='event-price').text
            except AttributeError: ev_price=''
            #print(f'{block_nm}: {ev_name} ___ {ev_disc} ___ {ev_dt_m} ___ {ev_tags} ___ {ev_link} ___ {ev_price}')
    second_block=soup.find(id="events")
    print(second_block.prettify())

try:
    true_connect('https://gorodzovet.ru/samara/2024/march/')
except Exception as e: print(f'Ошибка вида: {e}.....') #общая обработа ошибок