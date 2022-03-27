from pyexpat import model


from ..config.mysqlconnection import connectToMySQL

class SOSGenre:
    db = 'rym'
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.url = data['url']

    @classmethod

    def get_all(cls):

        query = 'SELECT * FROM  sounds_of_spotify_genres'

        return connectToMySQL(cls.db).query_db(query)