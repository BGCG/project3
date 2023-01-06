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

donation_data = donations.get_all_values()
stock_data = stock.get_all_values()
adj_stock_data = adj_stock.get_all_values()

# options = ['APOS', 'ANEG', 'BPOS', 'BNEG', 'ABPOS', 'ABNEG', 'OPOS', 'ONEG']


# def validate_abo_data():
#     """
#     Validate blood type input data and add to sheet
#     """
#     abo_inputted = False
#     while abo_inputted is False:
#         try:
#             print('Please enter the ABO blood type followed by Rh status '
#                   'i.e. APOS, ONEG, ABPOS')
#             abo_input = str(input('Enter the ABO blood type: '))
#             if abo_input.upper() in options:
#                 print(f'The blood type you entered was {abo_input.upper()}')
#                 abo_inputted = True
#                 donations.update_acell('A8', abo_input.upper())
#             else:
#                 print("You entered an invalid input")
#             # return abo_input
#         except ValueError:
#             print("You entered an invalid input")


# validate_abo_data()

# DONATIONS_DATA = validate_abo_data()
# print(DONATIONS_DATA.upper())


# def update_donations_worksheet(data):
#     """
#     Append row to donations worksheet
#     """
#     donations.append_row(data, table_range="donations!A:A")

# def check_stock():
#     """
#     Check stock data
#     """
#     print('Calculating donations collected today...')
#     blood_count = donations.col_values(1)
#     apos_count = blood_count.count('APOS')
#     print('Number of A positive blood donations collected today:'
#           ', apos_count)
#     aneg_count = blood_count.count('ANEG')
#     print('Number of A negative blood donations collected today:'
#           ', aneg_count)
#     bpos_count = blood_count.count('BPOS')
#     print('Number of B positive blood donations collected today:'
#           ', bpos_count)
#     bneg_count = blood_count.count('BNEG')
#     print('Number of B negative blood donations collected today:'
#           ', bneg_count)
#     abpos_count = blood_count.count('ABPOS')
#     print('Number of AB positive blood donations collected today:',
#           abpos_count)
#     abneg_count = blood_count.count('ABNEG')
#     print('Number of AB negative blood donations collected today:',
#           abneg_count)
#     opos_count = blood_count.count('OPOS')
#     print('Number of O positive blood donations collected today:'
#           ', opos_count)
#     oneg_count = blood_count.count('ONEG')
#     print('Number of O negative blood donations collected today:'
#           ', oneg_count)


# check_stock()


def validate_stock_input():
    """
    Validate user input data for stock data
    """
    stock_inputted = False
    while stock_inputted is False:
        try:
            print('Please input the blood stock today in eight digits '
                  'seperated by a space and no commas between')
            stock_input = input('Please enter the number of donations'
                                ' collected today: ').split()
            stock_list = [int(item) for item in stock_input]
            print(stock_list)
            print(len(stock_list))
            if any(num < 0 for num in stock_list):
                print('One or more of the numbers are negative -'
                      'please ensure they are all positive')
            elif len(stock_list) != 8:
                print('You entered the wrong number of numbers.'
                      'Please enter 8 sets')
            else:
                print(f'You entered the following numbers - {stock_list}')
                stock_inputted = True
        except ValueError:
            print("You entered an invalid input - must be only numeric")
    return stock_list


def validate_used_stock_input():
    """
    Validate used stock input
    """
    used_stock_inputted = False
    while used_stock_inputted is False:
        try:
            print('Please input the used blood stock today in eight digits '
                  'seperated by a space and no commas between')
            used_stock_input = input('Please enter the nummber of'
                                     ' used donations: ').split()
            used_stock_list = [int(item) for item in used_stock_input]
            print(used_stock_list)
            print(len(used_stock_list))
            if any(num < 0 for num in used_stock_list):
                print('One or more of the numbers are negative -'
                      'please ensure they are all positive')
            elif len(used_stock_list) != 8:
                print('You entered the wrong number of numbers.'
                      'Please enter 8 sets')
            else:
                print(f'You entered the following numbers - {used_stock_list}')
                used_stock_inputted = True
        except ValueError:
            print("You entered an invalid input - must be only numeric")
    return used_stock_list


# def update_stock_sheet():
#     """
#     Update stock data worksheet
#     """
#     stock_list = validate_stock_input()
#     print('Updating the stock sheet now...')
#     stock.append_row(stock_list)


# update_stock_sheet()

def update_adjusted_stock_sheet():
    """
    Update adjusted stock data worksheet
    """
    stock_list = validate_stock_input()
    used_stock_list = validate_used_stock_input()
    subtracted_list = []
    for stock_value, used_stock_value in zip(stock_list, used_stock_list):
        subtracted_list.append(stock_value - used_stock_value)
    print(subtracted_list)
    for num in subtracted_list:
        if num < 0:
            print('There has been an error - your calculated stock is '
                  'negative - enter stocks again')
        else:
            print('Updating the adjusted stock sheet now...')
            adj_stock.append_row(subtracted_list)
            print(num)


update_adjusted_stock_sheet()
