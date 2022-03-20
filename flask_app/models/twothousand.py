from ..config.mysqlconnection import connectToMySQL

class twoThousand:
    db = 'rym'
    def __init__(self, data):
        self.album_type = data['album_type']
        self.artist_external_url_spotify = data['artist_external_url_spotify']
        self.artist_id = data['artist_id']
        self.artist_name = data['artist_name']
        self.album_external_url_spotify = data['album_external_url_spotify']
        self.albums_id = data['albums_id']
        self.album_image = data['album_image']
        self.albums_name = data['albums_name']
        self.release_date = data['release_date']
        self.total_tracks = data['total_tracks']

    @classmethod

    def get_twothousand(cls):

        query = 'SELECT * FROM twothousand ORDER BY RAND()'

        results = connectToMySQL(cls.db).query_db(query)

        return results

    @classmethod 

    def get_twothousand_by_id(cls, data):

        query = 'SELECT * FROM twothousand WHERE albums_id = %(id)s'

        results = connectToMySQL(cls.db).query_db(query, data)

        return cls(results[0])