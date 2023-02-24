# Задача 1.

# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. 
# Пользователь вводит число N - количество элементов в первом массиве, затем N чисел - элементы массива. 
# Затем число M - количество элементов во втором массиве. Затем элементы второго массива

# Ввод:
# 7
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1

# Вывод:
# 3 3 2 12

def enter_elements_array(size_list: int) -> list:
    count = 1
    number_list = []
    for i in range(size_list):
        number = int(input(f'Введите число {count}: '))
        number_list.append(number)
        count += 1
    return number_list

def unique_arr_element(one_list, two_list: list) -> list:
    result_list = []
    for item in one_list:
        if item not in two_list:
            result_list.append(item)
    return result_list

size_list_one = int(input('Введите длину первого массива: '))
first_list = enter_elements_array(size_list_one)
size_list_two = int(input('Введите длину второго массива: '))
second_list = enter_elements_array(size_list_two)

result = unique_arr_element(first_list, second_list)

print(f'Элементы первого массива которые не встречаются нет во втором массиве: {(result)}')