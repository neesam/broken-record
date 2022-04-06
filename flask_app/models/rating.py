from ..config.mysqlconnection import connectToMySQL
from flask_app.models import genre
from flask import flash


class Rating:
    db = 'rym'
    def __init__(self, data): 
        self.id = data['id']
        self.stars = data['stars']
        self.artist = data['artist']
        self.album = data['album']
        self.cover = data['cover']
        self.artist_link = data['artist_link']
        self.album_link = data['album_link']
        self.release_date = data['release_date']
        self.tracks = data['tracks']
        self.reviewer = None
        self.genres = []
        self.album_info = None
        self.user_id = data['user_id']
        self.album_id = data['album_id']
        self.year = data['year']
        self.bunk = data['bunk']
        self.artist_id = data['artist_id']

    @classmethod 

    def get_all(cls):

        query = 'SELECT * FROM ratings'

        results = connectToMySQL(cls.db).query_db(query)

        return results

    @classmethod 

    def get_by_id(cls, data):

        query = 'SELECT * FROM ratings WHERE id = %(id)s'

        results = connectToMySQL(cls.db).query_db(query, data)

        return cls(results[0])

    @classmethod

    def get_all_ratings_for_one_album(cls, data):

        query = 'SELECT * FROM ratings WHERE album_id = %(id)s'

        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod

    def save(cls, data):

        query = 'INSERT INTO ratings (stars, artist, album, cover, year, artist_link, album_link, release_date, tracks, album_id, created_at, updated_at, bunk, artist_id, user_id) VALUES (%(stars)s, %(artist)s, %(album)s, %(cover)s,  %(year)s, %(artist_link)s, %(album_link)s, %(release_date)s, %(tracks)s, %(album_id)s, NOW(), NOW(), %(bunk)s, %(artist_id)s, %(user_id)s)'

        results = connectToMySQL(cls.db).query_db(query, data)
        print(results)

        return results

    @classmethod

    def destroy(cls, data):

        query = 'DELETE FROM ratings WHERE ratings.id = %(id)s'

        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    
    def update_rating(cls, data):

        query = 'UPDATE ratings SET stars=%(stars)s, artist=%(artist)s, album=%(album)s, cover=%(cover)s, year=%(year)s, artist_link=%(artist_link)s, album_link=%(album_link)s, release_date=%(release_date)s, tracks=%(tracks)s, album_id=%(album_id)s, artist_id=%(artist_id)s, bunk=%(bunk)s, updated_at=NOW() WHERE ratings.id = %(id)s'
        

        results = connectToMySQL(cls.db).query_db(query, data)

        return results

    @classmethod

    def get_all_stars(cls):

        query = 'SELECT rating FROM ratings'

        results = connectToMySQL(cls.db).query_db(query)

        return results

    @classmethod 

    def get_all_rating_genres(cls, data):

        query = 'SELECT * FROM ratings LEFT JOIN ratings_has_genres ON ratings.id = ratings_has_genres.rating_id LEFT JOIN genres ON genres.id = ratings_has_genres.genre_id WHERE ratings.id = %(id)s'

        results = connectToMySQL(cls.db).query_db(query, data)

        rating = cls(results[0])

        for row in results:

            genre_data = {
                'id': row['genres.id'],
                'type': row['type'],
                'created_at': row['genres.created_at'],
                'updated_at': row['genres.updated_at']
            }
            rating.genres.append(genre.Genre(genre_data))
        return rating

    # @staticmethod

    # def validate_content_length(rating):

    #     is_valid = True

    #     if len(rating['content']) > 295:
    #         flash('Only 295 characters.', 'content')
    #         is_valid = False
    #     return is_valid