# Задача 1. 

# Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где

# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).

# Требуется найти N-е число Фибоначчи

def fibonacci(n):
    if n == 0:
        return 0
    elif n in [1,2]:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

n = int(input('Введите число N: '))
fib_num = fibonacci(n)
print(f'Число Фибоначчи равно: {fib_num}')