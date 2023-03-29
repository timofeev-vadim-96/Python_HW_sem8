# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. Пользователь 
# также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных

def show_menu() -> int:
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Добавить абонента в справочник\n"
          "5. Удалить абонента из справочника\n"
          "6. Изменить номер телефона абонента\n"
          "7. Изменить описание абонента\n"
          "8. Сохранить справочник в текстовом формате\n"
          "9. Закончить работу")
    choice = int(input())
    return choice


def work_with_phonebook(file_name: str):
    choice = show_menu()
    phone_book = read_txt(file_name)
    while choice != 9:
        if choice == 1:
            print(*phone_book, sep = '\n')
            choice = show_menu()
        elif choice == 2:
            second_name = input('Введите фамилию: ')
            print(find_by_second_name(phone_book, second_name))
            choice = show_menu()
        elif choice == 3:
            number = input('Введите номер телефона: ')
            print(find_by_number(phone_book, number))
            choice = show_menu()
        elif choice == 4:
            user_data = get_new_user()
            phone_book.append(user_data)
            user_data = ','.join(list(user_data.values())) # конвертируем в строку для записи в справочник
            append_txt(file_name, user_data)
            choice = show_menu()
        elif choice == 5:
            second_name = input('Введите фамилию: ')
            print(del_by_name(phone_book, second_name))
            write_txt(file_name, phone_book)
            choice = show_menu()
        elif choice == 6:
            second_name = input('Введите фамилию: ')
            print(change_numb(second_name, phone_book))
            write_txt(file_name, phone_book)
            choice = show_menu()
        elif choice == 7:
            second_name = input('Введите фамилию: ')
            print(change_description(second_name, phone_book))
            write_txt(file_name, phone_book)
            choice = show_menu()
        elif choice == 8:
            file_name = input('Введите имя файла (без расширения): ') + '.txt'
            write_txt(file_name, phone_book)
            choice = show_menu()
        elif choice not in [1,2,3,4,5,6,7,8,9]: 
            print('Неверно введен вариант действия, повторите попытку: ')
            choice = show_menu()

def read_txt(filename: str) -> list: 
    data = []
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    with open(filename, 'r', encoding='utf-8') as fin: # utf-8 - для корректного чтения русских символов
        for line in fin:
            record = dict(zip(fields, line.strip().split(','))) #удаляет пробелы вначале и в конце строки, разбивает
            # ее на отдельные элементы, создает зип-список из пар кортежей, которые приводятся к словарю
            data.append(record)
        return data
    
def find_by_second_name(input_phone_book: dict, inp_second_name):
    for i in input_phone_book:
        if inp_second_name in i.values() and list(i.keys())[list(i.values()).index(inp_second_name)] == 'Фамилия':
            # 2 условие для того, чтобы введенное пользователем значение было именно Фамилией, а не именем.
            return i 
    return 'Абонент c такой фамилией не найден.' # если дошли сюда, то не ретерн не произведен и пользователь не найден

def del_by_name(input_phone_book: dict, inp_second_name):
    for i in range(len(input_phone_book)):
        if inp_second_name in input_phone_book[i].values() and \
            list(input_phone_book[i].keys())[list(input_phone_book[i].values()).index(inp_second_name)] == 'Фамилия':
            del input_phone_book[i]
            return 'Абонент с фамилией ' + inp_second_name + ' удален.'
    return 'Абонент c такой фамилией не найден.' # если дошли сюда, то не ретерн не произведен и 
    # пользователь не найден

def find_by_number(input_phone_book, number):
    for i in input_phone_book:
        if number in i.values(): #and list(i.keys())[list(i.values()).index(number)] == 'Телефон':
            return i 
    return 'Абонент с таким номером не найден.'

def get_new_user():
    new_data = []
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    new_data.append(input('Введите фамилию: '))
    new_data.append(input('Введите имя: '))
    new_data.append(input('Введите номер телефона: '))
    new_data.append(input('Введите описание: '))
    new_data = dict(zip(fields, new_data))
    return new_data

def append_txt(file_name: str, user_data: dict):
    with open(file_name, 'a', encoding='utf-8') as data:
        data.writelines(user_data + '\n')
        print()

def write_txt(file_name: str, input_phone_book: dict):
    with open(file_name, 'w', encoding='utf-8') as data:
        for i in input_phone_book:
            data_list = []
            data_str = ''
            for value in i.values():
                data_list.append(value) # формируем список из values 
            data_str = ','.join(data_list)# конвертируем его в строку
            data.writelines(data_str + '\n') #добавляем в файл

def change_numb(inp_second_name, inp_phone_book):
    for i in range(len(inp_second_name)):
        if inp_second_name in inp_phone_book[i].values() and \
        list(inp_phone_book[i].keys())[list(inp_phone_book[i].values()).index(inp_second_name)] == 'Фамилия':
            new_numb = input('Введите новый номер телефона: ')
            inp_phone_book[i]['Телефон'] = new_numb
            return 'Номер изменен.'
    return 'Абонент c такой фамилией не найден.' # если дошли сюда, то не ретерн не произведен и 
    # пользователь не найден

def change_description(inp_second_name, inp_phone_book):
    for i in range(len(inp_second_name)):
        if inp_second_name in inp_phone_book[i].values() and \
        list(inp_phone_book[i].keys())[list(inp_phone_book[i].values()).index(inp_second_name)] == 'Фамилия':
            new_numb = input('Введите новое описание: ')
            inp_phone_book[i]['Описание'] = new_numb
            return 'Описание изменено.'
    return 'Абонент c такой фамилией не найден.' # если дошли сюда, то не ретерн не произведен и 
    # пользователь не найден

work_with_phonebook('phon.txt')

