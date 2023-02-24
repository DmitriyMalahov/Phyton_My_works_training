# Задача 3.

# Дан список чисел. 
# Посчитайте, сколько в нем пар элементов, равных друг другу. 
# Считается, что любые два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. 
# Вводится список чисел. Все числа списка находятся на разных строках.

# Ввод:

# 1 2 3 2 3 
# Вывод:
# 2

# Ввод:
# 1 1 2 3 1 2
# Вывод:
# 4


def enter_elements_array(size_list: int) -> list:
    count = 1
    number_list = []
    for i in range(size_list):
        number = int(input(f'Введите цифру № {count}: '))
        number_list.append(number)
        count += 1
    return number_list

def enter_elements_array_2(size_list: int) -> list:
    my_list = [int(input('Введите цифру: ')) for i in range(size_list)]
    return my_list

size_list = int(input('Введите длину списка чисел: '))
my_list = enter_elements_array(size_list)

count = 0
temp_list = my_list
for index_list in range(len(my_list)):
    for element_list in my_list[index_list+1:]:
        if element_list == my_list[index_list]:
            count += 1


print(f'Количество пар элементов списка, равных друг другу равно: {count}')

# Включения:

# my_list = ["что сделать" for "где взять" if "при каком условии" ] - for в оду строчку:
#  
# n = 4
# list_ = [1, 2, 5, 7, 2, 6]
# new_list = [item for item in list_ if item > 3]

# print(new_list)