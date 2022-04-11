from ..config.mysqlconnection import connectToMySQL
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from flask import flash, request
from flask_app.models.rating import Rating
from flask_app.models.favartistalbum import favArtistAlbum

class User:
    db = 'rym'
    def __init__(self, data):
        self.id = data['id']
        self.email = data['email']
        self.username = data['username']
        self.password = data['password']
        self.avatar = data['avatar']
        self.listening_to = data['listening_to']
        self.ratings = []
        
    @classmethod

    def save(cls, data):

        query = 'INSERT INTO users (email, username, password, avatar, updated_at, created_at) VALUES (%(email)s, %(username)s, %(password)s, %(avatar)s, NOW(), NOW())'

        results = connectToMySQL(cls.db).query_db(query, data)

        return results

    @classmethod

    def save_listening(cls, data):

        query = 'UPDATE users SET listening_to=%(listening_to)s WHERE username = %(username)s'

        results = connectToMySQL(cls.db).query_db(query, data)

        return results

    @classmethod 

    def get_by_id(cls, data):

        query = 'SELECT * FROM users WHERE id = %(id)s'

        results = connectToMySQL(cls.db).query_db(query, data)

        if len(results) < 0:
            return False
        return cls(results[0])



    @classmethod 

    def get_by_username(cls, data):

        query = 'SELECT * FROM users WHERE username = %(username)s'

        results = connectToMySQL(cls.db).query_db(query, data)

        if len(results) < 0:
            return False
        return cls(results[0])

    @staticmethod

    def validate_registration(user):

        is_valid = True

        emailQuery = 'SELECT * FROM users WHERE email = %(email)s'
        usernameQuery = 'SELECT * FROM users WHERE username = %(username)s'

        results1 = connectToMySQL(User.db).query_db(emailQuery, user)
        results2 = connectToMySQL(User.db).query_db(usernameQuery, user)

        if len(results1) >= 1:
            flash('Email already taken. Please choose another.', 'register')
            is_valid = False
        if not EMAIL_REGEX.match(request.form['email']):
            flash('Use the correct format for emails.', 'register')
            is_valid = False
        if len(results2) >= 1:
            flash('Username already taken. Please choose another.')
            is_valid = False
        if user['password'] != user['confirm']:
            flash('Passwords must match.', 'register')
            is_valid = False
        if len(user['avatar']) == 0:
            flash('Please include an avatar', 'register')
            is_valid = False
        if len(user['username']) == 0:
            flash('Please choose a username', 'register')
            is_valid = False
        if len(user['password']) < 6:
            flash('Password must be at least six characters', 'register')
            is_valid = False
        return is_valid
        
    @staticmethod

    def validate_listening(user):

        is_valid = True

        if len(user['listening_to']) > 255:
            flash('Only 255 characters.', 'listening')
            is_valid = False
        return is_valid

    @classmethod

    def get_user_who_posted(cls):

        query = 'SELECT * FROM rym.ratings LEFT JOIN users ON rym.ratings.user_id = users.id LEFT JOIN favartistsalbums ON rym.ratings.album =  favartistsalbums.albums_items_name ORDER BY ratings.updated_at DESC'

        results = connectToMySQL(cls.db).query_db(query)
        print(results)
        all = []

        for row in results:
            rating_info = {
                'rating_id': row['rating_id'],
                'stars': row['stars'],
                'artist': row['artist'],
                'album': row['album'],
                'cover': row['cover'],
                'artist_link': row['artist_link'],
                'album_link': row['album_link'],
                'release_date': row['release_date'],
                'tracks': row['tracks'],
                'created_at': row['created_at'],
                'updated_at': row['updated_at'],
                'user_id': row['user_id'],
                'album_id': row['album_id'],
                'year': row['year'],
                'bunk': row['bunk'],
                'artist_id': row['artist_id']
            }

            user_info = {
                'username': row['username']
            }

            one_review = Rating(rating_info)
            one_review.reviewer = user_info
            print(one_review)
            all.append(one_review)
        return all


    @classmethod

    def get_user_ratings(cls, data):

        query = 'SELECT * FROM users LEFT JOIN ratings ON users.id = ratings.user_id WHERE users.id = %(id)s ORDER BY ratings.updated_at DESC' 

        results = connectToMySQL(cls.db).query_db(query, data)
        print(results)
        all = []

        for row in results:
            rating_info = {
                'rating_id': row['rating_id'],
                'stars': row['stars'],
                'artist': row['artist'],
                'album': row['album'],
                'cover': row['cover'],
                'artist_link': row['artist_link'],
                'album_link': row['album_link'],
                'release_date': row['release_date'],
                'tracks': row['tracks'],
                'created_at': row['created_at'],
                'updated_at': row['updated_at'],
                'user_id': row['user_id'],
                'album_id': row['album_id'],
                'year': row['year'],
                'bunk': row['bunk'],
                'artist_id': row['artist_id']
            }

            user_info = {
                'id': row['id'],
                'email': row['email'],
                'username': row['username'],
                'password': row['password'],
                'avatar': row['avatar'],
                'listening_to': row['listening_to']
            }

            one_rating = Rating(rating_info)
            one_reviewer = user_info
            one_rating.reviewer = one_reviewer
            all.append(one_rating)
            print(all)
        return all

    @classmethod

    def get_user_ratings_for_one_album_page(cls, data):

        query = 'SELECT * FROM users LEFT JOIN ratings ON users.id = ratings.user_id WHERE users.id = %(id)s AND ratings.album_id = %(id2)s' 

        results = connectToMySQL(cls.db).query_db(query, data)
        print(results)
        all = []

        for row in results:
            rating_info = {
                'rating_id': row['rating_id'],
                'stars': row['stars'],
                'artist': row['artist'],
                'album': row['album'],
                'cover': row['cover'],
                'artist_link': row['artist_link'],
                'album_link': row['album_link'],
                'release_date': row['release_date'],
                'tracks': row['tracks'],
                'created_at': row['created_at'],
                'updated_at': row['updated_at'],
                'user_id': row['user_id'],
                'album_id': row['album_id'],
                'year': row['year'],
                'bunk': row['bunk'],
                'artist_id': row['artist_id']
            }

            user_info = {
                'id': row['id'],
                'email': row['email'],
                'username': row['username'],
                'password': row['password'],
                'avatar': row['avatar'],
                'listening_to': row['listening_to']
            }

            one_rating = Rating(rating_info)
            one_reviewer = user_info
            one_rating.reviewer = one_reviewer
            all.append(one_rating)
            print(all)
        return all


    @classmethod

    def get_all_users(cls):

        query = 'SELECT * FROM users ORDER BY RAND()'

        results = connectToMySQL(cls.db).query_db(query)

        return results