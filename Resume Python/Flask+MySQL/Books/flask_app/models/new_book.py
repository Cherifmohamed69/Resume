from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE

class Books:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    # =======================GET ALL==========================
    @classmethod
    def get_all(cls):
        query = """SELECT * FROM books;"""
        results = connectToMySQL(DATABASE).query_db(query)
        all_books=[]
        for row in results:
            all_books.append(cls(row))
        return all_books

    # =========================== CREATE ===================================
    @classmethod
    def create(cls, data):
        query = """
            INSERT INTO books (title, num_of_pages)
            VALUES (%(title)s, %(num_of_pages)s);
        """
        return connectToMySQL(DATABASE).query_db(query,data)

    
@classmethod
def get_by_id(cls, data):
        query = """SELECT * FROM books WHERE id = %(id)s;"""
        result = connectToMySQL(DATABASE).query_db(query, data)
        if result:
            return cls(result[0])

