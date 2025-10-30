contacts = {}

def is_valid(name, phone):

    return name.strip() and phone.strip().replace('+', '').replace('-', '').isdigit()

def add_contact():

    name = input("Name: ").strip()

    phone = input("Phone: ").strip()

    if is_valid(name, phone):

        contacts[name] = phone

        print("Contact added.")

    else:

        print("Invalid name or phone.")

def search_contact():

    name = input("Name to search: ").strip()

    print(contacts.get(name, "Contact not found"))

def delete_contact():

    name = input("Name to delete: ").strip()

    print(contacts.pop(name, "Contact not found"))

def list_contacts():

    if not contacts:

        print("No contacts.")

    else:

        for name in sorted(contacts):

            print(f"{name}: {contacts[name]}")

def menu():

    while True:

        print("\n1 - Add, 2 - Search, 3 - Delete, 4 - List, 0 - Exit")

        choice = input("Choose: ").strip()  

        if choice == '1':

            add_contact()

        elif choice == '2':

            search_contact()

        elif choice == '3':

            delete_contact()

        elif choice == '4':

            list_contacts()

        elif choice == '0':

            break

        else:

            print("Wrong choice.")

menu()


1. contacts = {} - словарь с обозначением что он пустой 
2. def is_valid(name, phone): - имя функции и объявление функции, в скобках параметры функции 
3. return name.strip() and phone.strip().replace('+', '').replace('-', '').isdigit() - удаляем пробелы, убираем знаки + -, проверяем чтобы строка было только из цифр, возвращаем результат
4. def add_contact(): - функция добавления контактов 
5.      name = input("Name: ").strip() - просьба ввести имя и чтобы убрать ошибки из-за пробела добавляем .strip()
6.     phone = input("Phone: ").strip() - так же просим ввести номер 
7.     if is_valid(name, phone): - если номер телефона и имя правильные то
8.     contacts[name] = phone - ключ имя значение телефон 
9.     print("Contact added.") - отображение что телефон добавлен
10.      else:
        print("Invalid name or phone.") - ошибка если телефон или имя не прошли проверку 
11.  def search_contact(): - функция чтобы найти контакт
12.  name = input("Name to search: ").strip() - спрашиваем имя 
13.  print(contacts.get(name, "Contact not found")) - поиск по имени, если имя не найдено выводим сообщение 
14. def delete_contact(): - функция для удаления контакта 
15.     name = input("Name to delete: ").strip() - запрос на имя 
16.     print(contacts.pop(name, "Contact not found")) - удаляет контакт с именем, если такого имени нету то вывод фразы 
17. def list_contacts(): - функция показа всех контактов 
18.     if not contacts:
        print("No contacts.") - если в словаре контактов нет, то вывод текста 
19.     else:
        for name in sorted(contacts): - если контакт есть то сортируем имена в алфавитном порядке 
20.             print(f"{name}: {contacts[name]}") - вывод имени и номера
21.  def menu(): - функция меню программы 
22.     while True: - повторение
23.         print("\n1 - Add, 2 - Search, 3 - Delete, 4 - List, 0 - Exit") - вывод меню
24.         choice = input("Choose: ").strip() - выбор действия 
25.          if choice == '1':
            add_contact()
        elif choice == '2':
            search_contact()
        elif choice == '3':
            delete_contact()
        elif choice == '4':
            list_contacts()
        elif choice == '0':
            break
        else:
            print("Wrong choice.") - в зависимости от выбора назначенные действия 















