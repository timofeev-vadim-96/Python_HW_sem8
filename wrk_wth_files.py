# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. Пользователь 
# также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных

def show_menu() -> int:
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Добавить абонента в справочник\n"
          "5. Сохранить справочник в текстовом формате\n"
          "6. Закончить работу")
    choice = int(input())
    return choice


def work_with_phonebook(file_name: str):
    choice = show_menu()
    phone_book = read_txt(file_name)
    while choice != 6:
        if choice == 6: 'жопа!'
        if choice == 1:
            print(*phone_book, sep = '\n')
            choice = show_menu()
        elif choice == 2:
            name = input('Введите фамилию: ')
            print(find_by_name(phone_book, name))
            choice = show_menu()
        elif choice == 3:
            number = input('Введите номер телефона: ')
            print(find_by_number(phone_book, number))
            choice = show_menu()
        elif choice == 4:
            user_data = get_new_user()
            phone_book.append(user_data)
            append_txt(file_name, user_data)
            choice = show_menu()
        elif choice == 5:
            file_name = input('Введите имя файла (без расширения): ') + '.txt'
            write_txt(file_name, phone_book)
            choice = show_menu()
        elif choice not in [1,2,3,4,5,6]: 
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
    
def find_by_name(input_phone_book: dict, name):
    for i in input_phone_book:
        if name in i.values():
            return i 
    return 'Абонент не найден.' # если дошли сюда, то не ретерн не произведен и пользователь не найден

def find_by_number(input_phone_book, number):
    for i in input_phone_book:
        if number in i.values():
            return i 
    return 'Абонент с таким номером не найден.'

def get_new_user():
    new_data = ''
    new_data+=(input('Введите фамилию: ')) + ','
    new_data+=(input('Введите имя: ')) + ','
    new_data+=(input('Введите номер телефона: ')) + ','
    new_data+=(input('Введите описание: '))
    return new_data

def append_txt(file_name: str, user_data: dict):
    with open(file_name, 'a', encoding='utf-8') as data:
        data.writelines(user_data + '\n')

def write_txt(file_name: str, input_phone_book: dict):
    with open(file_name, 'w', encoding='utf-8') as data:
        for i in input_phone_book:
            data_list = []
            data_str = ''
            for value in i.values():
                data_list.append(value) # формируем список из values 
            data_str = ','.join(data_list)# конвертируем его в строку
            data.writelines(data_str + '\n') #добавляем в файл


work_with_phonebook('phon.txt')

