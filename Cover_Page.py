# Import
import datetime
from Function import left_bar, indent, single_divider, double_divider, quit_func, screen_clear_func
import Main_Menu

# Title & welcoming line
print("")
print(indent, " ____      __   _   _          _                        ")
print(indent, "|  _ \    /_/  | | (_)   ___  (_)   ___   _   _  __  __ ")
print(indent, "| | | |  / _ \ | | | |  / __| | |  / _ \ | | | | \ \/ / ")
print(indent, "| |_| | |  __/ | | | | | (__  | | |  __/ | |_| |  >  <  ")
print(indent, "|____/   \___| |_| |_|  \___| |_|  \___|  \__,_| /_/\_\ ")
print("")
print(indent, " ____            _                                      ")
print(indent, "| __ )    __ _  | | __   ___   _ __   _   _             ")
print(indent, "|  _ \   / _` | | |/ /  / _ \ | '__| | | | |            ")
print(indent, "| |_) | | (_| | |   <  |  __/ | |    | |_| |            ")
print(indent, "|____/   \__,_| |_|\_\  \___| |_|     \__, |            ")
print(indent, "                                      |___/             ")
print("\n"*3)
print(indent, "Welcome to Délicieux Bakery Material Planning System\n")


# Calculate datetime
date_time = datetime.datetime.now()  # Get the current datetime
current_year = date_time.year
current_month = date_time.strftime("%B")  # Get the full name of the current month
current_day = date_time.day
current_hour = date_time.strftime("%I")
current_minute = date_time.strftime("%M")
current_weekday = date_time.strftime("%A")  # Get the full name of the current day
current_time = date_time.strftime("%p")  # Indicate PM or AM


# Print datetime
double_divider(53)
print(left_bar, f"{'Current datetime': ^50}{'|': >1}")
single_divider(53)
print(left_bar, f"{'Date: %2d %s %s' %(current_day, current_month, current_year): ^50}{'|': >1}")
print(left_bar, f"{'Time: %s:%s %s' %(current_hour, current_minute, current_time): ^50}{'|': >1}")
print(left_bar, f"{current_weekday: ^50}{'|': >1}")
double_divider(53)


# Key and description
print("")
double_divider(53)
print(left_bar, f"{'Key': ^10}{'|': >1}{'Description': ^39}{'|': >1}")
single_divider(53)
print(left_bar, f"{' P': <10}{'|': >1}{' Proceed to main menu': <39}{'|': >1}")
print(left_bar, f"{' E': <10}{'|': >1}{' Exit the program': <39}{'|': >1}")
double_divider(53)


# User's input
print("")
print(indent, "Enter a key to continue")
user_input = str(input("\t\t\t\t\t >> ")).upper()


# Error when entering other key
while user_input != "P" and user_input != "E":  # Display error message when invalid key is entered

    single_divider(53)
    print(indent, "Invalid key entered, please try again")
    print(indent, "Press any key to continue...", end="")
    input_again = str(input())

    single_divider(53)
    print(indent, "Enter a key to continue")
    user_input = str(input("\t\t\t\t\t >> ")).upper()


#  Evaluate the user's input
if user_input == "E":

    quit_func()

else:

    screen_clear_func()
    Main_Menu.main_menu_func()



