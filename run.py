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

donations = SHEET.worksheet('donations')

donation_data = donations.get_all_values()
print(donation_data)


def validate_abo_data():
    """
    Validate ABO input data and add to sheet
    """
    abo_inputted = False
    while abo_inputted is False:
        try:
            print('Please enter ABO in the following format: A, B, AB or O') 
            abo_input = str(input('Enter the ABO blood type entered: '))
            if (abo_input.upper() == 'A') or (abo_input.upper() == 'B') or (abo_input.upper() == 'AB') or (abo_input.upper() == 'O'):
                print(f'The blood type you entered was {abo_input.upper()}')
                abo_inputted = True
            else:
                print("You entered an invalid input")
        except ValueError:
            print("You entered an invalid input")


validate_abo_data()


def validate_rh_data():
    """
    Validate Rh input data and add to sheet
    """
    rh_inputted = False
    while rh_inputted is False:
        try:
            print('Please enter Rh status in the following format: POS or NEG') 
            rh_input = str(input('Enter the Rh status entered: '))
            if (rh_input.upper() == 'POS') or (rh_input.upper() == 'NEG'):
                print(f'The blood type you entered was {rh_input.upper()}')
                rh_inputted = True
            else:
                print("You entered an invalid input")
        except ValueError:
            print("You did not enter a string")


validate_rh_data()
