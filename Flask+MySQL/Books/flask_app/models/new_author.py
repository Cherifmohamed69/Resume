from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE

class Author :
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

# =========================== CREATE ===================================
    @classmethod
    def create(cls,data):
        query= """INSERT INTO authors (name)
        VALUES (%(name)s);
        """
        return connectToMySQL(DATABASE).query_db(query,data)

# ========================== GET BY ID =================================
    @classmethod
    def get_by_id(cls,data):
        query=""" SELECT * FROM authors WHERE id =%(id)s
        """
        result = connectToMySQL(DATABASE).query_db(query,data)
        print(result )
        if (result):
            return cls(result[0])

# =======================GET ALL==========================
    @classmethod
    def get_all(cls):
        query=""" SELECT * FROM authors;
        """
        results =  connectToMySQL(DATABASE).query_db(query)
        all_auth=[]
        for row in results:
            all_auth.append(cls(row))
        return all_auth
