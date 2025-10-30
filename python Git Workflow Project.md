Общая логика проекта внутри папки teest26.py 
1. main.py рабочий код 
2. README.md документация 
3. .gitignore настройки Git 

Code:
Folder: teest26.py
Text file 1: main.py

def say_hello():

print("Hello, Sasha and Git")

  

def main():

say_hello()

  

if __name__ == "__main__":

main()

Разбор: 

1. def say_hello():
    print("Hello, Sasha and Git") - функция что выводит строку тем самым показывая что программа работает 
2. def main():
    say_hello() - определение функции main для запуска логики программы
3. if __name__ == "__main__":
    main() - проверка чтобы программа запускалась напрямую, если да, выполняется main 

Команды запуска: 
1. python3 main.py
2. вывод сообщения "Hello, Sasha and Git"


Code:
Folder: teest26.py 
Text file 2: README.md

# Git Workflow Project

instruction

1. Python3 must be installed.

2. git clone https://github.com/alex2003-dev/python-code-.git

3. Project folder cd ~/Documents/python

4. python3 main.py

5. You will see this print(‘Hello, Sasha and Git’)

Разбор: 
1. Заголовок 
2. Основные инструкции и рекомендации по использованию 

Code:
Folder: teest26.py 
Text file 3: .gitignore

__pycache__/

*.pyc

.env

.vscode/

.idea/

.DS_Store

Разбор: 
Имеет в себе: 
1. Временные файлы python  "__pycache__/.   *.pyc"
2. Среды разработки ".vscode/   .idea/"
3. Системные файлы макос '.DS_Store'
4. Конфиденциальные файлы ".env"


