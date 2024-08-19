from uuid import uuid4
from datetime import datetime

def get_current_date(serial=False):
    # Getting months in words
    
    """
    Returns the current date for the resource created
    The serial argument when set to true returns the current date in the format dd/mm/yy
    """
    month = ['january', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December' ]
    day = datetime.now().day
    month = datetime.now().month 
    year = datetime.now().year
    return f"{day}/{month}/{year}"
    
def get_current_time():

    """
    Returns the current time for the resource created

    """

    now = datetime.now()
    formatted_time = now.strftime("%I:%M %p")  
    return formatted_time

def get_random_id():
    """
    Returns a random string char set using the UUID4 module for the resource created

    """
    return uuid4().hex

print(get_random_id())