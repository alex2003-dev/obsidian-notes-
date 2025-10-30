Code: 
1.  folder: storage.py

import json

import os

  

file_name = "expenses.json"

  

def load_expenses():

if not os.path.exists(file_name):

return []

try:

with open(file_name, "r") as f:

return json.load(f)

except:

print("Error reading file")

return []

  

def save_expenses(data):

try:

with open(file_name, "w") as f:

json.dump(data, f, indent=2)

except:

print("Error saving file")

Разбор: 
1. import json
   import os - подключения модуля JSON для работы с файлами и os для проверки
2. file_name = "expenses.json" - имя файла где хранятся разборы 
3. def load_expenses():
    if not os.path.exists(file_name):
        return []
    try:
        with open(file_name, "r") as f:
            return json.load(f)
    except:
        print("Error reading file")
        return []  - загружает файлы  с "expenses.json", если их нет возращает пустой список 
4. def save_expenses(data):
    try:
        with open(file_name, "w") as f:
            json.dump(data, f, indent=2)
    except:
        print("Error saving file") - сохраняет список расходов в файл, если будет какая-то ошибка напишется слово в print 

Code:
2. Folder: logic.py 

import storage

  

def add_expense(name, amount, category):

data = storage.load_expenses()

try:

amount = float(amount)

except:

print("Invalid amount")

return

item = {"name": name, "amount": amount, "category": category}

data.append(item)

storage.save_expenses(data)

print("Expense added")

  

def list_expenses():

data = storage.load_expenses()

if not data:

print("No expenses yet")

return

total = 0

for i in data:

print(i["name"], "-", i["amount"], "(", i["category"], ")")

total += i["amount"]

print("Total:", total)

  

def filter_expenses(category):

data = storage.load_expenses()

found = [x for x in data if x["category"].lower() == category.lower()]

if not found:

print("No expenses in this category")

return

total = 0

for i in found:

print(i["name"], "-", i["amount"])

total += i["amount"]

print("Total for", category + ":", total)


Разбор:

 1. import storage - модуль storage.py чтобы использовать функции load_expenses() и save_expenses()
2. def add_expense(name, amount, category):
    data = storage.load_expenses()
    try:
        amount = float(amount)
    except:
        print("Invalid amount")
        return
    item = {"name": name, "amount": amount, "category": category}
    data.append(item)
    storage.save_expenses(data)
    print("Expense added") - добавляет расход, преображает сумму в число, если не выходит то будет ошибка 
3. def list_expenses():
    data = storage.load_expenses()
    if not data:
        print("No expenses yet")
        return
    total = 0
    for i in data:
        print(i["name"], "-", i["amount"], "(", i["category"], ")")
        total += i["amount"]
    print("Total:", total) - показывает все расходы и считает их сумму 
4. def filter_expenses(category):
    data = storage.load_expenses()
    found = [x for x in data if x["category"].lower() == category.lower()]
    if not found:
        print("No expenses in this category")
        return
    total = 0
    for i in found:
        print(i["name"], "-", i["amount"])
        total += i["amount"]
    print("Total for", category + ":", total) - фильтрует расходы по категориям 


Code: 
3. Folder: cli.py

import logic

  

def main():

while True:

print("\n1. Add expense")

print("2. List all")

print("3. Filter by category")

print("4. Exit")

choice = input("Choose: ")

if choice == "1":

name = input("Name: ")

amount = input("Amount: ")

category = input("Category: ")

logic.add_expense(name, amount, category)

elif choice == "2":

logic.list_expenses()

elif choice == "3":

cat = input("Category: ")

logic.filter_expenses(cat)

elif choice == "4":

print("Bye")

break

else:

print("Wrong choice")

  

if __name__ == "__main__":

main()

Разбор: 
1. import logic - подключение модуля для просмотра и фильтрации расходов
2. def main():
    while True:
        print("\n1. Add expense")
        print("2. List all")
        print("3. Filter by category")
        print("4. Exit")
        choice = input("Choose: ") - функция main запускает меню в цикле, вывод списка действий
3.         if choice == "1":
            name = input("Name: ")
            amount = input("Amount: ")
            category = input("Category: ")
            logic.add_expense(name, amount, category) - если пользователь выбрал первый вариант, то спрашиваем имя, сумму и категорию
4.         elif choice == "2":
            logic.list_expenses() - вывод всех расходов
5.         elif choice == "3":
            cat = input("Category: ")
            logic.filter_expenses(cat) - фильтр по категории
6.         elif choice == "4":
            print("Bye")
            break - выход из программы, завершение цикла 
7.         else:
            print("Wrong choice") - обработка неверного кода 
8. if __name__ == "__main__":
    main() - команда старт кода в терминале


