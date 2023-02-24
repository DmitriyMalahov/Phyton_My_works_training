# Задача 2. 

# Хакер Василий получил доступ к классному журналу и хочет заменить все свои
# минимальные оценки на максимальные. 
# Напишите программу,
# которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.

# [4, 2, 2, 1, 5, 5]

def replacement(grades_list: list) -> list:
# def replacement(grades_list: list) -> list: (какой вид данных принимает и что возвращает функция)
    maximum = max(grades_list)
    minimum = min(grades_list)
    for i in range(len(grades_list)):
        if grades_list[i] == maximum:
            grades_list[i] = minimum
    return grades_list

grades = [4, 2, 2, 1, 5, 5]
result = replacement(grades)
print(result)


                            # Вариант 2 с изменением оценок 4 и 5 на минимальную.
# def replace_marks(marks_list: list) -> list: 
# # def replace_marks(marks_list: list) -> list: (какой вид данных принимает и что возвращает функция)
#     minimum = min(marks_list)
#     for i in range(len(marks_list)):
#         if (marks_list[i] == 5) or (marks_list[i] == 4):
#             marks_list[i] = minimum
#     return marks_list

# marks = [4, 2, 2, 1, 5, 5]
# print(replace_marks(marks))

