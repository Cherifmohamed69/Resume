from flask_app import app
from flask import request ,render_template, redirect
from flask_app.models.new_author import Author

@app.route('/books')
def index():
    return render_template('books.html')


@app.route('/add_author', methods=['POST'])
def create():
    author_data = {
        'name': request.form["name"],
    }
    Author.create(author_data)
    return redirect('/authors')

@app.route('/authors')
def get_all():
    authors = Author.get_all()
    return render_template('authors.html', authors=authors)