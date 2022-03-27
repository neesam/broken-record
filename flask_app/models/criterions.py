from ..config.mysqlconnection import connectToMySQL

class Criterion:
    db = 'rym'
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.pic_src = data['pic_src']

    @classmethod

    def get_all(cls):

        query = 'SELECT * FROM criterion ORDER BY RAND()'

        return connectToMySQL(cls.db).query_db(query)