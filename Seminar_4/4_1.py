# Задача 1. 

# Напишите программу, которая принимает на вход строку, и отслеживает,
# сколько раз каждый символ уже встречался.

# 'Hello, World!'

# H: 1
# e: 1
# l: 3
# o: 2
# W: 1
# ' ': 1
# ,: 1
# r: 1
# d: 1
# !: 1

start_line = 'Hello, World!'

result_dict = {}
temp_set = set(start_line)

for letter in temp_set:
    count_letter = 0
    for letter_in_word in start_line:
        if letter == letter_in_word:
            count_letter += 1
    result_dict[letter] = count_letter

print(result_dict)

                           # Решение 2

text = input('Введите текст: ')  # Решение через встроеную функцию get для словарей
d = {}
for i in text:
   d[i] = d.get(i,0)+1
print(d)
