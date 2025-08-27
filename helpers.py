'''These are functions that help the project run successfully 
but does not define the main features
'''
def validate_phone_number(phone_number):
    '''Check if the phone number is valid. 
    the digits must be between 9 and 12, inclusive'''
    phone_number=str(phone_number)
    return phone_number.isdigit()and 9<=len(phone_number)<=12