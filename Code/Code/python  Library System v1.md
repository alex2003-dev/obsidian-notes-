папка: teest17.py


class Book:

    def __init__(self, title, author):

        self.title = title

        self.author = author
         
class Member:

    def __init__(self, name):

        self.name = name

class Library:

    def __init__(self):

        self.books = []

        self.members = []

    def add_book(self, book):

        for b in self.books:

            if b.title == book.title and b.author == book.author:

                return "Book exists"

        self.books.append(book)

    def remove_book(self, title, author):

        for b in self.books:

            if b.title == title and b.author == author:

                self.books.remove(b)

                return

    def find_book(self, title, author):

        for b in self.books:

            if b.title == title and b.author == author:

                return b

        return None

    def add_member(self, member):

        for m in self.members:

            if m.name == member.name:

                return "Member exists"

        self.members.append(member)

    def remove_member(self, name):

        for m in self.members:

            if m.name == name:

                self.members.remove(m)

                return

    def find_member(self, name):

        for m in self.members:

            if m.name == name:

                return m

        return None

print("Library system started")

Разбор: 
1.  class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author - 1 класс book - хранит информацию о книге, title название книги, author автор книги, init конструктор, задаёт свойства при создании объекта
2.  class Member:
    def __init__(self, name):
        self.name = name - 2 класс member - представляет читателя, name имя участника, init задаёт имя при создании объекта
3. class Library:
    def __init__(self):
        self.books = []
        self.members = [] - 3 класс library - управляет коллекциями книг и участников, books список объектов Book, members список объектов Member, init инициализирует пустые списки
4. def add_book(self, book):
    for b in self.books:
        if b.title == book.title and b.author == book.author:
            return "Book exists"
    self.books.append(book) - добавляет книгу, если такой нет, проверяет дубликат по названию и автору, если книга есть возвращает Book exists, если нет добавляет книгу в список
5. def remove_book(self, title, author):
    for b in self.books:
        if b.title == title and b.author == author:
            self.books.remove(b)
            return - удаляет книгу по названию и автору, перебирает список, если находит удаляет и выходит из метода, если книги нет ничего не происходит
6. def find_book(self, title, author):
    for b in self.books:
        if b.title == title and b.author == author:
            return b
    return None - ищет книгу по названию и автору, если находит возвращает объект книги, если не находит возвращает None
7. def add_member(self, member):
    for m in self.members:
        if m.name == member.name:
            return "Member exists"
    self.members.append(member) - добавляет участника, если такого ещё нет, проверяет дубликат по имени, если участник уже есть, возвращает Member exists, если нет добавляет участника.
8. def remove_member(self, name):
    for m in self.members:
        if m.name == name:
            self.members.remove(m)
            return - удаляет участника по имени, удаляет при совпадении
9.  def find_member(self, name):
    for m in self.members:
        if m.name == name:
            return m
    return None - ищет участника по имени, возвращает объект участника или None
10. print("Library system started") - вывод сообщения о том что код работает. 








