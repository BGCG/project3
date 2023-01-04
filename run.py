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

donation_data = donations.get_all_values()
stock_data = stock.get_all_values()

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
            abo_input = str(input('Enter the ABO blood type entered: '))
            if abo_input.upper() in options:
                print(f'The blood type you entered was {abo_input.upper()}')
                abo_inputted = True
                donations.update_acell('A8', abo_input.upper())
            else:
                print("You entered an invalid input")
            # return abo_input
        except ValueError:
            print("You entered an invalid input")


validate_abo_data()

# DONATIONS_DATA = validate_abo_data()
# print(DONATIONS_DATA.upper())


# def update_donations_worksheet(data):
#     """
#     Append row to donations worksheet
#     """
#     donations.append_row(data, table_range="donations!A:A")

def check_stock():
    """
    Check stock data
    """
    print('Calculating donations collected today...')
    apos_count = donations.findall('APOS')
    print(apos_count)


check_stock()


def update_stock():
    """
    Check stock data
    """
    stock_inputted = False
    while stock_inputted is False:
        try:
            print('Please input the blood stock today in eight digits in the '
                  'following format 29, 25, 20, 50, 20, 29, 20, 19')
            stock_input = []
            stock_input = input('Please enter the stock check for today: ')
            for int(values) in stock_input:
                if len(stock_input[values]) == 8:
                    print(f'You entered the following numbers - {stock_input}')
                    stock_inputted = True
        except ValueError:
            print("You entered an invalid input")


update_stock()
