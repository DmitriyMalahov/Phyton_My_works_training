# 1. Уставшие от необычно теплой зимы, жители решили узнать,
# действительно ли это самая длинная оттепель за всю историю наблюдений за погодой.
# Они обратились к синоптикам, а те, в свою очередь, занялись исследованиями статистики
# за прошлые годы. Их интересует, сколько дней длилась самая длинная оттепель.
# Оттепелью они называют период, в который среднесуточная температура ежедневно превышала 0 градусов
# Цельсия. Напишите программу, помогающую синоптикам в работе.

# Пользователь вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 100).
# В следующих строках располагается N целых чисел.

# Каждое число – среднесуточная температура в соответствующий день.
# Температуры – целые числа и лежат в диапазоне от –50 до 50

# *input*
# 6
# 1
# 3
# -5
# 0
# -1
# 7

# *output*
# -> 2


# days = int(input('Введите количество дней от 1 до 100: '))
# count = 0
# max_count = 0
# for i in range(days):
#     temp = int(input('Введите значение темперетвруры от -50 до 50: '))
#     if temp > 0:
#         count += 1
#     else:
#         if count > max_count:
#             max_count = count
#             count = 0
# print(f'Самая длинная оттепель длилась дней: {max_count}')


                    # len() -> возвращает количество элементов в коллекци
                    # range(5) -> 0, 1, 2, 3, 4
                    # range(5, 11) -> 5, 6, 7, 8, 9, 10
                    # range(1, 11, 2) -> 1, 3, 5, 7, 9

days = int(input('Введите количество дней от 1 до 100: '))
days_list = []

for i in range(days):
    temp = int(input('Введите значение темперетвруры от -50 до 50: '))
    days_list.append(temp)

count = 0
max_count = 0

for i in range(len(days_list)):
    if days_list[i] > 0:
        count += 1
    else:
        if count > max_count:
            max_count = count
            count = 0
            
print(f'Самая длинная оттепель длилась дней: {max_count}')


# num_in_str = '2 2 2 2 3 1'
# print(num_in_str.split(' '))