Code: 

import requests

import json

import os

import time

  

API_KEY = "YOUR_METEOSOURCE_API_KEY"

BASE_URL = "https://www.meteosource.com/api/v1/free/point"

CACHE_FILE = "weather_cache.json"

CACHE_EXPIRY = 3600

  

def load_cache():

if not os.path.exists(CACHE_FILE):

return {}

try:

with open(CACHE_FILE, "r") as f:

return json.load(f)

except Exception:

return {}

  

def save_cache(cache):

try:

with open(CACHE_FILE, "w") as f:

json.dump(cache, f)

except Exception:

pass

  

def get_weather_from_api(city):

params = {

"place_id": city,

"sections": "current",

"units": "metric",

"language": "en",

"key": API_KEY

}

try:

response = requests.get(BASE_URL, params=params, timeout=10)

response.raise_for_status()

data = response.json()

current = data.get("current", {})

return {

"city": city,

"temperature": current.get("temperature"),

"conditions": current.get("summary")

}

except requests.RequestException as e:

print("Network error:", e)

return None

except ValueError:

print("Error decoding response")

return None

  

def get_weather(city):

cache = load_cache()

now = time.time()

if city in cache:

entry = cache[city]

if now - entry["timestamp"] < CACHE_EXPIRY:

return entry["data"]

weather = get_weather_from_api(city)

if weather:

cache[city] = {"timestamp": now, "data": weather}

save_cache(cache)

return weather

  

def main():

city = "kyiv"

weather = get_weather(city)

if weather:

print("City:", weather["city"])

print("Temperature:", weather["temperature"], "°C")

print("Conditions:", weather["conditions"])

else:

print("Could not get weather data.")

  

if __name__ == "__main__":

main()

Разбор: 

1. import requests
import json
import os
import time - импортирование модулей
2. API_KEY = "YOUR_METEOSOURCE_API_KEY"
BASE_URL = "https://www.meteosource.com/api/v1/free/point"
CACHE_FILE = "weather_cache.json"
CACHE_EXPIRY = 3600 - заданные настройки 
3. def load_cache():
    if not os.path.exists(CACHE_FILE):
        return {} - функция загружает данные из файла, если их нет, возвращает пустой словарь
4.     try:
        with open(CACHE_FILE, "r") as f:
            return json.load(f)
    except Exception:
        return {} -   программа пытается открыть его и прочитать JSON-данные, если файл повреждён, возвращает пустой словарь
5. def save_cache(cache):
    try:
        with open(CACHE_FILE, "w") as f:
            json.dump(cache, f)
    except Exception:
        pass - сохраняет кэш в файл weather_cache.json, при ошибках программа их пропускает чтобы не завершать процесс
6. def get_weather_from_api(city): - делает запрос к сайту чтобы узнать актуальные данные 
7.     params = {
        "place_id": city,
        "sections": "current",
        "units": "metric",
        "language": "en",
        "key": API_KEY
    } - создание словаря params, они будут отправлены на сайт 
8.     try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        response.raise_for_status() - отправка запроса на сайт, если случается ошибка, программа выбросит её
9.         data = response.json()
        current = data.get("current", {}) - полученние данных в формате JSON и сохранение их в переменной data
10.         return {
            "city": city,
            "temperature": current.get("temperature"),
            "conditions": current.get("summary")
        } - формирование словаря с нужной информацией 
11.     except requests.RequestException as e:
        print("Network error:", e)
        return None
    except ValueError:
        print("Error decoding response")
        return None - при ошибке сама программа не упадёт, будет сообщение Network error и возврат none 
12. def get_weather(city): - функция которая решает брать ли погоду из кэша или с сайта
13.     cache = load_cache()
    now = time.time() - загружает текущий кэш
14.     if city in cache:
        entry = cache[city]
        if now - entry["timestamp"] < CACHE_EXPIRY:
            return entry["data"] - если город есть в кэше, то программа возвращает их сразу, без запроса на сайт
15.     weather = get_weather_from_api(city) - если данные устарели или их нет, идёт запрос о погоде через API 
16.     if weather:
        cache[city] = {"timestamp": now, "data": weather}
        save_cache(cache)
    return weather - если погода получена, она сохраняется в кэш 
17. def main():
    city = "kyiv" - заданный город 
18.     weather = get_weather(city) - получение погоды из кэша 
19.     if weather:
        print("City:", weather["city"])
        print("Temperature:", weather["temperature"], "°C")
        print("Conditions:", weather["conditions"])
    else:
        print("Could not get weather data.") - если данные полученны идёт вывод информации, если нет вывод ошибки
20. if __name__ == "__main__":
    main() - часть запуска если код запускается на прямую 

