from ..config.mysqlconnection import connectToMySQL
from flask import request, flash

class Genre:
    db = 'rym'
    def __init__(self, data):
        self.artists_items_0_external_urls_spotify = data
        ['artists_items_0_external_urls_spotify'] 
        self.artists_items_followers_href = data['artists_items_followers_href']
        self.artists_items_followers_total = data['artists_items_followers_total']
        self.artists_items_genres_0 = data['artists_items_genres_0']
        self.artists_items_href = data['artists_items_href']
        self.artists_items_id = data['artists_items_id']
        self.artists_items_images_0_height = data['artists_items_images_0_height']
        self.artists_items_images_0_url = data['artists_items_images_0_url']
        self.artists_items_images_0_width = data['artists_items_images_0_width']
        self.artists_items_name = data['artists_items_name']
        self.artists_items_popularity = data['artists_items_popularity']
        self.artists_items_type = data['artists_items_type']
        self.artists_items_uri = data['artists_items_uri']
        self.artists_href = data['artists_href']
        self.artists_limit = data['artists_limit']
        self.artists_next = data['artists_next']
        self.artists_offset = data['artists_offset']
        self.artists_previous = data['artists_previous']
        self.artists_total = data['artists_total']

    @classmethod

    def get_alt_emo(cls):

        query = 'SELECT * FROM genre_alternative_emo ORDER BY RAND()'
        
        results = connectToMySQL(cls.db).query_db(query)

        return results

    @classmethod

    def get_pop_punk(cls):

        query = 'SELECT * FROM genre_pop_punk ORDER BY RAND()'
        
        results = connectToMySQL(cls.db).query_db(query)

        return results

    @classmethod

    def get_midwest_emo(cls):

        query = 'SELECT * FROM genre_midwest_emo ORDER BY RAND()'
        
        results = connectToMySQL(cls.db).query_db(query)

        return results

    @classmethod

    def get_indie_rock(cls):

        query = 'SELECT * FROM genre_indie_rock ORDER BY RAND()'
        
        results = connectToMySQL(cls.db).query_db(query)

        return results

    @classmethod

    def get_glitchcore(cls):

        query = 'SELECT * FROM genre_glitchcore ORDER BY RAND()'
        
        results = connectToMySQL(cls.db).query_db(query)

        return results

    @classmethod

    def get_mathrock(cls):

        query = 'SELECT * FROM genre_math_rock ORDER BY RAND()'
        
        results = connectToMySQL(cls.db).query_db(query)

        return results

    @classmethod

    def get_plugg(cls):

        query = 'SELECT * FROM genre_plugg ORDER BY RAND()'
        
        results = connectToMySQL(cls.db).query_db(query)

        return results

    @classmethod

    def get_vaporwave(cls):

        query = 'SELECT * FROM genre_vaporwave ORDER BY RAND()'
        
        results = connectToMySQL(cls.db).query_db(query)

        return results