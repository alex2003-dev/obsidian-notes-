folder: test15.py
text file: teest15.py 

f = open("log.txt")

i = w = e = 0

for l in f:

    if "INFO" in l: i += 1

    elif "WARN" in l: w += 1

    elif "ERROR" in l: e += 1

f.close()

print("INFO:", i)

print("WARN:", w)

print("ERROR:", e)

Разбор: 
1. f = open("log.txt") - отрывает файл с именем log.txt  в режиме чтения 
2. i = w = e = 0 - три переменные i, w, e для счётчиков сообщений и инициализируем 0
3.  for l in f: -  цикл, который перебирает все строки в файле f
4.  if "INFO" in l: i += 1 -  есть ли в текущей строке INFO, если да увеличиваем счётчик i на 1,  оператор in проверяет вхождение подстроки в строку.
5.  elif "WARN" in l: w += 1 - если INFO не найдено, смотрим есть WARN в строке, если есть увеличиваем счётчик w
6.  elif "ERROR" in l: e += 1 - если нет INFO и WARN, проверяем ERROR, при совпадении увеличиваем счётчик e
7.  f.close() - закрываем файл, чтобы освободить ресурсы
8. print("INFO:", i)
   print("WARN:", w)
   print("ERROR:", e) - подсчёты

txt file: log.txt:
вводим любой текст в том числе слова которые мы будем использовать для подсчёта (INFO/WARN/ERROR.)






