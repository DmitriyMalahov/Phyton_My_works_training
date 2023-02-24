# 3. Напишите программу для печати всех уникальных значений в словаре.

# {
# 1: 'Vlad',
# 2: 'Vlad',
# 3: 'Oleg'
# }

# -> 2
dictionary = \
{
1: 'Vlad',
2: 'Vlad',
3: 'Oleg'
}

my_set = set()
for i in dictionary.values():
    my_set.add(i)

print(f'в словаре {dictionary} встречаются уникальные значения в количестве -> {len(my_set)}')