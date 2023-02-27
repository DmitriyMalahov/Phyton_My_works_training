# Создать телефонный справочник с возможностью импорта
# и экспорта данных в формате .txt. Фамилия, имя, отчестово,
# номер телефона - данные, которые должны находится в файле.

# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле.
# 3. Пользователь может ввести одну из характеристик для поиска
# определенной записи(Например имя или фамилию человека).
# 4. Использование функций. Ваша программа не должна быть линейной.

# 1. Вывод всех контактов
# 2. Поиск контактов
# 3. Добавить контакт (сразу сохранить)
# 4. Выход по требованию пользователя


def print_all_contacts():
    with open('phone_book.txt', 'r', encoding='utf8') as data:
        for line in data:
            print(line)

def find_contact(find_element):
        with open('phone_book.txt', 'r', encoding='utf8') as data:
            for line in data:
                if find_element in line:
                    print(line)

def add_contact(add_element):
     with open('phone_book.txt', 'a', encoding='utf8') as data:
          data.write(add_element +'\n')

def exit_program():
    data = open('phone_book.txt', 'r', encoding='utf8')
    data.close()

def main_menu(numb):
    if numb == 1:
        print_all_contacts()
    elif numb == 2:
        find_element = input('Введите Ф.И.О. либо номер телефона для поиска: ')
        find_contact(find_element)
    elif numb == 3:
        add_element = input('Введите Ф.И.О. и номер телефона через пробел: ')
        add_contact(add_element)
    elif numb == 4:
        exit_program()

numb = int(input('Введите:\n 1 - для печати всех контактов;\n 2 - для поиска контакта;\n\
 3 - для добавления нового контакта в справочник;\n 4 - для выхода из программы:  '))
main_menu(numb)



# add_contact('Николай Котов +78651790625')
# print_all_contacts()
# find_contact('Котов')


