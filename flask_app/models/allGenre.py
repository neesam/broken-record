from ..config.mysqlconnection import connectToMySQL

class allGenre:
    db = 'rym'
    def __init__(self, data):
        self.id = data['id']
        self.genre = data['genre']
        self.image = data['image']

    @classmethod

    def get_all(cls):

        query = 'SELECT * FROM genres ORDER BY RAND()'

        return connectToMySQL(cls.db).query_db(query)
