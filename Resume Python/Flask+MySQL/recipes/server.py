# Import the 'app' instance from the 'flask_app' module
from flask_app import app

# Import all the controllers from the 'flask_app.controllers'
from flask_app.controllers import users
from flask_app.controllers import recipes

# Check if this script is the main entry point of the program
if __name__ == '__main__':
# Run the Flask application in debug mode
    app.run(debug=True)
