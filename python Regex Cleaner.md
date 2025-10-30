Code: 

import re

  

text = "Hello,,, this is my email: test.email@@gmail.com!! Call me at +1 (234) - 567 - 8900..."

  

text = re.sub(r'[ ]+', ' ', text)

text = re.sub(r'[,!?.]{2,}', '.', text)

text = re.sub(r'\s*@+\s*', '@', text)

text = re.sub(r'\s*\.\s*', '.', text)

text = re.sub(r'\+?\s*\(?(\d{1,3})\)?[\s\-]*(\d{3})[\s\-]*(\d{3})[\s\-]*(\d{2,4})', r'+\1\2\3\4', text)

  

print(text)


Разбор:

1. import re - своего рода поиск по шаблонам, заданное действие = результат 
2. text = "Hello,,,   this   is   my email:   test.email@@gmail.com!!  Call   me at +1 (234) - 567 - 8900..." - пример текста 
3. text = re.sub(r'[ ]+', ' ', text) - поиск нескольких пробелов заменяя их на один 
4. text = re.sub(r'[,!?.]{2,}', '.', text) - поиск нескольких знаков препинания заменяя на одну точку
5. text = re.sub(r'\s*@+\s*', '@', text) - поиск лишних собачек и пробелов 
6. text = re.sub(r'\s*\.\s*', '.', text) - убирает проблемы вокруг точек
7. text = re.sub(r'\+?\s*\(?(\d{1,3})\)?[\s\-]*(\d{3})[\s\-]*(\d{3})[\s\-]*(\d{2,4})', r'+\1\2\3\4', text) - пишет в адекватном виде номер телефона
8. print(text) - показ очищенного текста

