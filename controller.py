import view
import module


def create_note():
    return module.create(view.add_new())


def find_note():
    return module.find(view.find_note())


def edit_note():
    return module.edit_note(view.edit_note())


def delete_note():
    return module.delete_note(view.delete_note())


def export_notes():
    return module.exp()


def show_all_notes():
    return module.san()


def show_all_notes_file():
    return module.sanf()


def improt_notes_from_file():
    return module.imp()

def dcn():
    return module.date_choose(view.date_chose_note())

def menu(data):
    if data == '0':
        show_res('До свидания')
    else:
        if data == '1':
            show_res(create_note())
        elif data == '2':
            show_res(find_note())
        elif data == '3':
            show_res(show_all_notes())
        elif data == '4':
            show_res(export_notes())
        elif data == '5':
            show_res(show_all_notes_file())
        elif data == '6':
            show_res(improt_notes_from_file())
        elif data == '7':
            show_res(edit_note())
        elif data == '8':
            show_res(delete_note())
        elif data == '9':
            show_res(dcn())
        else:
            show_res('Ошибка ввода')
        menu(view.nemu())


def show_res(data):
    view.view_res(data)
