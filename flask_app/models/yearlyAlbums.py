from ..config.mysqlconnection import connectToMySQL

class yearlyAlbums:
    db = 'rym'
    def __init__(self, data):
        self.album_type = data['albums_items_album_type']
        self.artist_external_url_spotify = data
        ['albums_items_artists_0_external_urls_spotify'] 
        self.albums_items_artists_0_href = data['albums_items_artists_0_href']
        self.artist_id = data['albums_items_artists_0_id']
        self.artist_name = data['albums_items_artists_0_name']
        self.albums_items_artists_0_type = data['albums_items_artists_0_type']
        self.albums_items_artists_0_uri = data['albums_items_artists_0_uri']
        self.album_external_url_spotify = data['albums_items_external_urls_spotify']
        self.albums_items_href = data['albums_items_href']
        self.albums_items_id = data['albums_items_id']
        self.albums_items_images_0_height = data['albums_items_images_0_height']
        self.album_image = data['albums_items_images_0_url']
        self.albums_items_images_0_width = data['albums_items_images_0_width']
        self.album_name = data['albums_items_name']
        self.album_release_date = data['albums_items_release_date']
        self.albums_items_release_date_precision = data['albums_items_release_date_precision']
        self.year = data['year']
        self.total_tracks = data['albums_items_total_tracks']
        self.albums_items_type = data['albums_items_type']
        self.albums_items_uri = data['albums_items_uri']
        self.albums_href = data['albums_href']
        self.albums_limit = data['albums_limit']
        self.albums_next = data['albums_next']
        self.albums_offset = data['albums_offset']
        self.albums_previous = data['albums_previous']
        self.albums_total = data['albums_total']

    @classmethod

    def get_twothousand(cls):

        query = 'SELECT * FROM twothousand ORDER BY RAND()'

        results = connectToMySQL(cls.db).query_db(query)

        return results

    @classmethod

    def get_random_from_all(cls):

        query = 'SELECT * FROM all_albums LIMIT 1'

        results = connectToMySQL(cls.db).query_db(query)

        return cls(results[0])

    @classmethod 

    def get_twothousand_by_id(cls, data):

        query = 'SELECT * FROM twothousand WHERE albums_items_id = %(id)s'

        results = connectToMySQL(cls.db).query_db(query, data)

        return cls(results[0])

    @classmethod 

    def get_twothousandone(cls):

        query = 'SELECT * FROM twothousandone ORDER BY RAND()'

        results = connectToMySQL(cls.db).query_db(query)

        return results

    @classmethod 

    def get_twothousandone_by_id(cls, data):

        query = 'SELECT * FROM twothousandone WHERE albums_items_id = %(id)s'

        results = connectToMySQL(cls.db).query_db(query, data)
        print(results)

        return cls(results[0])

    @classmethod 

    def get_twothousandtwo(cls):

        query = 'SELECT * FROM twothousandtwo ORDER BY RAND()'

        results = connectToMySQL(cls.db).query_db(query)

        return results

    @classmethod 

    def get_twothousandtwo_by_id(cls, data):

        query = 'SELECT * FROM twothousandtwo WHERE albums_items_id = %(id)s'

        results = connectToMySQL(cls.db).query_db(query, data)

        return cls(results[0])

    @classmethod 

    def get_twothousandthree(cls):

        query = 'SELECT * FROM twothousandthree ORDER BY RAND()'

        results = connectToMySQL(cls.db).query_db(query)

        return results

    @classmethod 

    def get_twothousandthree_by_id(cls, data):

        query = 'SELECT * FROM twothousandthree WHERE albums_items_id = %(id)s'

        results = connectToMySQL(cls.db).query_db(query, data)

        return cls(results[0])

    @classmethod 

    def get_twothousandfour(cls):

        query = 'SELECT * FROM twothousandfour ORDER BY RAND()'

        results = connectToMySQL(cls.db).query_db(query)

        return results

    @classmethod 

    def get_twothousandfour_by_id(cls, data):

        query = 'SELECT * FROM twothousandfour WHERE albums_items_id = %(id)s'

        results = connectToMySQL(cls.db).query_db(query, data)
        print(results)

        return cls(results[0])

    @classmethod 

    def get_twothousandfive(cls):

        query = 'SELECT * FROM twothousandfive ORDER BY RAND()'

        results = connectToMySQL(cls.db).query_db(query)

        return results

    @classmethod 

    def get_twothousandfive_by_id(cls, data):

        query = 'SELECT * FROM twothousandfive WHERE albums_items_id = %(id)s'

        results = connectToMySQL(cls.db).query_db(query, data)
        print(results)

        return cls(results[0])

    @classmethod 

    def get_twothousandsix(cls):

        query = 'SELECT * FROM twothousandsix ORDER BY RAND()'

        results = connectToMySQL(cls.db).query_db(query)

        return results

    @classmethod 

    def get_twothousandsix_by_id(cls, data):

        query = 'SELECT * FROM twothousandsix WHERE albums_items_id = %(id)s'

        results = connectToMySQL(cls.db).query_db(query, data)
        print(results)

        return cls(results[0])

    @classmethod 

    def get_twothousandseven(cls):

        query = 'SELECT * FROM twothousandseven ORDER BY RAND()'

        results = connectToMySQL(cls.db).query_db(query)

        return results

    @classmethod 

    def get_twothousandseven_by_id(cls, data):

        query = 'SELECT * FROM twothousandseven WHERE albums_items_id = %(id)s'

        results = connectToMySQL(cls.db).query_db(query, data)
        print(results)

        return cls(results[0])

    @classmethod
    
    def get_side_albums(cls):

        query = 'SELECT * FROM all_albums ORDER BY RAND() LIMIT 5'

        results = connectToMySQL(cls.db).query_db(query)

        return results