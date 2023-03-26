# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. Пользователь 
# также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных

# def show_menu() -> int:
#     print("\nВыберите необходимое действие:\n"
#           "1. Отобразить весь справочник\n"
#           "2. Найти абонента по фамилии\n"
#           "3. Найти абонента по номеру телефона\n"
#           "4. Добавить абонента в справочник\n"
#           "5. Сохранить справочник в текстовом формате\n"
#           "6. Закончить работу")


# choice = int(input())
# # return choice


# def work_with_phonebook():
#     choice = show_menu()
#     phone_book = read_csv('phonebook.csv')


# while (choice != 6):
#     if choice == 1:
#         print_result(phone_book)
#     elif choice == 2:
#         name = get_search_name()
#         print(find_by_name(phone_book, name))
#     elif choice == 3:
#         number = get_search_number()
#         print(find_by_number(phone_book, number))
#     elif choice == 4:
#         user_data = get_new_user()
#         add_user(phone_book, user_data)
#         write_csv('phonebook.csv', phone_book)
#     elif choice == 5:
#         file_name = get_file_name()
#         write_txt(file_name, phone_book)
#     choice = show_menu()

def read_csv(filename: str) -> list:
    data = []
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    with open(filename, 'r', encoding='utf-8') as fin: # utf-8 - для корректного чтения русских символов
        for line in fin:
            record = dict(zip(fields, line.strip().split(',')))
            data.append(record)
    print(*data, sep = '\n')
read_csv('phon.txt')
