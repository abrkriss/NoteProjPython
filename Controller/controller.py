import InterfUSer.ConsoleUser as uc
import Controller.commands as com


def start():
    while True:
        uc.console()
        user_inf = input()
        if user_inf == '1':
            com.show("all")
        elif user_inf == '2':
            com.show("ID")
        elif user_inf == '3':
            com.show("date")
        elif user_inf == '4':
            com.show("all")
            com.change()
        elif user_inf == '5':
            com.add_note()
        elif user_inf == '6':
            com.show("all")
            com.delete()
        else:
            print("Program note is done")
            break
