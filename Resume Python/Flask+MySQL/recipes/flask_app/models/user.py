# Import necessary modules and classes
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
import re
# Regular expression for validating email addresses
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')




# ==================User class for interacting with the 'users' table in the database=======================

class User:
    def __init__(self, data):
        # Initialize user attributes with data from the database
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']



#=================== Class method to create a new user in the database============================
    @classmethod
    def create_user(cls, data):
        query = """
        INSERT INTO users (first_name, last_name, email, password) 
        VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);
        """
        return connectToMySQL(DATABASE).query_db(query, data)

    # Representation method for displaying user information
    def __repr__(self) -> str:
        return f"{self.first_name}--{self.last_name}--{self.email}"



# ============================Class method to retrieve a user by their ID===================

    @classmethod
    def get_by_id(cls, data):
        query = """
        SELECT * FROM users WHERE id = %(id)s;
        """
        result = connectToMySQL(DATABASE).query_db(query, data)
        return cls(result[0])




#================Class method to retrieve a user by their email===============

    @classmethod
    def get_by_email(cls, data):
        query = """
        SELECT * FROM users WHERE email = %(email)s;
        """
        result = connectToMySQL(DATABASE).query_db(query, data)
        # Check if a user with the given email exists
        if result:
            return cls(result[0])
        return False

#============== Static method to validate user registration data=================

    @staticmethod
    def validate(data):
        is_valid = True
        # Check first name length
        if len(data['first_name']) < 2:
            flash("First Name must be at least 2 characters", "reg")
            is_valid = False
        # Check last name length
        if len(data['last_name']) < 2:
            flash("Last name is required", "reg")
            is_valid = False
        # Validate email format
        if not EMAIL_REGEX.match(data['email']):
            flash("Invalid email address!", "reg")
            is_valid = False
        # Check if email is already in use
        elif User.get_by_email({'email': data['email']}):
            flash("Email address already used, try login", "reg")
            is_valid = False
        # Check password length
        if len(data['password']) < 6:
            flash("Password too short", "reg")
            is_valid = False
        # Check if password matches confirmation
        elif data['password'] != data['confirm_password']:
            flash("Password does not match", "reg")
            is_valid = False
        return is_valid
