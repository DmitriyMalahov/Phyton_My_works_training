
# 1. Дан список чисел. Определите, сколько в нем встречается различных чисел.

# [1, 1, 2, 3, 4, 4] 

# -> 4

my_list = [1, 1, 2, 3, 4, 4] 
my_set = set(my_list)

print(f'в списке {my_list} встречается различных чисел -> {len(my_set)}')

