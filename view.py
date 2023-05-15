def add_new():
    name = input('Название: ')
    text = input('Текст заметки: ')
    return (name, text)


def find_note():
    return input('Введите название: ')


def edit_note():
    return input('Введите название: ')


def delete_note():
    return input('Введите название: ')

def date_chose_note():
    return input('Введите дату в формате дд.мм.гггг: ')


def nemu():
    return input('1 - Создать новую заметку\n'
                 '2 - Поиск заметки\n'
                 '3 - Показать все заметки\n'
                 '4 - Экспорт заметок в файл\n'
                 '5 - Показать заметки в файле\n'
                 '6 - Импортировать заметки из файла\n'
                 '7 - Редактировать заметку\n'
                 '8 - Удалить заметку\n'
                 '9 - Сделать выборку по дате\n'
                 '0 - Выход\n')


def view_res(res):
    print(f"{res}\n")
