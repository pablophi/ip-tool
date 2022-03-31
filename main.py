from ip2geotools.databases.noncommercial import DbIpCity
import time
import json


def choose_lng():
    lng = input(f'\n>>Choose language/Выберите язык(eng / ru):')
    if lng == 'eng':
        get_ip_eng()
    elif lng == 'ru':
        get_ip_ru()
    else:
        print('Please, write "eng" or "ru"\nПожалуйста, введите "eng" или "ru"')

def get_ip_eng():
    ip = input('\n>> Write IP: ')
    time.sleep(1)
    response = DbIpCity.get(ip, api_key='free')
    r_json = response.to_json()
    result = json.loads(r_json)
    print(f'---------------------------------------\n'
          f'City: {result["city"]}\n'
          f'Region: {result["region"]}\n'
          f'Country: {result["country"]}\n'
          f'Latitude: {result["latitude"]}\n'
          f'Longitude: {result["longitude"]}\n'
          f'---------------------------------------\n'
          f'(using latitude and longitude, you can find the approximate location of a person on the map using the website https://geotree.ru/)')
    time.sleep(60)

def get_ip_ru():
    ip = input('\n>> Введите желаемый IP: ')
    time.sleep(1)
    response = DbIpCity.get(ip, api_key='free')
    r_json = response.to_json()
    result = json.loads(r_json)
    print(f'---------------------------------------\n'
          f'Город: {result["city"]}\n'
          f'Регион/Область: {result["region"]}\n'
          f'Страна: {result["country"]}\n'
          f'Широта: {result["latitude"]}\n'
          f'Долгота: {result["longitude"]}\n'
          f'---------------------------------------\n'
          f'(используя широту и долготу вы можете найти примерное местоположение человека на карте, с помощью сайта https://geotree.ru/)')
    time.sleep(60)

def main():
    banner()
    choose_lng()

def banner():
    print('''
                 __    __            __    _ 
    ____  ____ _/ /_  / /___  ____  / /_  (_)
   / __ \/ __ `/ __ \/ / __ \/ __ \/ __ \/ / 
  / /_/ / /_/ / /_/ / / /_/ / /_/ / / / / /  
 / .___/\__,_/_.___/_/\____/ .___/_/ /_/_/   
/_/                       /_/                

tg: @pablophi_dev
'''
)


if __name__ == '__main__':
    main()


