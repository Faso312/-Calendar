# main
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

def main(): #основная функция системы
    URL_TEMPLATE = "https://gorodzovet.ru/samara/2024/march/"
    r = requests.get(URL_TEMPLATE)
    print(r.status_code)
    pass

    
try: #последовательная обработка функциий
    if __name__ == '__main__': 
        pass
except KeyboardInterrupt as e: 
    print(f'Работа приостановлена......') #прерывание через Ctrl+C
except Exception as e: print(f'Ошибка вида: {e}.....') #общая обработа ошибок