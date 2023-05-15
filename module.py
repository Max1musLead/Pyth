import csv
from datetime import datetime
import random
from Note import Note
notes = []
id = random.randint(0, 10000)
current_datetime = datetime.now()
notes_imp_from_file = False

def create(data):
    note = Note(data[0], data[1], current_datetime, id)
    notes.append(note)
    return 'Заметка созданa'

def imp():
    with open('notes.csv', 'r', encoding='utf-8') as data:
        lines = data.read().split('\n')
        for i in lines[0:-1]:
            member = i.split(';')
            note = Note(member[0], member[1], member[2], member[3])
            notes.append(note)
    return 'Заметки импортированы'

def find(name):
    finder = True
    for i in notes:
        if name == i.get_name():
            print(
                f'Название заметки: {i.get_name()}\n Текст заметки: {i.get_text()}\n Дата создания/редактирования: {i.get_date()}\n ID заметки: {i.get_id()}')
            finder = False
    if finder:
        print('Заметки с таким именем нет')

def edit_note(name):
    finder = True
    for i in notes:
        if name == i.get_name():
            print(
                f'Название заметки: {i.get_name()}\n Текст заметки: {i.get_text()}\n Дата создания/редактирования: {i.get_date()}\n ID заметки: {i.get_id()}')
            i.set_name(input('Введите новое название: '))
            i.set_text(input('Введите новый текст: '))
            i.set_date(current_datetime)
            finder = False
    if finder:
        print('Заметки с таким именем нет')

def delete_note(name):
    finder = True
    for i in notes:
        if name == i.get_name():
            notes.remove(i)
            finder = False
    if finder:
        print('Заметки с таким именем нет')

def san():
    if len(notes) != 0:
        for i in notes:
            print(
                f'Название заметки: {i.get_name()}\n Текст заметки: {i.get_text()}\n Дата создания/редактирования: {i.get_date()}\n ID заметки: {i.get_id()}\n-----')
        return 'Вот все заметки'
    else:
        return 'Заметки могут быть в файле'

def exp():
    with open('notes.csv', 'w', encoding='utf-8') as book:
            for i in notes:
                book.write(
                    f'{i.get_name()};{i.get_text()};{i.get_date()};{i.get_id()};\n')
    return 'Заметки записаны в файл'

def sanf():
    with open('notes.csv', encoding='utf-8') as data:
        file_reader = csv.reader(data, delimiter=";")
        for i in file_reader:
            with open('notes.csv', 'a'):
                print(
                    f'Название заметки: {i[0]}\n Текст заметки: {i[1]}\n Дата создания/редактирования: {i[2]}\n ID заметки: {i[3]}\n-----')
    return 'Вот все заметки в файле'

def date_choose(data):
    normal_data = data.split('.')
    if len(normal_data) >= 2:
        for i in notes:
            fi = i.get_date().split(' ')
            si = fi[0].split('-')
            if normal_data[2] == si[0] and normal_data[1] == si[1] and normal_data[0] == si[2]:
                print(
                f'Название заметки: {i.get_name()}\n Текст заметки: {i.get_text()}\n Дата создания/редактирования: {i.get_date()}\n ID заметки: {i.get_id()}\n-----')
        return 'Вот все заметки'
    else:
        return 'Неправильная дата'
