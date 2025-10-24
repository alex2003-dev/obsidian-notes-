первая папка: utils.py

def format_currency(amount):
    return f"${amount:.2f}"

def clamp(value, min_value, max_value):
    return max(min_value, min(value, max_value))

def percent(part, whole):
    if whole == 0:
        return 0
    return (part / whole) * 100

вторая папка: demo.py

from utils import format_currency, clamp, percent

print("Price:", format_currency(99.999))
print("Clamped:", clamp(120, 0, 100))
print("Used percent:", f"{percent(30, 50):.1f}%")



Разбор:
1. def format_currency(amount):
    return f"${amount:.2f}" - эта функция делает число с долларом и после точки добавляет два числа, то есть делает не полное число 
2.  def clamp(value, min_value, max_value):
    return max(min_value, min(value, max_value)) - Эта функция подгоняется под минимальное или максимальное число. 
3. def percent(part, whole):
    if whole == 0:
        return 0
    return (part / whole) * 100 - функция считает, сколько процентов одно число составляет от другого.
4. from utils import format_currency, clamp, percent - импортируют функции из файла utils.py
5. print("Price:", format_currency(99.999)) - выводит цену формата $100.00.
6. print("Clamped:", clamp(120, 0, 100)) - показывает число 120 подогнанное под 100.
7. print("Used percent:", f"{percent(30, 50):.1f}%") - показывает что от 50 - 30 это 60%

Источники:

https://www.geeksforgeeks.org/python/how-to-clamp-floating-numbers-in-python/?utm_source

https://realpython.com/lessons/format-currency-solution/?utm_source=

https://docs.python.org/3/library/locale.html

https://pypi.org/project/multicurrency/?utm_source=