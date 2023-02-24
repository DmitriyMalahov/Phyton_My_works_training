# Задача 2.

# Дан массив, состоящий из целых чисел.
# Напишите программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. 
# Сначала вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. 
# Массив состоит из целых чисел.

# Ввод:
# 5
# 1 2 3 4 5
# Вывод:
# 0

# Ввод:
# 5
# 1 5 1 5 1
# Вывод:
# 2

def enter_elements_array(size_list: int) -> list:
    count = 1
    number_list = []
    for i in range(size_list):
        number = int(input(f'Введите элемент массива № {count}: '))
        number_list.append(number)
        count += 1
    return number_list

size_list = int(input('Введите длину массива: '))
my_list = enter_elements_array(size_list)

count = 0
for i in range(1,(len(my_list)-1)):
    if my_list[i-1] < my_list[i] > my_list[i+1]:
        i +=1
        count +=1

print(f'Количество элементов массива,\
у которых два соседних элемента меньше данного равно: {count}')