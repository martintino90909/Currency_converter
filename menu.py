import currency_converter
import pprint
import os.path

pp = pprint.PrettyPrinter()


def start_menu():
    print("welcome to coolcurrencyconverter.progamer@696969.com")
    user_start_input = input("Would you like to 1.convert a currency 2.access favourite 3.edit favourites :") or "2"
    if user_start_input == "1":
        main_menu()
    elif user_start_input == "2":
        view_favourite()
    elif user_start_input == "3":
        favourite_list()


def main_menu():
    local_currency = input("Please enter local currency :").upper()
    amount = int(input("Please enter amount to convert [Leave blank for base rates] :") or 1)
    pp.pprint(currency_converter.convert_all(amount, local_currency))


def view_favourite():
    local_currency = input("Please enter local currency :").upper()
    amount = int(input("Please enter amount to convert [Leave blank for base rates] :") or 1)
    if os.path.exists("favefile.cfg"):
        f = open("favefile.cfg", "r")
        fave_file = f.read()
        fave_list = fave_file.splitlines()
        pp.pprint(currency_converter.convert_selected(amount, local_currency, fave_list))


def favourite_list():
    # make sure currency code is real currency
    add_or_remove_currency = input("Please enter currency you would like to add or remove :").upper()
    action = input("Enter what you would like to do [A = Add/R = Remove]").upper()
    if action == "A":
        if os.path.exists("favefile.cfg"):
            f = open("favefile.cfg", "r")
            fave_file = f.read()
            if add_or_remove_currency in fave_file:
                print("Currency is already in favourite")
                return
        a = open("favefile.cfg", "a")
        a.write(add_or_remove_currency + "\n")
        a.close()
    elif action == "R":
        if os.path.exists("favefile.cfg"):
            f = open("favefile.cfg", "r")
            fave_file = f.read()
            if add_or_remove_currency not in fave_file:
                print("Currency is not in file")
                return
            write_string = fave_file.replace(add_or_remove_currency + "\n", "")
            b = open("favefile.cfg", "w")
            b.write(write_string)
            b.close()
