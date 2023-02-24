# Задача 3.

# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым



                                                # Решение с перебором всех чисел до запрашиваемого.

def natural_number(num):
    for i in range(2, num//2 + 1):
        if num % i == 0:
            return False
    return True

n = int(input('Введите число: '))
print(natural_number(n))


