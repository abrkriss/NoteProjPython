from datetime import datetime
import uuid
import Controller.counter as counter


class Note:
    def __init__(self, id=str(counter.counter()), title="text", full_text="text",
                 date=str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))):
        self.id = id
        self.title = title
        self.full_text = full_text
        self.date = date

    def get_id(note):
        return note.id

    def get_title(note):
        return note.title

    def get_fullText(note):
        return note.full_text

    def get_date(note):
        return note.date

    def set_id(note):
        note.id = str(counter.counter())

    def set_title(note):
        note.title = note

    def fullText(note):
        note.full_text = note

    def set_date(note):
        note.date = str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))

    def to_string(note):
        return note.id + ';' + note.title + ';' + note.full_text + ';' + note.date

    def map_note(note):
        return '\nID: ' + note.id + '\n' + 'Name: ' + note.title + '\n' + 'Description:' + note.full_text + '\n' + \
            'Publication date: ' + note.date
