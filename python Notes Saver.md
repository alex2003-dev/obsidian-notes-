def add(n): open("notes.txt", "a").write(n + "\n")

def list():

    try: print(*open("notes.txt"), sep="")

    except: print("No notes found.")

def search(k):

    try:

        f = [l for l in open("notes.txt") if k.lower() in l.lower()]

        print(*f if f else ["No matches found."], sep="")

    except: print("No notes found.")

add("Buy milk")

add("Read book")

list()

search("milk")


Разбор: 

1. def add(n): open("notes.txt", "a").write(n + "\n") - n текст заметки переменная которая принимается созданной нами функцией, далее  открывается и создаётся файл в режиме append, и в конце добавляется текст заметки и перевод строки в конец файла
2. def list(): - создаёт функцию `list()` которая покажет все заметки
3.  try: print(*open("notes.txt"), sep="") - выполняет команду, при нахождении ошибки обрабатывает её, далее открывается файл на чтении и распаковывается строки из файла 
4. except: print("No notes found.") - при отсутствии файла напишет команду no notes found 
5. def search(k): - функция поиска которая ищет букву k
6. try:

        f = [l for l in open("notes.txt") if k.lower() in l.lower()] - открывает файл, проходит по всем строкам l в файле, проверяет содержится ли k в l, сохраняет совпавшие строки в список `f`.
 7.  print(*f if f else ["No matches found."], sep="") - если f не пустой то выводит все строки из списка, если f пустой то выводит no matches found
 8.  except: print("No notes found.") - если файла нет то выдаёт ошибку 
 9. add("Buy milk")
    add("Read book")
    list()
    search("milk") - ищет слово молоко где оно встречается среди заметок

Источники: 

https://realpython.com/videos/list-comprehensions-overview/?utm_source=

https://www.youtube.com/watch?v=5K08WcjGV6c&ab_channel=CSDojo

https://pythonbasics.org/try-except/?utm_source=

https://www.geeksforgeeks.org/python/python-try-except/
