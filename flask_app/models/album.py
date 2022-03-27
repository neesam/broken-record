from ..config.mysqlconnection import connectToMySQL

class Album:
    db = 'rym'
    def __init__(self, data):
        self.id = data['RYM_Album']
        self.Name = data['Name']
        self.Title = data['Title']
        self.Release_Date = data['Release_Date']
        self.Rating = data['Rating']
        self.image = data['image']
        self.album_link = data['album_link']
        self.artist_link = data['artist_link']

    @classmethod

    def get_all(cls):

        query = 'SELECT * FROM mydata ORDER BY RAND()'

        results = connectToMySQL(cls.db).query_db(query)

        return results

    @classmethod

    def get_by_id(cls, data):

        query = 'SELECT * FROM mydata WHERE RYM_Album = %(id)s'

        results = connectToMySQL(cls.db).query_db(query, data)
        print(results)

        return cls(results[0])

    @classmethod

    def get_titles(cls):

        query = 'SELECT Title FROM mydata'

        results = connectToMySQL(cls.db).query_db(query)

        print(results)

        return results

    @classmethod

    def get_sundial_albums(cls):

        query = 'SELECT * FROM sundial ORDER BY RAND()'

        results = connectToMySQL(cls.db).query_db(query)

        return results

    @classmethod 

    def get_side_albums(cls):

        query = 'SELECT * FROM twothousandone UNION SELECT * FROM twothousandfive ORDER BY RAND() LIMIT 5'

        results = connectToMySQL(cls.db).query_db(query)

        return results