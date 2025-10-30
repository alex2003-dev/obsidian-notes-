Code: 

import requests

import json

import os

  

cache_file = "data_cache.json"

url = "https://api.coindesk.com/v1/bpi/currentprice.json"

  

if os.path.exists(cache_file):

with open(cache_file, "r") as f:

data = json.load(f)

else:

r = requests.get(url)

data = r.json()

with open(cache_file, "w") as f:

json.dump(data, f, indent=2)

  

bpi = data["bpi"]

for key, value in bpi.items():

print("Currency:", key)

print("Rate:", value["rate"])

print("Description:", value["description"])

print("---------------------")

Разбор: 

1. import requests - даёт возможность делать http запросы через библеотеку requests, для получения данных с сайтов или API 
2. import json - чтение и запись в формате JSON 
3. import os - работа с файлами и папками например: проверять, создавать, удалять 
4. cache_file = "data_cache.json" - создание переменной для хранения кэша, чтобы в дальнейшем не запускать всё заново
5. url = "https://api.coindesk.com/v1/bpi/currentprice.json" - адрес API сайта
6. if os.path.exists(cache_file): - проверка существующего файла с помощью кэша
7.     with open(cache_file, "r") as f:
        data = json.load(f) - если файл существует читаем его и превращаем в словарь python 
8. else:
    r = requests.get(url)
    data = r.json() - если файла нету делает запрос к сайту 
9.     with open(cache_file, "w") as f:
        json.dump(data, f, indent=2) - данные с сайта сохраняет в кэш + делает файл отформатированным 
10. bpi = data["bpi"] - из всего берет только bpi там лежат курсы валют
11. for key, value in bpi.items(): - перебирает все валюты 
12. print("Currency:", key)
print("Rate:", value["rate"])
print("Description:", value["description"])
print("---------------------") - принт валют в терминале 

