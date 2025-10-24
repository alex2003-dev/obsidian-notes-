folder test14.py 
text document: teest14 and names

teest14:       

import csv

def read_grades(filename):

    grades = []

    try:

        with open(filename, newline='', encoding='utf-8') as csvfile:

            reader = csv.reader(csvfile)

            next(reader)  

            for row in reader:

                print("Read row:", row)

                if len(row) < 2:

                    print("Skipped row (not enough columns):", row)

                    continue

                try:

                    grade = float(row[1])

                    grades.append(grade)

                except ValueError:

                    print("Skipped row (not a number):", row)

    except FileNotFoundError:

        print("File not found:", filename)

    return grades


file = 'names.csv'

grades = read_grades(file)

print("Grades collected:", grades)


names: 

Имена,Оценка
Саша,22
Женя,36
Ваня,90
Ирина,20

Разбор документа teest14: 
1. import csv - импортирует модуль csv, который позволяет удобно работать с cvs-файлами
2. def read_grades(filename): -  функция read_grades, которая принимает один аргумент — filename
3.     grades = [] - пустой список куда в дальнейшем будут добавлены оценки
4.  try:
        with open(filename, newline='', encoding='utf-8') as csvfile: - try ловит ошибки, потом открывается файл для чтения и предотвращение двойных пустых строк, далее кодировка файла и переменна которая ссылается на открытый файл.
5.    reader = csv.reader(csvfile)
            next(reader) - читает строки как списки и пропуск первой строки
6.   for row in reader:
                print("Read row:", row) - читает каждую строку как список значений
7.  if len(row) < 2:
                    print("Skipped row (not enough columns):", row)
                    continue - делает ограничение от двух строк иначе она не корректная, continue пропускает строку и двигается далее
8.    try:
                    grade = float(row[1])
                    grades.append(grade) - значение row преобразуем в float, если всё выходит получается grades 
9.  except ValueError:
                    print("Skipped row (not a number):", row) - ошибка что преображение не получается и вывод ошибки 
10.  except FileNotFoundError:
        print("File not found:", filename) - так же если файл не найден будет ошибка
11.  return grades - получается список только там где прошла оценка
12.  file = 'names.csv'
grades = read_grades(file) - называние файла с именами преображаем с read_grades
13. print("Grades collected:", grades) - финальный список всех оценок 

