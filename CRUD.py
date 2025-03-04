# Import
from Function import indent, single_divider, double_divider, left_bar, screen_clear_func, printlst, \
     ins_ing, ins_updt, ins_re, sync_func
import Main_Menu

def CRUD_func():
    #Format printing
    print("")
    print(indent, "-"*28,"INGREDIENT MAINTENANCE","-"*28, "\n")
    double_divider(80)
    print(left_bar, f'{"Recipe":<22s}{"Unit":<22s}{"Quantity":<22s}{"|":>12}')
    single_divider(80)

    #Function that will print item from txt file
    printlst()
    double_divider(80)

    #Will loop until user enter Q
    print("")
    single_divider(80)
    print(indent, "<A>dd\t<M>od\t<Q>uit\t<S>yncFile  <R>eset >>", end="")
    command = input().upper()

    while command != "Q":

        print("")
        single_divider(80)
        print(indent, "Ingredient List Maintanence --->\n")

        if command == "A":

            ins_ing()

        elif command == "M":

            ins_updt()

        elif command == "R":

            ins_re()

        elif command == "S":

            sync_func()

        else:

            print(indent, "Invalid input. Please enter again...")

        print("")
        single_divider(80)
        print(indent, "<A>dd\t<M>od\t<Q>uit\t<S>yncFile  <R>eset >>", end="")
        command = input().upper()

    # Direct the user to main menu when Q is entered
    screen_clear_func()
    Main_Menu.main_menu_func()
