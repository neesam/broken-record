from ..config.mysqlconnection import connectToMySQL

class Brookfield:
    db = 'rym'
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.image = data['image']
        self.link = data['link']

    @classmethod

    def get_my_albums(cls):

        query = 'SELECT * FROM brookfieldcorp ORDER BY RAND()'

        results = connectToMySQL(cls.db).query_db(query)

        return results

    @classmethod

    def get_brookfield_by_id(cls, data):

        query = 'SELECT * FROM brookfieldcorp WHERE id = %(id)s'

        results = connectToMySQL(cls.db).query_db(query, data)

        return cls(results[0])

    @classmethod

    def get_sundial_albums(cls):

        query = 'SELECT * FROM sundial ORDER BY RAND()'

        results = connectToMySQL(cls.db).query_db(query)

        return results

    @classmethod

    def get_sundial_by_id(cls, data):

        query = 'SELECT * FROM sundial WHERE id = %(id)s'

        results = connectToMySQL(cls.db).query_db(query, data)

        return cls(results[0])