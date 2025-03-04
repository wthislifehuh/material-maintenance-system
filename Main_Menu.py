# Import
import datetime
from Function import left_bar, indent, single_divider, double_divider, screen_clear_func, quit_func
import CRUD
import Maintain_Recipe
import MRP
import Order_Creation

def main_menu_func():

    # Calculate datetime
    date_time = datetime.datetime.now()
    current_year = date_time.year
    current_month = date_time.strftime("%B")  # Get the full name of the current month
    current_day = date_time.day
    current_hour = date_time.strftime("%I")
    current_minute = date_time.strftime("%M")
    current_weekday = date_time.strftime("%A")  # Get the full name of the current day
    current_time = date_time.strftime("%p")  # Indicate PM or AM


    # Heading
    print("")
    double_divider(55)
    print(left_bar, f"{'Délicieux Bakery Material Planning System': ^52}{'|': >1}")
    single_divider(55)
    print(left_bar, f"{'Date: %2d %s %s' %(current_day, current_month, current_year): ^52}{'|': >1}")
    print(left_bar, f"{'Time: %s:%s %s' %(current_hour, current_minute, current_time): ^52}{'|': >1}")
    print(left_bar, f"{'Today is %s' %current_weekday: ^52}{'|': >1}")
    double_divider(55)


    # Key and description
    print("")
    double_divider(55)
    print(left_bar, f"{'Key': ^10}{'| ': >2}{'Description': ^39}{' |': >2}")
    single_divider(55)
    print(left_bar, f"{'I': <10}{'| ': >2}{'Ingredients maintenance': <39}{' |': >2}")
    print(left_bar, f"{'M': <10}{'| ': >2}{'Maintain recipes': <39}{' |': >2}")
    print(left_bar, f"{'C': <10}{'| ': >2}{'Create orders': <39}{' |': >2}")
    print(left_bar, f"{'G': <10}{'| ': >2}{'Generate material requirements plan': <39}{' |': >2}")
    print(left_bar, f"{'E': <10}{'| ': >2}{'Exit the program': <39}{' |': >2}")
    double_divider(55)


    # User's input
    print("")
    print(indent, "Enter a key to continue")
    user_input = str(input("\t\t\t\t\t >> ")).upper()


    # Validate the input
    key_list = ["I", "M", "C", "G", "E"]

    while user_input not in key_list:  # Display error message if invalid key is entered

        single_divider(55)
        print(indent, "Invalid key entered, please try again")
        print(indent, "Press any key to continue...", end="")
        input_again = str(input())

        single_divider(55)
        print(indent, "Enter a key to continue")
        user_input = str(input("\t\t\t\t\t >> ")).upper()


    # Direct the user to the desired function
    if user_input == "I":

        screen_clear_func()
        CRUD.CRUD_func()

    elif user_input == "M":

        screen_clear_func()
        Maintain_Recipe.maintain_recipe_func()

    elif user_input == "C":

        screen_clear_func()
        Order_Creation.order_creation_func()

    elif user_input == "G":

        screen_clear_func()
        MRP.MRP_func()

    else: # User's input is "E", exit the program

        quit_func()