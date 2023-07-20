import Reposit.fromFile as fF
import Reposit.toFile as tF
import Model.Note


def add_note():
    title = input("Add name notes\n")
    full_text = input("Add description\n")
    note = Model.Note.Note(title=title, full_text=full_text)
    array_notes = fF.read()
    for i in array_notes:
        if Model.Note.Note.get_id(note) == Model.Note.Note.get_id(i):
            Model.Note.Note.set_id(note)
    array_notes.append(note)
    tF.write(array_notes, 'a')
    print("Note is done")


def show(txt):
    array_notes = fF.read()

    if array_notes:
        if txt == "all":
            print("NOTES")
            for i in array_notes:
                print(Model.Note.Note.map_note(i))

        elif txt == "ID":
            for i in array_notes:
                print("ID - ", Model.Note.Note.get_id(i))
            id = input("\nEnter id number")
            flag = True
            for i in array_notes:
                if id == (Model.Note.Note.get_id(i)):
                    print(Model.Note.Note.map_note(i))
                    flag = False
            if flag:
                print("ID not found")

        elif txt == "date":
            date = input("Enter date (day.month.year): ")
            flag = True
            for i in array_notes:
                date_note = str(Model.Note.Note.get_date(i))
                if date == date_note[:10]:
                    print(Model.Note.Note.map_note(i))
                    flag = False
            if flag:
                print("Date not found")
        else:
            print("Note is null")


def delete():
    id = input("Enter note id for delete: ")
    array_notes = fF.read()
    flag = False

    for i in array_notes:
        if id==Model.Note.Note.get_id(i):
            array_notes.remove(i)
            flag = True

        if flag:
            tF.write(array_notes, 'a')
            print("Delete is done ", id)
        else:
            print("id not found")


def change():
    id = input("Enter note id for change: ")
    array_notes = fF.read()
    flag = True
    array_notes_new = []
    for i in array_notes:
        if id == Model.Note.Note.get_id(i):
            i.title = input("Enter title to change\n")
            i.full_text = input("Enter description to change\n")
            Model.Note.Note.set_date(i)
            logic = False
            array_notes_new.append(i)

    if flag:
        tF.write(array_notes_new, 'a')
        print("Change is done for note id ", id)
    else:
        print("Id not found")
