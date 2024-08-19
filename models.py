from extensions import db
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


class User(db.Model):

    """
    This User Model has features for generating unique user id based on the UUID4 module, It has attibutes for storing, usernames, useremails, password, time user was created and date created. The following are the naming conventaions for this attributes...

            name  ==> user_name              ===> optional
            email ==> user_email             ==> required and must be unique
            password ==> user_password       ==> required
            time ==> time_created            ==> auto created
            date ==> date_created            ==> auto created
    
    The User Class model has a method for saving an instance to the database "self.save() method"

    The User Class Model has method for deleting an instance from the database with the self.delete() method
    """

    id = db.Column(db.String(255), nullable = False, primary_key = True, unique = True, default = get_random_id)
    user_name = db.Column(db.String(255))
    user_email = db.Column(db.String(255), nullable = False, unique = True)
    user_password = db.Column(db.String(255), nullable = False)
    time_created = db.Column(db.String(255), nullable = False, default = get_current_time)
    date_created = db.Column(db.String(255), nullable = False, default = get_current_date)

    def save(self):
        """Automatically Save without using the db.add and commit"""
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        """Automatically Delete without using the db.delete and commit"""

        db.session.delete(self)
        db.session.commit(self)

