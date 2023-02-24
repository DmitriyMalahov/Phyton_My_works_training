# Задача 3.

# Ваня и Петя поспорили, кто быстрее решит следующую задачу:
# “Задана последовательность неотрицательных целых чисел.
# Требуется определить значение наибольшего элемента последовательности,
# которая завершается первым встретившимся нулем (число 0 не входит в последовательность)”.
# Однако 2 друга оказались не такими смышлеными. Никто из ребят не смог до конца сделать это задание.
# Они решили так: у кого будет меньше ошибок в коде, тот и выиграл спор.
# За помощью товарищи обратились к Вам, студентам.

# 2
# 4
# 6
# 2
# 8
# 0

# -> 8

                        # Моё решение
 
# number = int(input("Введите неотрицательное число: "))
# number_list = [number]

# while number != 0:
#     number = int(input("Введите неотрицательное число: "))
#     if number != 0:
#         number_list.append(number)

# temp_set = set(number_list)
# max_number = 0

# for i in temp_set:
#     if i > max_number:
#         max_number = i
#         i += 1

# print(max_number)

                                         # Второе решение 

# number = int(input("Введите неотрицательное число: "))
# max_number = number
# while number != 0:
#     if number > max_number:
#         max_number = number
#     number = int(input("Введите неотрицательное число: "))
# print(max_number)

                                      # Третье решение

print('Вводим числа')
number = None
array = list()
while number != 0:
    number = int(input('Ведите число: '))
    array.append(number)
print(f'Максимальное число в массиве - {max(array)}')