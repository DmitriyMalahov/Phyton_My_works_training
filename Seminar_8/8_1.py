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
          data.writelines(add_element)

def exit_program():
    data = open('phone_book.txt', 'r', encoding='utf8')
    data.close()

