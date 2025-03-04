# Import
import os
from time import sleep
import datetime

# Indentation
left_bar = "\t\t\t\t\t |"
indent = "\t\t\t\t\t"


# Divider
def single_divider(num):

    print("\t\t\t\t\t ", end="")
    print("-" * num)

def double_divider(num):

    print("\t\t\t\t\t ", end="")
    print("=" * num)


# Clear screen before switching to other program
def screen_clear_func():

    if os.name == 'posix':
        os.system('clear')  # for mac and linux

    else:

        os.system('cls')  # for windows platform


# Print "THANK YOU" when exiting, and stay for 3 seconds before closing the program
def quit_func():

    screen_clear_func()

    print("\n"*10)
    print("\t\t\t\t\t  _____   _   _      _      _   _   _  __ ")
    print("\t\t\t\t\t |_   _| | | | |    / \    | \ | | | |/ / ")
    print("\t\t\t\t\t   | |   | |_| |   / _ \   |  \| | | ' /  ")
    print("\t\t\t\t\t   | |   |  _  |  / ___ \  | |\  | | . \  ")
    print("\t\t\t\t\t   |_|   |_| |_| /_/   \_\ |_| \_| |_|\_\ ")
    print("")
    print("\t\t\t\t\t          __   __   ___    _   _          ")
    print("\t\t\t\t\t          \ \ / /  / _ \  | | | |         ")
    print("\t\t\t\t\t           \ V /  | | | | | | | |         ")
    print("\t\t\t\t\t            | |   | |_| | | |_| |         ")
    print("\t\t\t\t\t            |_|    \___/   \___/          ")

    sleep(3)  # Sleep and stay for 3 seconds after printing

#=======================================================================================================================
# INGREDIENT MAINTENANCE
def printlst():
    f = open("ingredient.txt", "r")

    # To take off the title
    f.seek(0)
    title = f.readline()
    ingredient = f.read()

    # Seperate data by spliting break line
    ingredient_list = ingredient.split("\n")
    ing_lst = list(filter(None, ingredient_list))
    name = []
    unit = []
    quantity = []

    # Loop to store 3 types of data separately
    for i in range(len(ing_lst)):
        r = ing_lst[i].split("|")
        name.append(r[0])
        unit.append(r[1])
        quantity.append(r[2])
        print(left_bar, f'{name[i]:<22s}{unit[i]:<22s}{quantity[i]:<22s}{"|":>12}')

    f.close()


# Add new data into file
def ins_ing():
    outfile = open("ingredient.txt", "a")
    print(indent, "Enter Ingredient \t>> ", end="")
    data = input()
    print(indent, "Enter Unit (g,ml,pcs)  >> ", end="")
    data1 = input()
    print(indent, "Enter Quantity \t>> ", end="")
    data2 = input()
    n_data = (data + "|" + data1 + "|" + data2 + "\n")  # the format of data in txt file
    print(indent, "Data successfully added...", "\n")  # Notification for the user
    outfile.write(n_data)
    outfile.close()


# Update data in txt file
def ins_updt():
    f1 = open("ingredient.txt", "r")
    f2 = open("ig.txt", "w")
    # to take off the title
    f1.seek(0)
    title = f1.readline()
    r = f1.read()
    r1 = r.split("\n")
    name = []
    # to get every ingredient available
    for i in range(len(r1)):
        o = r1[i].split("|")
        name.append(o[0])

    truth = True

    while truth != False:

        print(indent, "Enter which ingredient to update <Q>uit  >>", end="")
        updt = input()

        if updt == "Q" or updt == "q":

            truth = False

        elif updt not in name:  # if ingredient not available notified the user

            truth = True
            print(indent, "Ingredient not available...")

        else:  # if available run get item line by line

            x = ' '
            f1.seek(0)

            while (x):

                x = f1.readline()
                y = x.split("|")

                if int(len(x)) > 0:  # to make sure it's not empty

                    if y[0] == updt:  # if input is same as the data update else write the same

                        print(indent, "Enter new name for the ingredient >>", end="")
                        n_updt = input()
                        print(indent, "Enter new unit\t\t\t   >>", end="")
                        updt1 = input()
                        print(indent, "Enter new quantity\t\t   >>", end="")
                        updt2 = input()
                        f2.write(n_updt + "|" + updt1 + "|" + updt2 + "\n")
                        print(indent, "Data successfully updated...", "\n")

                    else:

                        f2.write(x)

                    truth = True

    f1.close()
    f2.close()
    os.remove("ingredient.txt")
    os.rename("ig.txt", "ingredient.txt")


def sync_func():  # Get data from another file

    while True:

        print("\n", indent, "Enter the file name in (xxx.txt)format >>", end="")
        x = input()
        quit = ""

        while quit != "YES":

            if x[-4:] == ".txt":

                print("\n", indent, "Syncing file ...")

                try:

                    with open(x) as f:

                        with open("recipe.txt", "w") as f1:
                            for line in f:
                                f1.write(line)

                    print("\n", indent, "The file has been successfully synced...")
                    break

                except:

                    print(indent, "There is no file named", x, ".Please enter again.")
                    print(indent, "Do you want to quit (yes/no) >>", end="")
                    quit = input().upper()

                    while quit != "NO" and quit != "YES":

                        print(indent, "Invalid Input. Please try again.")
                        print(indent, "Do you want to quit (yes/no) >>", end="")
                        quit = input().upper()

                    if quit != "YES":
                        break

            else:

                print(indent, "Invalid Input. Please try again.")
                print(indent, "Do you want to quit (yes/no) >>", end="")
                quit = input().upper()

                while quit != "NO" and quit != "YES":
                    print(indent, "Invalid Input. Please try again.")
                    print(indent, "Do you want to quit (yes/no) >>", end="")
                    quit = input().upper()

                if quit != "YES":
                    break

        else:

            break


def ins_re():  # delete everything inside the file

    with open("ingredient.txt", "w") as f:
        f.truncate()
        f.write("INGREDIENT" + "\n")

    print(indent, "Text file has been successfully reset...")

#=======================================================================================================================
# RECIPE MAINTENANCE
# To read from menu.txt and print menu to the screen for the reference of the user
def menu_print():

    with open("menu.txt", "r") as f:

        f.seek(0)
        title = f.readline()  # To move the cursor to the next line(after title)

        if title.endswith('\n'):

            title = title.rstrip('\n') # To remove the space line for printing

        # Print title
        double_divider(80)
        print(left_bar, f'{title:^77}{"|":>1}')
        double_divider(80)

        # Print title line
        print(left_bar, f'\t\t\t{"Recipe":<20s}{"Description":<28s}{"|":>9}')
        single_divider(80)

        # Read info from menu.txt
        read3 = f.read()
        read4 = read3.split("\n")
        recipe = list(filter(None, read4))
        listcode = []  # Recipe name in menu
        listname = []  # Recipe description in menu

        for i in range(len(recipe)):

            recipe_list = recipe[i].split("|")
            listcode.append(recipe_list[0])
            listname.append(recipe_list[1])
            print(left_bar, f'\t\t\t{listcode[i]:<20s}{listname[i]:<25s}{"|":>12}')


# RECIPE ADDITION PLAN
def recipe_addition():

    file = open("recipe.txt", "a+")
    file1 = open("menu.txt", "a+")
    file2 = open("ingredient.txt", "r")

    # Store info and name from menu.txt
    file1.seek(0)
    menu_list = []  # store recipe name/code
    name_list = []  # store recipe description
    title = file1.readline()    #to move cursor
    read1 = file1.read()
    read2 = read1.split("\n")
    listing = list(filter(None, read2))

    for r in range(len(listing)):

        list2 = listing[r].split("|")
        menu_list.append(list2[0])
        name_list.append(list2[1])

    # Store info from recipe.txt(for checking data validation)
    file.seek(0)
    recipecode_list = []  # Store recipe name/code
    recipeing_list = []  # Store ingredient name
    title = file.readline()
    read3 = file.read()
    read4 = read3.split("\n")
    listing1 = list(filter(None, read4))

    for j in range(len(listing1)):

        list1 = listing1[j].split(":")
        recipecode_list.append(list1[0])
        recipeing_list.append(list1[1])

    file2.seek(0)

    # Read ing from ingredient.txt (for data validation)
    ing_list = []  # Store ingredient name
    title = file2.readline()
    read5 = file2.read()
    read6 = read5.split("\n")
    listing2 = list(filter(None, read6))

    for r in range(len(listing2)):

        list3 = listing2[r].split("|")
        ing_list.append(list3[0])

    # Prompt for user to modify the menu and recipe
    # MENU ADDITION PLAN
    truth = True

    while truth == True:  # Will stop looping (add new recipe) once truth is false

        print("")
        single_divider(80)
        print(indent, "RECIPE and MENU Addition Plan -->", "\n")
        print(indent, "Enter new recipe to be added in MENU | <Q>uit\t>>", end="")
        new_recipe = str(input()).upper()

        # Data validation : the user cannot add the menu again that have been already in the menu
        if new_recipe in menu_list:

            print(indent, "The recipe has been in the MENU. Please enter again.")
            truth = True

        # If the user want to stop adding new recipe
        elif new_recipe == "Q":

            truth = False

        # Enter If the user does not want to quit and the input is not in the menu
        else:
            print(indent, "Enter new description\t\t\t\t>>", end="")
            des = str(input())

            # Data validation : the user cannot add the decription that have been already in the menu
            if des in name_list:

                print(indent, "The description has been in the MENU. Please enter again.")
                truth = True

            else:

                x = (new_recipe + "|" + des + "\n")  # append to menu.txt
                file1.write(x)
                print(indent, "The recipe has been successfully updated in MENU...")

                # RECIPE ADDITION PLAN
                truth2 = True

                while truth2 == True:
                    print("\n", indent, "Do you want the recipe to be updated in Recipe List? (yes/no)>>", end="")
                    verification = str(input()).upper()

                    if verification == "NO":

                        truth2 = False  # quit looping
                        truth3 = True  # go into verification3 to prompt user if he wants to add another recipe

                    elif verification == "YES":

                        file.write(new_recipe + ":")  # append recipe to recipe.txt
                        truth4 = True

                        while truth4 == True:

                            print(indent, "Enter the ingredient \t>>", end="")
                            y = str(input()).lower()

                            # Data validation: the user cannot add the ingredient that is not in the ingredient list
                            if y not in ing_list:

                                print(indent, "There is no", y, "in ingredient list. Please enter another ingredient.")
                                truth4 = True

                            else:

                                file.write(y + ",") # append ingredient to recipe.txt
                                print(indent, "Enter the quantity\t>>", end="")
                                z = input()
                                file.write(z + "-")  # append quantity to recipe.txt
                                print(indent, "Enter the units\t>>", end="")
                                q = input()

                                # Prompt the user to input to know whether it is the last ingredient
                                # To decide which format to print in the recipe.txt-->
                                # If last ingredient = "\n"
                                # If not last ingredient = "|"

                                truth1 = True

                                while truth1 == True:

                                    print("\n", indent, "Do you want to add another ingredient?(yes/no) >>", end="")
                                    verification2 = input().upper()

                                    if verification2 == "YES":

                                        file.write(q + "|")
                                        truth1 = False   # loop out of the verification
                                        truth4 = True    # continue to loop to enter ingredient

                                    elif verification2 == "NO":

                                        file.write(q + "\n")
                                        truth1 = False  # loop out of verification2  (to know whether the user wants to add another ingredient)
                                        truth2 = False  # loop out of verification (to know whether the user wants to update in recipe)
                                        truth3 = True   # enter verification3 (to know whether the user wants to add another recipe)
                                        truth4 = False  # loop out of ingredient prompt

                                    else:

                                        print(indent, "Invalid input. Please try again.")
                                        truth1 = True   # continue to loop in verification 2(see if the user wants to add another ingredient)

                    else:

                        print(indent, "Invalid input. Please try again")
                        truth2 = True   # continue to loop in verification (to know whether the user wants to update in recipe)

                # Enter verification 3 to know wheter the user wants to add another recipe
                if truth3 == True:

                    while truth3 == True:

                        print("\n", indent, "Do you want to add another RECIPE? (yes/no) >>", end="")
                        verification3 = input().upper()

                        if verification3 == "NO":

                            truth = False # loop out of recipe_addition
                            truth3 = False  # loop out of verification

                        elif verification3 == "YES":

                            truth = True    # continue to loop recipe_addition
                            truth3 = False  # loop out of verification

                        else:

                            print(indent, "Invalid input. Please try again")
                            truth3 = True # continue to loop verification

    file.close()
    file1.close()
    file2.close()


# RECIPE MODIFICATION PLAN
def recipe_modification():

    f1 = open("recipe.txt", "r")
    f2 = open("a.txt", "w")
    f3 = open("menu.txt", "r")
    f4 = open("b.txt", "w")
    f5 = open("ingredient.txt", "r")

    # Store code and name from menu.txt
    f3.seek(0)
    menu_list = []  # store recipe name from menu
    name_list = []  # store recipe description from menu
    title = f3.readline()  # to move the cursor to the next line(after title)

    if title.endswith('\n'):

        title = title.rstrip('\n')  # for rewrite purpose

    read1 = f3.read()
    read2 = read1.split("\n")
    listing = list(filter(None, read2))

    for r in range(len(listing)):

        list2 = listing[r].split("|")
        menu_list.append(list2[0])
        name_list.append(list2[1])

    # Store code from recipe.txt(for checking data validation & for rewrite if no changes)
    recipecode_list = []  # Store recipe name from recipe
    recipeing_list = []  # Store recipe ingredient from recipe
    f1.seek(0)
    title1 = f1.readline()
    read3 = f1.read()
    read4 = read3.split("\n")
    listing = list(filter(None, read4))

    for j in range(len(listing)):

        list1 = listing[j].split(":")
        recipecode_list.append(list1[0])
        recipeing_list.append(list1[1])

    # Read ing from ingredient.txt(for checking data validation)
    f5.seek(0)
    ing_list = []  # Store ingredient from ingredient list
    title2 = f5.readline()
    read5 = f5.read()
    read6 = read5.split("\n")
    listing2 = list(filter(None, read6))

    for r in range(len(listing2)):

        list3 = listing2[r].split("|")
        ing_list.append(list3[0])

    # RECIPE MODIFICATION
    truth = 1

    while truth != 0:  # stop looping when truth = 0, successful modified and enter menu if truth = 1, not successful so loop again if truth = 2

        print("")
        single_divider(80)
        print(indent, "RECIPE Modification Plan -->", "\n")
        print(indent, "Enter which recipe to update |<Q>uit >>", end="")
        updt = str(input()).upper()

        if updt == "Q":

            truth = 0

        elif updt not in recipecode_list:

            print(indent, "Recipe does not exist in RECIPE LIST. Please enter again.")
            truth = 2

        # Enter if the user does not want to quit and the recipe that the user wants to update is in the recipe
        else:

            x = ' '
            f1.seek(0)

            while (x):

                x = f1.readline()
                y = x.split(":")

                if int(len(x)) > 0:

                    if y[0] == updt:

                        print(indent, "Enter new recipe name >>", end="")
                        new = str(input()).upper()

                        truth3 = True

                        while truth3 == True:

                            print("\n", indent, "Do you want to modify ingredient? (yes/no) >>", end="")
                            verification = str(input()).upper()

                            if verification == "YES":  # Enter if the user want to modify ingredient

                                f2.write(new + ":")
                                truth4 = True

                                while truth4 == True:

                                    print(indent, "Enter the ingredient >>", end="")
                                    y = str(input()).lower()

                                    if y not in ing_list:

                                        print(indent, "There is no", y, "in ingredient list. Please enter another ingredient.")
                                        truth4 = True  # loop back for ingredient prompt

                                    else:

                                        f2.write(y + ",")
                                        print(indent, "Enter the quantity   >>", end="")
                                        z = str(input())
                                        f2.write(z + "-")
                                        print(indent, "Enter the units      >>", end="")
                                        q = str(input())

                                        # to decide the format to print to the recipe
                                        # if last ingredient = "\n"
                                        # if not last ingredient = "|"
                                        while True:

                                            print("\n", indent, "Do you want to add another ingredient?(yes/no) >>",end="")
                                            verification2 = input().upper()

                                            if verification2 == "YES":

                                                f2.write(q + "|")
                                                truth4 = True  # loop back for ingredient prompt
                                                truth5 = False  # loop out of verification2 prompt
                                                break

                                            elif verification2 == "NO":  # break all to go into menu modification

                                                f2.write(q + "\n")
                                                truth = 1  # break all to go into menu modification
                                                truth3 = False
                                                truth4 = False
                                                truth5 = False
                                                break

                                            else:

                                                print(indent, "Invalid input. Please try again.")

                            elif verification == "NO":  # Enter if the user want to modify recipe only but not ingredient

                                f2.write(new + ":")  # rewrite the ingredient into recipe.txt

                                for e in range(len(recipecode_list)):

                                    if updt == recipecode_list[e]:

                                        updtindex = e

                                f2.write(recipeing_list[updtindex] + "\n")
                                truth = 1
                                truth3 = False

                            else:

                                print(indent, "Invalid input. Please try again.")
                                truth3 = True

                    else:

                        f2.write(x)

        # MENU modification plan
        truth2 = 1

        if truth == 1:

            print(indent, "Recipe has been successfully modified in Recipe List...")
            truth1 = True

            while truth1 == True:

                single_divider(80)
                print("")
                print(indent, "Menu Modification plan -->", "\n")
                print(indent, "Do you want the recipe you updated in RECIPE to be modified in MENU? (yes/no) >>", end="")
                updt1 = str(input()).upper()

                if updt1 == "YES":

                    p = ' '
                    f3.seek(0)

                    while (p):

                        p = f3.readline()
                        b = p.split("|")

                        if int(len(p)) > 0:

                            if b[0] == updt:

                                print(indent, "New description for updated recipe in MENU >>", end="")
                                c = input()
                                f4.write(new + "|" + c + "\n")
                                truth2 = 1

                            else:

                                f4.write(p)
                # Will enter if the user does not want to update MENU

                elif updt1 == "NO":

                    truth1 = False  # Loop out of menu modification plan
                    truth2 = 0  # Will not print success message
                    print(title, file=f4)  # Print back title

                    for i in range(len(menu_list)):

                        print(f'{menu_list[i]}|{name_list[i]}', file=f4)  # Print back original menu into menu.txt

                    print(indent, "Record has been saved...")
                    print("\n", indent, "! REMINDER: Please modify your order as well to ensure correctness.")  # Reminder for corrective action
                    truth = 0  # Loop out of modification plan

                else:

                    truth1 = True
                    print(indent, "Invalid input. Please try again.")

                if truth2 == 1:

                    print(indent, "Menu has been successfully modified...")
                    print("\n", indent, "! REMINDER: Please modify your order as well to ensure correctness.")
                    truth1 = False  # Loop out of menu modification plan
                    truth = 0  # Straight away break modification plan , modify once at a time

    f1.close()
    f2.close()
    f3.close()
    f4.close()
    f5.close()
    os.remove("recipe.txt")
    os.rename("a.txt", "recipe.txt")
    os.remove("menu.txt")
    os.rename("b.txt", "menu.txt")


# RECIPE DELETION PLAN
def recipe_deletion():

    f1 = open("recipe.txt", "r")

    # Store code from recipe.txt(for checking data validation)
    recipe_list = []
    f1.seek(0)
    title = f1.readline()
    read1 = f1.read()
    read2 = read1.split("\n")
    nospace = list(filter(None, read2))

    for j in range(len(nospace)):

        list1 = nospace[j].split(":")
        recipe_list.append(list1[0])

    f1.close()

    truth = True

    while truth == True:

        print("")
        single_divider(80)
        print(indent, "Recipe Deletion Plan -->", "\n")
        print(indent, "Enter recipe to remove from recipe list|<Q>uit >>", end="")
        del_recipe = input().upper()

        if del_recipe == "Q":  # If the user want to quit

            truth = False  # Break out of the loop

        elif del_recipe not in recipe_list:  # Data validation: the user cannot enter recipe that are not in the recipe list to delete

            print(indent, "There is no recipe", del_recipe, ". Please enter again.")
            truth = True  # Keep looping

        else:

            # To write file
            with open("recipe.txt", 'r') as file:

                lines = file.readlines()

            with open("recipe.txt", 'w') as file:

                for line in lines:

                    if line.find(del_recipe) != -1:  # If found, will not be added into recipe.txt

                        pass
                        print(indent, "Recipe has been successfully deleted...")  # Success message

                    else:

                        file.write(line)  # Write the code existed except found del_recipe

            truth1 = True

            while truth1 == True:

                print("\n", indent, "Do you want to remove it from you menu?(yes/no) >>", end="")
                verification = str(input()).upper()

                if verification == "YES":

                    truth1 = False  # Break out of the loop

                    with open("menu.txt", 'r') as file:

                        lines = file.readlines()

                    with open("menu.txt", 'w') as file:

                        for line in lines:

                            if line.find(del_recipe) != -1:  # if found, will not be added into menu.txt

                                pass
                                print(indent, "MENU has been successfully deleted...")  # success message

                            else:

                                file.write(line)  # write the code existed except found del_recipe
                        print("\n", indent, "! REMINDER: Please remove it from your order as well to ensure correctness.")

                # If the user does not want the recipe to be deleted from menu
                elif verification == "NO":

                    print("\n", indent, "! REMINDER: Please remove it from your order as well to ensure correctness.")
                    truth1 = False  # Break out of the loop

                else:

                    print(indent, "Invalid input! Please try again.")  # Error message


# RECIPE RESET PLAN
# To DELETE everything in the recipe.txt and menu.txt and reset file
def recipe_reset():

    print(indent, "Resetting recipe ...")

    with open("recipe.txt", "w") as f1:

        f1.truncate()
        f1.write("RECIPE LIST" + "\n")

    print(indent, "The recipe has been successfully reset...")

    # Prompt for the user to reset menu
    truth = True

    while truth == True:

        print("\n", indent, "Do you want to reset MENU?(yes/no) >>", end="")
        verification = input().upper()

        if verification == "YES":

            print(indent, "Resetting menu ...")

            with open("menu.txt", "w") as f2:

                f2.truncate()
                f2.write("MENU" + "\n")

            print(indent, "The menu has been successfully reset...")
            truth = False

        elif verification == "NO":

            print(indent, "! Reminder: Please check the recipe order again to ensure correctness. ")
            truth = False

        else:

            print(indent, "Invalid input! Please enter again.")

#=======================================================================================================================
# ORDER CREATION
def order_print():  # print order

    with open("order.txt", "r") as f:

        listcode = []
        listname = []
        listunit = []
        f.seek(0)
        title = f.readline()  # to move the cursor after the title

        if title.endswith('\n'):
            title = title.rstrip('\n')  # to remove the space line for printing

        double_divider(80)
        print("")
        double_divider(80)
        print(left_bar, f'{title:^77}{"|":>1}')
        double_divider(80)
        print(left_bar, f'\t\t{"Recipe":<20s}{"Description":<28s}{"Quantity":<s}{"|":>9}')
        single_divider(80)
        read3 = f.read()
        read4 = read3.split("\n")  # separate data by spliting break line
        recipe = list(filter(None, read4))

        for i in range(len(recipe)):  # loop to store data seperately
            recipe_list = recipe[i].split("|")
            listcode.append(recipe_list[0])
            listname.append(recipe_list[1])
            listunit.append(recipe_list[2])
            print(left_bar, f'\t\t{listcode[i]:<15s}\t{listname[i]:<18s}\t{listunit[i]:>12s}{"|":>13}')

        double_divider(80)


def order_addition():  # add new data
    f1 = open("menu.txt", "r")
    f2 = open("order.txt", "a+")
    title = f1.readline()
    title1 = f2.readline()

    menu_list = []  # store code and name from menu.txt
    name_list = []
    read1 = f1.read()
    read2 = read1.split("\n")
    listing = list(filter(None, read2))

    for r in range(len(listing)):  # loop to store data seperately

        list1 = listing[r].split("|")
        menu_list.append(list1[0])
        name_list.append(list1[1])

    order_list = []  # store code from order.txt(for checking data validation)
    f2.seek(0)
    read3 = f2.read()
    read4 = read3.split("\n")
    listorder = list(filter(None, read4))

    for j in range(len(listorder)):

        list1 = listorder[j].split("|")
        order_list.append(list1[0])

    truth = 0

    while truth == 0:

        print("")
        single_divider(80)
        print(indent, "Order Addition Plan -->", "\n")
        print(indent, "Enter new order |<Q>uit >>", end="")
        new_recipe = input().upper()

        if new_recipe == "Q":

            truth = 1

        elif new_recipe in order_list:

            print(indent, "The recipe existed! Please <M>odify.")
            truth = 0

        elif new_recipe not in menu_list:

            print(indent, "Invalid recipe! Please enter again.")
            truth = 0

        else:

            print(indent, "Enter new qty to bake   >>", end="")
            new_qty = input()
            truth = 1  # loop to match the order code with recipe code

            for t in range(len(menu_list)):

                if menu_list[t] == new_recipe:

                    total_a = (new_recipe + "|" + name_list[t] + "|" + new_qty)
                    f2.write(total_a)
                    print(indent, "Your new order has been saved...")

    f1.close()
    f2.close()


def order_modification():  # modify data

    f1 = open("order.txt", "r")
    f2 = open("abc.txt", "w")
    f3 = open("menu.txt", "r")
    f1.seek(0)
    f3.seek(0)
    title1 = f1.readline()
    title = f3.readline()

    menu_list = []  # store code and name from menu.txt
    name_list = []
    read1 = f3.read()
    read2 = read1.split("\n")
    listing = list(filter(None, read2))

    for r in range(len(listing)):

        list1 = listing[r].split("|")
        menu_list.append(list1[0])
        name_list.append(list1[1])

    order_list = []  # Store code from order.txt (for data validation)
    f1.seek(0)
    read3 = f1.read()
    read4 = read3.split("\n")
    listorder = list(filter(None, read4))

    for j in range(len(listorder)):
        list1 = listorder[j].split("|")
        order_list.append(list1[0])

    truth = True

    while truth == True:

        print("")
        single_divider(80)
        print(indent, "Order Modification plan -->", "\n")
        print(indent, "Enter which order to update | <Q>uit >>", end="")
        updt = input().upper()

        if updt == "Q":

            truth = False

        elif updt not in order_list:

            print(indent, "There is no order", updt, ". Please enter again.")

        elif updt not in menu_list:

            print(indent, "Invalid recipe. Please enter again.")

        else:

            x = ' '
            f1.seek(0)

            while (x):

                x = f1.readline()
                y = x.split("|")

                if int(len(x)) > 0:

                    if y[0] == updt:

                            print(indent, "Enter new quantity | <Q>uit >>", end="")
                            new_q = input()

                            if new_q == "Q" or new_q == "q":

                                f2.write(x)
                                break

                            for i in range(len(menu_list)):

                                if updt in menu_list:
                                    name = name_list[i]

                            f2.write(updt + "|" + name + "|" + new_q + "\n")
                            print(indent, "Order has been successfully modified...")

                    else:

                        f2.write(x)

            break

    f1.close()
    f2.close()
    f3.close()
    os.remove("order.txt")
    os.rename("abc.txt", "order.txt")


def order_deletion():  # delete data

    f1 = open("order.txt", "r")
    f1.readline()  # To move the cursor to the next line

    order_list = []  # Store code from order.txt (for data validation)
    f1.seek(0)
    read3 = f1.read()
    read4 = read3.split("\n")

    for j in range(len(read4)):

        list1 = read4[j].split("|")
        order_list.append(list1[0])

    f1.close()

    truth = True

    while truth != False:

        print("\n", indent, "Order Deletion plan -->", "\n")
        print(indent, "Enter recipe to remove |<Q>uit >>", end="")
        del_recipe = input().upper()

        if del_recipe == "Q":

            truth = False

        elif del_recipe not in order_list:

            print(indent, "There is no order", del_recipe, ". Please enter again.")
            truth = True

        else:

            with open("order.txt", 'r') as file:

                lines = file.readlines()

            with open("order.txt", 'w') as file:

                for line in lines:

                    if line.find(del_recipe) != -1:

                        pass
                        print(indent, "Order has been successfully deleted...")

                    else:

                        file.write(line)


def order_reset():  # delete everything inside the file

    print(indent, "Resetting order ...")

    with open("order.txt", "w") as f1:

        f1.truncate()
        f1.write("ORDER" + "\n")

    print(indent, "The order has been successfully reset...")

#=======================================================================================================================
# MATERIAL REQUIREMENT PLAN
def mrp():
    
    # to print title and time of MRP
    double_divider(80)
    now = datetime.datetime.now()
    time = now.strftime("%d/%m/%Y %H:%M:%S")
    print(left_bar, f'{"MATERIAL REQUIREMENT PLAN (MRP) Run":^77}{"|": >1}')
    print(left_bar, f'{"Date and time: %s" %time:^77}{"|": >1}')
    double_divider(80)
    print("")
    double_divider(80)
    print(left_bar, f'{"PRODUCTION PLAN":^77}{"|": >1}')
    double_divider(80)
    print(left_bar, f'{"Code":<20}{"Recipe":<30}{"Quantity":<27}{"|": >1}')
    single_divider(80)
    
    # To display order/PRODUCTION PLAN
    production_plan()
    double_divider(80)
    
    # To print RECIPE onto the screen
    recipe_printing()
    double_divider(80)

    # To calculate and display demand, unit, stock level and shortfall
    print(left_bar, f'{"INGREDIENT REQUIREMENT":^77}{"|": >1}')
    double_divider(80)
    demand()


# To display order/ Production Plan
def production_plan():
    with open("order.txt", "r") as file:

        file.seek(0)
        title = file.readline()

        read1 = file.read()
        read2 = read1.split("\n")
        recipe = list(filter(None, read2))
        listcode = []
        listname = []
        listqty = []

        for i in range(len(recipe)):

            recipe_list = recipe[i].split("|")
            listcode.append(recipe_list[0])
            listname.append(recipe_list[1])
            listqty.append(recipe_list[2])
            print(left_bar, f'{listcode[i]:<20s}{listname[i]:<24s}{listqty[i]:>9s}{"|": >25}')


#  To print recipe onto the screen
def recipe_printing():

    file = open("recipe.txt", "r")
    file0 = file.read()
    CoList = file0.split("\n")
    Counter = 0

    for i in CoList:

        if i:

            Counter += 1

    total_recipe = Counter - 1

    file.seek(0)
    title = file.readline()  # To move the cursor to the next line

    if title.endswith('\n'):

        title = title.rstrip('\n')

    print("")
    double_divider(80)

    # To print header
    print(left_bar, f'{title:^77s}{"|": >1}')
    double_divider(80)
    print(left_bar, f'{"Recipe":<20}{"Ingredient":<24}{"Requirement":<22}{"Unit":<11}{"|": >1}')
    single_divider(80)

    recipe_list = []
    ING_list = []
    QTY_list = []
    UNIT_list = []

    for recipeNUM in range(total_recipe):  # Handle recipe one by one

        recipe = file.readline()

        if recipe.endswith('\n'):

            recipe = recipe.rstrip('\n')

        # Empty list that refreshes every time
        totalinglist = []  # No use, just for splitting
        inglist = []
        qtyunitlist = []  # No use, just for splitting
        qtylist = []  # In integer
        unitlist = []

        # To split and store recipe name, ingredient, unit, quantity into different list
        code = recipe.split(":")    
        recipe_list.append(code[0]) # recipe name
        total_ingredientlist = code[1].split("|")

        for i in range(len(total_ingredientlist)):

            totalinglist.append(total_ingredientlist[i].split(",")) 

        for j in range(len(totalinglist)):

            inglist.append(totalinglist[j][0])  # ingredient
            qtyunitlist.append(totalinglist[j][1])

        for k in range(len(qtyunitlist)):

            qty_unit = qtyunitlist[k].split("-")
            qtylist.append(float(qty_unit[0]))  # quantity
            unitlist.append(qty_unit[1])    # unit

        ING_list.append(inglist)
        QTY_list.append(qtylist)
        UNIT_list.append(unitlist)

    # Printing of recipe
    for a in range(len(recipe_list)):

        print(left_bar, f'{recipe_list[a]:<77s}{"|": >1}')

        for b in range(len(ING_list[a])):

            print(left_bar, f'{"":<20}{ING_list[a][b]:<20}{"%.2f"%QTY_list[a][b]:>10}{UNIT_list[a][b]:>17}{"|": >11}')

        if a != len(recipe_list)-1:

            print(left_bar, f'{"|":>78}')
            single_divider(80)

        else:

            print(left_bar, f'{"|":>78}')
            double_divider(80)
            print("")

    file.close()


# To calculate demand, shortfall
def demand():

    print(left_bar, f'{"Ingredient":<15s}{"Unit":>s}{"Stock level":>17s}{"Demand":>16s}{"Shortfall":>20s}{"|": >6}')
    single_divider(80)
    file = open("recipe.txt", "r")
    file0 = file.read()
    CoList = file0.split("\n")
    
    Counter = 0
    for i in CoList:
        if i:
            Counter += 1

    total_recipe = Counter - 1

    file.seek(0)
    title = file.readline()  # To move the cursor to the next line

    totaling_amtlist = []
    ing_referencelist = []

    for recipeNUM in range(total_recipe):  # Handle recipe one by one

        recipe = file.readline()
        if recipe.endswith('\n'):
            recipe = recipe.rstrip('\n')

        # Empty list that refreshes every time
        recipe_list = []
        totalinglist = []  # No use, just for splitting
        inglist = []
        qtyunitlist = []  # No use, just for splitting
        qtylist = []  # In integer
        unitlist = []
        orderlist = []
        orderqty_list = []
        total_ingamt_eachlist = []
        total_inglist = []

        # To split and store recipe name, ingredient, unit, quantity into different list
        code = recipe.split(":")
        recipe_list.append(code[0]) # recipe name
        total_ingredientlist = code[1].split("|")

        for i in range(len(total_ingredientlist)):

            totalinglist.append(total_ingredientlist[i].split(","))

        for j in range(len(totalinglist)):

            inglist.append(totalinglist[j][0])  # ingredient
            qtyunitlist.append(totalinglist[j][1])

        for k in range(len(qtyunitlist)):

            qty_unit = qtyunitlist[k].split("-")
            qtylist.append(float(qty_unit[0]))  # quantity
            unitlist.append(qty_unit[1])    # unit

        # Read order quantity from order.txt 
        with open("order.txt", "r") as f:

            f.seek(0)
            title = f.readline()
            read1 = f.read()
            read2 = read1.split("\n")
            quantity = list(filter(None, read2))

            for j in range(len(quantity)):

                list1 = quantity[j].split("|")
                orderlist.append(list1[0])
                orderqty_list.append(int(list1[2]))

        # Check if recipe in order list, only will calculate for those in order list
        for g in recipe_list:

            if g in orderlist:
                recipeindex_in_order = orderlist.index(g)
                total_inglist = inglist
                order_qty = orderqty_list[recipeindex_in_order]
                truth = 1

            else:
                truth = 0

        # To store all demand of each recipe in a list
        if truth == 1:

            for i in range(len(inglist)):

                total_ingamt_each = int(qtylist[i] * order_qty)
                total_ingamt_eachlist.append(total_ingamt_each)

        # TO store all in 2 list--> ing(ingredient) for index referencing, amt(amount) for calculation
        totaling_amtlist.append(total_ingamt_eachlist)
        totaling_amtlist = list(filter(None, totaling_amtlist))
        ing_referencelist.append(total_inglist)
        ing_referencelist = list(filter(None, ing_referencelist))

    item_list = []
    quantity_list = []

    # Get each ingredient and respective quantity ( in same index for reference) from nested list
    for a in range(len(ing_referencelist)):
        for b in range(len(ing_referencelist[a])):
            item_list.append(ing_referencelist[a][b])

    for c in range(len(totaling_amtlist)):
        for d in range(len(totaling_amtlist[c])):
            quantity_list.append(totaling_amtlist[c][d])

    # To calculate total demand(quantity needed) of same ingredient
    demand_list = []
    quantity_list_2 = []
    total_demandlist = []

    while len(item_list) != 0:
        item = item_list[0]
        quantity = quantity_list[0]
        item_list.pop(0)
        quantity_list.pop(0)
        quantity_list_2.append(quantity)

        while item in item_list:
            index = item_list.index(item)
            quantity = quantity_list[index]
            quantity_list_2.append(quantity)
            item_list.pop(index)
            quantity_list.pop(index)

        total_quantity = 0

        for i in range(len(quantity_list_2)):
            total_quantity += float(quantity_list_2[i]) # added up quantity for same ingredient

        demand_list.append(item) # store the name of ingredient in a list for reference
        total_demandlist.append(float(total_quantity))
        quantity_list_2.clear()

    # Read ingredient stock level from ingredient.txt and store as list
    with open("ingredient.txt", "r") as file:

        file.seek(0)
        title = file.readline()
        read1 = file.read()
        read2 = read1.split("\n")
        ingredient = list(filter(None, read2))
        ing_list2 = []
        unit_list = []
        stock_level = []

        for j in range(len(ingredient)):
            ing_list = ingredient[j].split("|")
            ing_list2.append(ing_list[0])
            unit_list.append(ing_list[1])
            stock_level.append(float(ing_list[2]))

    # Compare ingredient in ingredient list and ingredient in recipe list
    AMTINGlist = []
    ingredient_list = []
    UNIT_list = []

    for e in range(len(ing_list2)):
        
        # only will store into the lists if ingredient in ingredient list exists in demand(needed in recipe)
        # to get rid of unwanted ingredient index taken from list from ingredient.txt (for shortfall of same ingredients)
        if ing_list2[e] in demand_list:
            Ingredient = ing_list2[e]
            ingredient_amt = stock_level[e]
            unit = unit_list[e]
            ingredient_list.append(Ingredient)
            AMTINGlist.append(ingredient_amt)
            UNIT_list.append(unit)

    # Calculate shortfall of ingredient
    shortfall_list = []

    for i in range(len(ingredient_list)):

        for j in range(len(demand_list)):

            if ingredient_list[i] == demand_list[j]:

                shortfall = AMTINGlist[i] - total_demandlist[j]

                if shortfall >= 0:

                    shortfall = "N/A" # no shortfall: the stock level is more than demand

                else:

                    shortfall = format((0 - shortfall), ".2f")  # format the shortfall: without -ve sign, 2 decimal places

                shortfall_list.append(shortfall)

    # Display on the screen: demand, unit, stock level and shortfall
    for u in range(len(shortfall_list)):

        print(left_bar, f'{demand_list[u]:<18s}{UNIT_list[u]:<5}{"%.2f"%stock_level[u]:>12}{"%.2f"%total_demandlist[u]:>17}{shortfall_list[u]:>20}{"|": >6}')

    single_divider(80)
    file.close()
