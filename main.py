# main


def main(): #основная функция системы
 pass

    
try: #последовательная обработка функциий
    if __name__ == '__main__': 
        pass
except KeyboardInterrupt as e: 
    print(f'Работа приостановлена......') #прерывание через Ctrl+C
except Exception as e: print(f'Ошибка вида: {e}.....') #общая обработа ошибок