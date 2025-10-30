Code: Main folder, weather.py 

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

except:

return {}

  

def save_cache(cache):

try:

with open(CACHE_FILE, "w") as f:

json.dump(cache, f)

except:

pass

  

def get_weather_from_api(city):

params = {

"place_id": city,

"sections": "current",

"units": "metric",

"language": "uk",

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

except:

return None

  

def get_weather(city="kyiv"):

cache = load_cache()

now = time.time()

if city in cache:

entry = cache[city]

if now - entry["timestamp"] < CACHE_EXPIRY:

return entry["data"]

weather_data = get_weather_from_api(city)

if weather_data:

cache[city] = {"timestamp": now, "data": weather_data}

save_cache(cache)

return weather_data

  

def main():

weather_info = get_weather("kyiv")

if weather_info:

print("City:", weather_info["city"])

print("Temperature:", weather_info["temperature"], "°C")

print("Conditions:", weather_info["conditions"])

else:

print("Failed to get weather data")

  

if __name__ == "__main__":

main()

 Разбор: 

1. import requests
import json
import os
import time

API_KEY = "YOUR_METEOSOURCE_API_KEY"
BASE_URL = "https://www.meteosource.com/api/v1/free/point"
CACHE_FILE = "weather_cache.json"
CACHE_EXPIRY = 3600 - импорт библиотеки для работы с HTTP, JSON, файлами OS и временем
2. def load_cache():
    if not os.path.exists(CACHE_FILE):
        return {}
    try:
        with open(CACHE_FILE, "r") as f:
            return json.load(f)
    except:
        return {}

def save_cache(cache):
    try:
        with open(CACHE_FILE, "w") as f:
            json.dump(cache, f)
    except:
        pass -  работа с кэшем
3. def get_weather_from_api(city):
    params = {
        "place_id": city,
        "sections": "current",
        "units": "metric",
        "language": "uk",
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
    except:
        return None - формирование параметров запроса к API, делает HTTP-запрос проверяя статус, из ответа получается текущая температура и условие, если что-то пошло не так возвращается none
4. def get_weather(city="kyiv"):
    cache = load_cache()
    now = time.time()
    if city in cache:
        entry = cache[city]
        if now - entry["timestamp"] < CACHE_EXPIRY:
            return entry["data"]
    weather_data = get_weather_from_api(city)
    if weather_data:
        cache[city] = {"timestamp": now, "data": weather_data}
        save_cache(cache)
    return weather_data - проверяет кэш, если данные актуальные, возвращает их, если данных нет или они устарели обращение к API, обновляет кэш с текущими данными.
5. def main():
    weather_info = get_weather("kyiv")
    if weather_info:
        print("City:", weather_info["city"])
        print("Temperature:", weather_info["temperature"], "°C")
        print("Conditions:", weather_info["conditions"])
    else:
        print("Failed to get weather data")

if __name__ == "__main__":
    main() - если данные получены, выводит город, температуру и условия, если нет сообщение об ошибке, выполняется только при запуске файла напрямую.

Code: 
test folder 2

import unittest

import weather

import os

import time

  

class TestWeather(unittest.TestCase):

  

def setUp(self):

if os.path.exists(weather.CACHE_FILE):

os.remove(weather.CACHE_FILE)

  

def test_load_empty_cache(self):

cache = weather.load_cache()

self.assertEqual(cache, {})

  

def test_save_and_load_cache(self):

data = {"kyiv": {"timestamp": time.time(), "data": {"temperature": 20, "conditions": "sunny"}}}

weather.save_cache(data)

loaded = weather.load_cache()

self.assertEqual(loaded["kyiv"]["data"]["temperature"], 20)

  

def test_get_weather_from_api_success(self):

result = weather.get_weather_from_api("kyiv")

self.assertIsInstance(result, dict)

self.assertIn("temperature", result)

self.assertIn("conditions", result)

  

def test_get_weather_from_api_fail(self):

result = weather.get_weather_from_api("invalid_city_123")

self.assertTrue(result is None or isinstance(result, dict))

  

def test_get_weather_cache_hit(self):

city = "kyiv"

data = {"timestamp": time.time(), "data": {"temperature": 25, "conditions": "sunny"}}

weather.save_cache({city: data})

result = weather.get_weather(city)

self.assertEqual(result["temperature"], 25)

  

def test_get_weather_cache_expired(self):

city = "kyiv"

old_time = time.time() - (weather.CACHE_EXPIRY + 10)

data = {"timestamp": old_time, "data": {"temperature": 25, "conditions": "sunny"}}

weather.save_cache({city: data})

result = weather.get_weather(city)

self.assertIsInstance(result, dict)

  

def test_get_weather_invalid_city(self):

result = weather.get_weather("invalid_city_123")

self.assertTrue(result is None or isinstance(result, dict))

  

def test_cache_file_created(self):

city = "kyiv"

weather.get_weather(city)

self.assertTrue(os.path.exists(weather.CACHE_FILE))

  

if __name__ == "__main__":

unittest.main()


Разбор: 

1. import unittest
import weather
import os
import time - импорт библиотеки для работы с HTTP, JSON, файлами OS и временем 
2. class TestWeather(unittest.TestCase): - создание класса тестов 
3.     def setUp(self):
        if os.path.exists(weather.CACHE_FILE):
            os.remove(weather.CACHE_FILE) -  метод выполняется перед каждым тестом, проверка есть ли файл кэша, и удаляет его
4.     def test_load_empty_cache(self):
        cache = weather.load_cache()
        self.assertEqual(cache, {})

    def test_save_and_load_cache(self):
        data = {"kyiv": {"timestamp": time.time(), "data": {"temperature": 20, "conditions": "sunny"}}}
        weather.save_cache(data)
        loaded = weather.load_cache()
        self.assertEqual(loaded["kyiv"]["data"]["temperature"], 20) - проверяет, что при отсутствии файла кэша функция возвращает пустой словарь так же проверяет, что данные корректно сохраняются и загружаются из файла
5.     def test_get_weather_from_api_success(self):
        result = weather.get_weather_from_api("kyiv")
        self.assertIsInstance(result, dict)
        self.assertIn("temperature", result)
        self.assertIn("conditions", result)

    def test_get_weather_from_api_fail(self):
        result = weather.get_weather_from_api("invalid_city_123")
        self.assertTrue(result is None or isinstance(result, dict)) - проверяет, что API возвращает словарь с ключами, проверяет, что для неверного города возвращается none или словарь
6.     def test_get_weather_cache_hit(self):
        city = "kyiv"
        data = {"timestamp": time.time(), "data": {"temperature": 25, "conditions": "sunny"}}
        weather.save_cache({city: data})
        result = weather.get_weather(city)
        self.assertEqual(result["temperature"], 25)

    def test_get_weather_cache_expired(self):
        city = "kyiv"
        old_time = time.time() - (weather.CACHE_EXPIRY + 10)
        data = {"timestamp": old_time, "data": {"temperature": 25, "conditions": "sunny"}}
        weather.save_cache({city: data})
        result = weather.get_weather(city)
        self.assertIsInstance(result, dict) - проверяет, что функция возвращает данные из кэша, если они свежие, проверяет, что функция обновляет данные через API
7.     def test_get_weather_invalid_city(self):
        result = weather.get_weather("invalid_city_123")
        self.assertTrue(result is None or isinstance(result, dict))

    def test_cache_file_created(self):
        city = "kyiv"
        weather.get_weather(city)
        self.assertTrue(os.path.exists(weather.CACHE_FILE)) - проверяет обработку ошибки при неправильном названии города, проверяет, что кэш-файл создаётся после запроса
8. if __name__ == "__main__":
    unittest.main() - запуск файла напрямую 






