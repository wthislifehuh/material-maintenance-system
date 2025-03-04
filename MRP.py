# Import
from Function import mrp, indent, screen_clear_func
import Main_Menu
import sys

def MRP_func():
    # Material Requirement Plan
    mrp()

    # Continue to choose
    print("")
    print(indent, "<S>ave to file\t\t<Q>uit\t>>", end="")
    choice = str(input()).upper()
    truth = 0

    # Data validation
    while truth != 1:  # Loop when invalid key is entered

        if choice == "S":

            stdoutOrigin = sys.stdout
            sys.stdout = open("MRP.txt", "w")
            mrp()
            sys.stdout.close()
            sys.stdout = stdoutOrigin
            print("")
            print(indent, "Successfully saved...")
            print(indent, "Press any key to quit...", end="")
            con = str(input())

            screen_clear_func()
            mainmenu()

            truth = 1

        elif choice == "Q":

            truth = 1
            screen_clear_func()
            Main_Menu.main_menu_func()

        else:

            print("")
            print(indent, "Invalid input. Please enter again.")
            truth = 2
            print(indent, "<S>ave to file\t\t<Q>uit\t>>", end="")
            choice = str(input()).upper()
