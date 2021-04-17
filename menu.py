import json
import requests
import currency_converter
from currency import Currency
import pprint
import os.path

def load_currency_info():
    currencies_dict = dict()
    response = requests.get("https://gist.githubusercontent.com/Fluidbyte/2973986/raw/8bb35718d0c90fdacb388961c98b8d56abc392c9/Common-Currency.json")
    if response.status_code == 200:
        content = response.content.decode("utf-8")
        json_content = json.loads(content)
        for key, value in json_content.items():
            currencies_dict[value["code"]] = Currency(value["symbol"], value["name"], value["symbol_native"], value["decimal_digits"], value["rounding"], value["code"], value["name_plural"])
    return currencies_dict

pp = pprint.PrettyPrinter()
currencies = load_currency_info()


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
    dict_of_adjusted_rates = currency_converter.convert_all(amount, local_currency)
    print(get_rates_string(dict_of_adjusted_rates, amount))





def get_rates_string(rates_dict, amount):
    output = "currency\tamount (" + str(amount) + ")\n"
    for adjusted_rate in rates_dict:
        if adjusted_rate in currencies.keys():
            output += currencies[adjusted_rate].name + "\t\t\t" + str(rates_dict[adjusted_rate]) + "\n"
        else:
            output += adjusted_rate + "\t\t\t" + str(rates_dict[adjusted_rate]) + "\n"
    return output


def view_favourite():
    local_currency = input("Please enter local currency :").upper()
    amount = int(input("Please enter amount to convert [Leave blank for base rates] :") or 1)
    if os.path.exists("favefile.cfg"):
        f = open("favefile.cfg", "r")
        fave_file = f.read()
        fave_list = fave_file.splitlines()
        dict_of_adjusted_rates = currency_converter.convert_selected(amount, local_currency, fave_list)
        print(get_rates_string(dict_of_adjusted_rates, amount))


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
