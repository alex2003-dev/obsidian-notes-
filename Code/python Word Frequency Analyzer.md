text = input("Enter text: ")

text = text.lower()

text = text.replace('.', ' ')

text = text.replace(',', ' ')

text = text.replace('!', ' ')

text = text.replace('?', ' ')

stop_words = ["and", "the", "is", "in", "at", "to", "a", "of", "on", "for", "it", "with", "as", "was", "but"]

words = text.split()

word_counts = {}

for word in words:

    if word not in stop_words:

        if word in word_counts:

            word_counts[word] = word_counts[word] + 1

        else:

            word_counts[word] = 1

word_items = list(word_counts.items())

for i in range(len(word_items)):

    for j in range(i + 1, len(word_items)):

        if word_items[j][1] > word_items[i][1]:

            temp = word_items[i]

            word_items[i] = word_items[j]

            word_items[j] = temp

print("Top 10 words:")

count = 0

for item in word_items:

    print(item[0], ":", item[1])

    count = count + 1

    if count == 10:

        break

1. text = input("Enter text: ") - говорит пользователю ввести текст
2. text = text.lower() - делает слова все в нижний регистр то есть маленькими. Это нужно для того чтобы сравнение слов не относилось к регистру 
3. text = text.replace('.', ' ')
   text = text.replace(',', ' ')
   text = text.replace('!', ' ')
   text = text.replace('?', ' ') - знаки превращает в пробелы для корректного разбиения текста
4. stop_words = ["and", "the", "is", "in", "at", "to", "a", "of", "on", "for", "it", "with", "as", "was" "but"] - артикли, глаголы и вспомогательные  слова которые закидываем в понятие стоп-слов чтобы они не засчитывались 
5. words = text.split() -  делит текст на отдельные слова, используя пробелы как разделители.
6. word_counts = {} - создаёт пустой словарь
7. for word in words:
    if word not in stop_words:
        if word in word_counts:
            word_counts[word] = word_counts[word] + 1
        else:
            word_counts[word] = 1 - фрагмент кода который реализует логику то есть если слово не является стоп-слово то....
            если слово уже было то счётчик прибавится на +1 
   И добавляет слово в словарь +1 
8. word_items = list(word_counts.items()) - для сортировки 
9. for i in range(len(word_items)):
    for j in range(i + 1, len(word_items)):
        if word_items[j][1] > word_items[i][1]:
            temp = word_items[i]
            word_items[i] = word_items[j]
            word_items[j] = temp  - сортирует список по убыванию 
10. print("Top 10 words:")
count = 0
for item in word_items:
    print(item[0], ":", item[1])
    count = count + 1
    if count == 10:
        break - выводит первые 10 частых слов. Цикл прерывается после 10-ти слов. 


