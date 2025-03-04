# Import
from Function import indent, left_bar, single_divider, double_divider, recipe_printing, screen_clear_func, \
     menu_print, recipe_addition, recipe_modification, recipe_deletion, sync_func, recipe_reset
import Main_Menu


def maintain_recipe_func():
    # Heading
    print("")
    print(indent, "-"*30,"RECIPE MAINTENANCE","-"*30, "\n")

    menu_print()

    double_divider(80)

    recipe_printing()

    print("")
    single_divider(80)
    print(indent, "<A>dd <M>od <D>el <Q>uit <S>yncFile <R>esetFile >>", end="")
    command = str(input()).upper()


    while command != "Q":

        if command == "A":

             recipe_addition()

        elif command == "M":

             recipe_modification()

        elif command == "D":

            recipe_deletion()

        elif command == "S":

            sync_func()

        elif command == "R":

            recipe_reset()

        else:

            print(indent, "Invalid input. Please enter again.")

        print("")
        single_divider(80)
        print(indent, "<A>dd <M>od <D>el <Q>uit <S>yncFile <R>esetFile >>", end="")
        command = str(input()).upper()

    # Direct the user to main menu when Q is entered
    screen_clear_func()
    Main_Menu.main_menu_func()