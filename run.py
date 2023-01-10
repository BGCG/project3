import pprint
from datetime import datetime, date
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

# global variables as caps
donations = SHEET.worksheet('donations')
stock = SHEET.worksheet('stock')
adj_stock = SHEET.worksheet('adjusted_stock')
stock_check = SHEET.worksheet('stock_check')

donation_data = donations.get_all_values()
stock_data = stock.get_all_values()
adj_stock_data = adj_stock.get_all_values()
stock_check_data = stock_check.get_all_values()

options = ['APOS', 'ANEG', 'BPOS', 'BNEG', 'ABPOS', 'ABNEG', 'OPOS', 'ONEG']

print('Welcome to the blood checker app!')


def validate_abo_data():
    """
    Validate blood type input data and add to sheet
    """
    abo_inputted = False

    while abo_inputted is False:
        
        print('Please enter the ABO blood type followed by Rh status '
              'i.e. APOS, ONEG, ABPOS')
        abo_input = str(input('Enter the ABO blood type: ')).upper().strip()

        if abo_input in options:
            print(f'The blood type you entered was {abo_input}')
            print('Your input was valid')
            abo_inputted = True
        else:
            print('Sorry your input was invalid')
    
    return abo_input


def check_stock(abo_data, abo_lst):
    """
    Check stock and provides feedback to user of specific blood type
    """
    headers = stock_check.row_values(1)
    blood_data = [dict(zip(headers, row)) for row in abo_lst if
                  abo_data in row]
    print(f'The blood stock for {abo_data} is as follows - ')
    print(pprint.pformat(str(blood_data).replace("'", "").replace('[', '')
          .replace(']', '')))


def stock_low_alert(id_list, abo_data, units):
    """
    Alerts user to whether blood is low of particular type
    """
    if any(num < 10 for num in units):
        print(f'You are running low on {abo_data} stock')
        samples_index = [i for i in range(len(units)) if units[i] < 10]
        sample_bloodid = [id_list[i] for i in samples_index]
        print(f'The following blood id(s) are low in stock - {sample_bloodid}')
    else:
        print(f'You have sufficient stock of {abo_data}')


def check_expiry(id_list, abo_data, abo_lst):
    """
    Checks if certain stock is outwith expiry
    """
    todays_date = date.today().isocalendar()

    exp_lst = [item[2] for item in abo_lst]

    exp_lst_formatted = [datetime.strptime(item, "%m-%d-%y").date()
                         .isocalendar() for item in exp_lst]

    if any(exp < todays_date for exp in exp_lst_formatted):
        print(f'You have {abo_data} stock that is expired')
        samples_index = [i for i in range(len(exp_lst_formatted))
                         if exp_lst_formatted[i] < todays_date]
        sample_bloodid = [id_list[i] for i in samples_index]
        print(f'The id(s) of the expired stock is - {sample_bloodid}. '
              'Please discard this bag.')
    else:
        print(f'All {abo_data} stock is within expiry date')


def main():
    """
    Calls for all functions
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


while True:
    user_input = input('Would you like to check another blood type? '
                       'Answer y/n: ').strip()
    if user_input == 'y':
        main()
    elif user_input == 'n':
        print('Thank you for using the blood tracker system.')
        break
    else:
        print('You entered an invalid input - answer y/n')
