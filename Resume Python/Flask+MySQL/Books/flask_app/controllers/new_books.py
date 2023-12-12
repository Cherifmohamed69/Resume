from flask_app import app
from flask import request ,render_template, redirect
from flask_app.models.new_book import Books

@app.route('/books')
def get_all():
    books = Books.get_all()
    return render_template('books.html', books=books)


@app.route('/authors')
def Hom():
    return render_template('authors.html')

@app.route('/add_book', methods=['POST'])
def create():
    books_data = {
        'title': request.form["title"],
        'num_of_pages': request.form["num_of_pages"],
    }
    Books.create(books_data)
    return redirect('/books')





