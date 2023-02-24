# Задача 4.

# Два различных натуральных числа n и m называются дружественными, 
# если сумма делителей числа n (включая 1, но исключая само n) равна числу m и наоборот. 
# Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных чисел, каждое из которых не превосходит k. 
# Программа получает на вход одно натуральное число k, не превосходящее 10 в 5 степени (100 000).  
# Программа должна вывести все пары дружественных чисел, каждое из которых не превосходит k. 
# Пары необходимо выводить по одной в строке, разделяя пробелами. 
# Каждая пара должна быть выведена только один раз (перестановка чисел новую пару не дает).

# Ввод:
# 300 

# Вывод:
# 284 200

# Список делителей для 220: 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 и 110, — их сумма равна 284.
# Список делителей для 284: 1, 2, 4, 71 и 142, — и сумма равна 220.

def div_num_sum(num: int) -> int:
    result_sum = 0
    for i in range(1, (num // 2) + 1):
        if num % i == 0:
            result_sum += i
    return result_sum

k = int(input('Введите число k: '))
result = []
for i in range(2, k + 1):
    div_num_i = div_num_sum(i)
    div_num_div = div_num_sum(div_num_i)
    duet = {i, div_num_i}
    if (i == div_num_div) and (i != div_num_i) and (duet not in result):
        result.append(duet)

print(*result)