from package.setup.extensions import db
from package.utils.get_creation import get_random_id, get_current_time, get_current_date


class User(db.Model):

    """
    This User Model has features for generating unique user id based on the UUID4 module, It has attibutes for storing, usernames, useremails, password, time user was created and date created. The following are the naming conventions for this attributes...

           
            name        ==> user_name               ==> optional    |
            firstname   ==> first_name              ==> optional    |         
            lastname    ==>  last_name              ==> optional    |
            email       ==> user_email              ==> required and must be unique |
            password    ==> user_password           ==> required |
            time        ==> time_created            ==> auto created |
            date        ==> date_created            ==> auto created |
    
    The User Class model has a method for saving an instance to the database "self.save() method"

    The User Class Model has method for deleting an instance from the database with the self.delete() method
    """

    _id = db.Column(db.String(255), nullable = False, primary_key = True, unique = True, default = get_random_id)
    user_name = db.Column(db.String(255))
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    user_email = db.Column(db.String(255), nullable = False, unique = True)
    phone = db.Column(db.String(12))
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
    
    def rollback(self):
        db.session.rollback()

