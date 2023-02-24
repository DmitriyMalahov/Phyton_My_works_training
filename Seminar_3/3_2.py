# 2. Дана последовательность из N целых чисел и число K.
# Необходимо сдвинуть всю последовательность (сдвиг - циклический) 
# на K элементов вправо, K – положительное число.

# staert_list = [1, 2, 3, 4, 5]
# k = 3

# -> [3, 4, 5, 1, 2]

start_list = [1, 2, 3, 4, 5]

k = int(input('Введите число K: '))
n = k % len(start_list)
temp_list = [0] * len(start_list)

for i in range(len(start_list)):
    if (i + n) >= len(start_list):
        temp_list[(i + n) - len(start_list)] = start_list[i]
    else:
        temp_list[(i + n)] = start_list[i]
        
print(temp_list) 

# k = 2
# start_list = [1, 2, 3, 4]
# new_list = []

# k = -(k%len(start_list))
# for i in start_list:
# new_list.append(start_list[k])
# k += 1

# print(new_list