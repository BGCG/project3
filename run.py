# Wireing up of API and scope declarations helped by following Code institutes
# Love Sandwiches tutorial

from datetime import datetime, date
from tabulate import tabulate
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('project3')

stock_check = SHEET.worksheet('stock')

stock_check_data = stock_check.get_all_values()

options = ['APOS', 'ANEG', 'BPOS', 'BNEG', 'ABPOS', 'ABNEG', 'OPOS', 'ONEG']

print('Welcome to the BloodTracker app!\n')


def validate_abo_data():
    """
    Validate blood type input data to ensure any input is same as options list.
    Allow whitespace at from or end of input but not between characters.
    Alert user if the response does not match options list.
    Return the correct user input.
    """
    abo_inputted = False

    while abo_inputted is False:

        print('Please enter the ABO blood type followed by Rh status '
              'i.e. APOS, ONEG, ABPOS\n')
        abo_input = str(input('Enter the blood type here: \n')).upper().strip()

        if abo_input in options:
            print(f'The blood type you entered was {abo_input}')
            print('Your input was valid \n')
            abo_inputted = True
        else:
            print('Sorry your input was invalid\n')

    return abo_input


def check_stock(abo_data, abo_lst):
    """
    Provide feedback of stock details including units and expiration
    of specific blood type as specified by the user input.
    """
    head = stock_check.row_values(1)
    # Build dictonary and provide this in a string output for readability
    # Creation of dict was helped by learnings from the follow post -
    # https://stackoverflow.com/questions/72076666/create-a-dictionary-from-multiple-lists-one-list-as-key-other-as-value
    blood_data = [dict(zip(head, row)) for row in abo_lst if
                  abo_data in row]
    print(f'The blood stock for {abo_data} is as follows: \n')
    print(tabulate(blood_data, headers="keys"))
    print("\n")


def stock_low_alert(id_list, abo_data, units):
    """
    Alerts user to whether blood is low in units of particular type
    as specified by user input and report this to user.
    Alert which particular blood type stock is low by reporting id.
    """
    if any(num < 10000 for num in units):
        print(f'You are running low on {abo_data} stock')
        samples_index = [i for i in range(len(units)) if units[i] < 10000]
        sample_bloodid = [id_list[i] for i in samples_index]
        print('The following blood ID(s) are low in stock:'
              f' {str(sample_bloodid)[1:-1]}\n')
    else:
        print(f'You have sufficient stock of {abo_data}\n')


def check_expiry(id_list, abo_data, abo_lst):
    """
    Checks if stock a particular blood type is outwith expiry
    and report this to user.
    Convert dates extracted from google sheets to isocalendar format
    and also do same conversion for todays date to allow determination
    of equality or not.
    Alter which specific blood type stock is low by reporting id.
    """
    todays_date = date.today().isocalendar()

    exp_lst = [item[2] for item in abo_lst]

    # Conversion of date formats in exp_lst helped
    # by learnings from the following post -
    # https://stackoverflow.com/questions/36424255/python-iterating-through-a-list-using-datetime-strptime

    exp_lst_formatted = [datetime.strptime(item, "%m-%d-%Y").date()
                         .isocalendar() for item in exp_lst]

    if any(exp < todays_date for exp in exp_lst_formatted):
        print(f'You have {abo_data} stock that is expired')
        samples_index = [i for i in range(len(exp_lst_formatted))
                         if exp_lst_formatted[i] < todays_date]
        sample_bloodid = [id_list[i] for i in samples_index]
        print('The ID(s) of the expired stock is:'
              f' {str(sample_bloodid)[1:-1]}')
        print('Please discard the blood bag(s) matching this ID.\n')
    else:
        print(f'All {abo_data} stock is within expiry date.\n')


def main():
    """
    Calls for all functions
    This function also contains heavily used variables
    """
    abo_value = validate_abo_data()
    values = stock_check_data[1:]
    abo_value_lst = [item for item in values if abo_value in item]
    unit_lst = [int(item[1]) for item in abo_value_lst]
    check_stock(abo_value, abo_value_lst)
    bloodid_lst = [int(item[3]) for item in abo_value_lst]
    stock_low_alert(bloodid_lst, abo_value, unit_lst)
    check_expiry(bloodid_lst, abo_value, abo_value_lst)


main()


# Code to allow user to restart stock check if they wish or exit

while True:
    user_input = input('Would you like to check another blood type? '
                       'Answer y/n: \n').lower().strip()
    if user_input == 'y':
        main()
    elif user_input == 'n':
        print("\n")
        print('Thank you for using the BloodTracker app.\n')
        break
    else:
        print('You entered an invalid input - answer y/n\n')
