
todos = []

def add(task):
    todos.append(task)
    return todos

def remove(index):
    if 0 <= index < len(todos):
        todos.pop(index)
    return todos

def view():
    for i, t in enumerate(todos):
        print(f"{i}: {t}")
    return todos

def main():
    while True:
        cmd = input("cmd (add/rm/view/exit): ")
        if cmd == "add":
            t = input("task: ")
            add(t)
        elif cmd == "rm":
            i = int(input("index: "))
            remove(i)
        elif cmd == "view":
            view()
        elif cmd == "exit":
            break

main()



Разбор: 
1. todos = [] - создаёт пустой список с задачами или делами 
2. def add(task):
    todos.append(task)
    return todos  - добавляет задачу в список todos, и возвращает весь список задач после добавления новой.
3. def remove(index):
    if 0 <= index < len(todos):
        todos.pop(index)
    return todos - функция remove которая безопасно удаляет задачу по индексу, не вызывает ошибок, если индекс неправильный и возвращает обновлённый список.
4. def view():
    for i, t in enumerate(todos):
        print(f"{i}: {t}")
    return todos - фунуция view которая перебирает список задач todos, красиво выводит их с номерами и возвращает весь список задач.
5. def main(): - главная функция, где запускается циклическое меню.
6.  while True: - программа без exit циклична 
7.  cmd = input("cmd (add/rm/view/exit): ") - команды как в терминале на ввод
8.  if cmd == "add":
            t = input("task: ")
            add(t)   -  команда add, запрашивает текст задачи (t) и передаётся в функцию add.
9.  elif cmd == "rm":
            i = int(input("index: "))
            remove(i)  -   rm, запрашивает номер задачи (index) , превращается в int, и вызывается remove(i).
10. elif cmd == "view":
            view() - view, вызывает функцию view() и показывает задачи.
11.  elif cmd == "exit":
            break  - если пользователь пишет exit то команда завершается
12. main() - запуск команды совершается через main 
 
Источники: 

https://github.com/LLR1/Python-ToDo-List?utm_source=

https://notebook.community/IST256/learn-python/content/lessons/08/Now-You-Code/NYC5-Todo-Parsing?utm_source=