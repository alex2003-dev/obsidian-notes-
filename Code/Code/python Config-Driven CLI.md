Код: 

import json

  

settings = {

"speed": "medium",

"retries": 3

}

  

try:

with open("config.json", 'r') as f:

conf = json.load(f)

settings.update(conf)

except FileNotFoundError:

pass

except json.JSONDecodeError:

pass

except Exception:

pass

Разбор и последовательность файлов: 

1. import json - модуль для работы с JSON файлами, хранения настроек и данных 
2. settings = {
    "speed": "medium",
    "retries": 3
}.   -   значения используются, если файл отсутствует или повреждён, так же создаёт словарь с начальными параметрами 
3. try:
    with open("config.json", 'r') as f:
        conf = json.load(f)
        settings.update(conf) - первый блок открывает файл config.json для чтения read mode, если файл существует, переменная f становится файлом. Второй блок загружает данные из файла и преобразует их из формата JSON в словарь python 
4.  except FileNotFoundError:
    pass
except json.JSONDecodeError:
    pass
except Exception:
    pass. - обрабатывает ошибки 



