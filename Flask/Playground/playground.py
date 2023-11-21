from flask import Flask  ,render_template# Import Flask to allow us to create our app
app = Flask(__name__)


@app.route('/play')
def play():
    return render_template('play.html')#he will go to the folder ( templates) and searsh ( play.html)


@app.route('/play/<int:nums>/<string:color>')
def index(nums, color):
    return render_template('play.html' , num=nums, color=color)

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)