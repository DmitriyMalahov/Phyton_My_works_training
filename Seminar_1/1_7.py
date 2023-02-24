# 7. Дано натуральное число. 
# Требуется определить, является ли год с данным номером високосным. 
# Если год является високосным, то выведите YES, иначе выведите NO. 
# Напомним, что в соответствии с григорианским календарем, год является високосным, 
# если его номер кратен 4, но не кратен 100, а также если он кратен 400.

# **Input:**

# 2016

# **Output:**

# YES

# year = int(input('--> '))
# if ((year%4 == 0) and (year%100 != 0)) or (year%400 == 0):
#     print('YES')
# else:
#     print('NO')

# year = int(input('--> '))
# result = 'NO'
# if ((year%4 == 0) and (year%100 != 0)) or (year%400 == 0):
#    result = 'YES'
# print(result)

year = int(input('--> '))
result = 'YES' if ((year%4 == 0) and (year%100 != 0)) or (year%400 == 0) else 'NO'
print(result)

# print('YES' if (year:=int(input('--> '))%400 == 0) else 'NO') # моржовый оператор.

