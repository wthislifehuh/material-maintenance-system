# Import
from Function import indent, single_divider, double_divider, screen_clear_func, menu_print, sync_func, order_print, \
     order_addition, order_modification, order_deletion, order_reset
import Main_Menu


def order_creation_func():
    print("")
    print(indent, f'{"-"*32}{" ORDER CREATION "}{"-"*32}', "\n")

    menu_print()

    order_print()

    print("")
    single_divider(80)
    print(indent, "<A>dd <M>od <D>el <Q>uit <S>yncFile <R>esetFile >>", end="")
    command = input().upper()

    while command != "Q":

        if command == "A":

            order_addition()

        elif command == "M":

            order_modification()

        elif command == "D":

            order_deletion()

        elif command == "S":

            sync_func()

        elif command == "R":

            order_reset()

        else:

            print(indent, "Invalid input. Please enter again.")

        print("")
        single_divider(80)
        print(indent, "<A>dd <M>od <D>el <Q>uit <S>yncFile <R>esetFile >>", end="")
        command = input().upper()

    # Direct the user to main menu when Q is entered
    screen_clear_func()
    Main_Menu.main_menu_func()