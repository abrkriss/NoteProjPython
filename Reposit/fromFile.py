import Model.Note


def read():
    try:
        array = []
        file = open("notes.csv", "r", encoding='utf-8')
        notes = file.read().strip().split("\n")
        for n in notes:
            split_n = n.split(';')
            note = Model.Note.Note(
                id=split_n[0], title=split_n[1], full_text=split_n[2], date=split_n[3])
            array.append(note)
    except Exception:
        print("Notes is null")
    finally:
        return array


