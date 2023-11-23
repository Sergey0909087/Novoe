# Task
# 1. Найти индексы символов "!?."
# 2. Сформировать список из предложений
# с помощью найденных индексов и срезов
# 3. Применить к каждому эелементу
# получившимся списке метод capitalize()
# если есть лишник пробелы, применим strip()
# 4. Собрать строку из списка

import string

text = str(input("Введи текст: "))
indexes = 0
vosclic = '!'
koli_vosclick = 0
print(text.title())

digits = 0
for i in range(len(text)):
    if (text[i].isdigit()) == True:
        digits += 1
print('количество цифр - ', digits)

for i in text:
    if i in string.punctuation:
        indexes += 1        
print('количество пунктуационных символов - ', indexes)

for i in text:
    if i == vosclic:
        koli_vosclick += 1
print('количество восклицательных - ', koli_vosclick)

# Task 6
# a = [1 , 2, 3, 4, 5, 6]
# for i in a:
#     if i % 2 == 1:
#         a.remove(i)
# print(a)
# for i in range(len(a)):
#     a[i] = a[i] // 2
# print(a)

# a = []
# for i in range(5):
#     a.append(int(input()))
# print(a)

# a = [int(input()) for i in range(5)]
# print(a)