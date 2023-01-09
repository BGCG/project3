from datetime import datetime, date
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials
import pprint


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


def validate_abo_data():
    """
    Validate blood type input data and add to sheet
    """
    abo_inputted = False
    while abo_inputted is False:
        try:
            print('Please enter the ABO blood type followed by Rh status '
                  'i.e. APOS, ONEG, ABPOS')
            abo_input = str(input('Enter blood type: ')).strip().upper()
            if abo_input.upper() in options:
                print(f'The blood type you entered was {abo_input}')
                abo_inputted = True
                donations.update_acell('A8', abo_input.upper())
            else:
                print("You entered an invalid input")
        except ValueError:
            print("You entered an invalid input")
        return abo_input


abo_value = validate_abo_data()
values = stock_check_data[1:]
abo_value_lst = [item for item in values if abo_value in item]
bloodid_lst = [int(item[3]) for item in abo_value_lst]


def check_stock():
    """
    Check stock and provides feedback to user of specific blood type
    """
    headers = stock_check.row_values(1)
    unit_lst = [int(item[1]) for item in abo_value_lst]

    blood_data = [dict(zip(headers, row)) for row in values if
                  abo_value in row]
    print(f'The blood stock for {abo_value} is as follows - ')
    print(pprint.pformat(str(blood_data).replace("'", "").replace('[', '')
          .replace(']', '')))
    return unit_lst


def stock_low_alert():
    """
    Alerts user to whether blood is low of particular type
    """
    unit_lst = check_stock()
    if any(num < 10 for num in unit_lst):
        print(f'You are running low on {abo_value} stock')
        samples_index = [i for i in range(len(unit_lst)) if unit_lst[i] < 10]
        sample_bloodid = [bloodid_lst[i] for i in samples_index]
        print(f'The following blood id(s) are low in stock - {sample_bloodid}')
    else:
        print(f'You have sufficient stock of {abo_value}')


stock_low_alert()


def check_expiry():
    """
    Checks if certain stock is outwith expiry
    """
    todays_date = date.today().isocalendar()

    exp_lst = [item[2] for item in abo_value_lst]

    exp_lst_formatted = [datetime.strptime(item, "%m-%d-%y").date()
                         .isocalendar() for item in exp_lst]
    
    if any(exp < todays_date for exp in exp_lst_formatted):
        print(f'You have {abo_value} stock that is expired')
        samples_index = [i for i in range(len(exp_lst_formatted))
                         if exp_lst_formatted[i] < todays_date]
        sample_bloodid = [bloodid_lst[i] for i in samples_index]
        print(f'The id(s) of the expired stock is - {sample_bloodid}. '
              'Please discard this bag.')
    else:
        print(f'All {abo_value} stock is within expiry date')


check_expiry()

