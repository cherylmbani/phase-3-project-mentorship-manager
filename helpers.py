from datetime import datetime
'''These are functions that help the project run successfully 
but does not define the main features
'''
def validate_phone_number(phone_number):
    '''Check if the phone number is valid. 
    the digits must be between 9 and 12, inclusive'''
    phone_number=str(phone_number)
    return phone_number.isdigit()and 9<=len(phone_number)<=12


def validate_email(email_address):
    '''CHecks if an email address contains @ and "." for
    it to be valid'''
    return "@" in email_address and "." in email_address

def validate_date(date):
    '''we parse the date in form of a string to datetime.
    %y-%m-%d means two digits of each, eg 2025-08-25, but our column date
    has four digits for year so we use capital, Y'''
    try:
        datetime.strptime(date, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def confirm_action(message="Are you sure? (y/n): "):
    """
    Asks user to confirm an action (like deleting a participant).
    Returns True if 'y' or 'Y', otherwise False.
    """
    choice = input(message).strip().lower()
    return choice == "y"




