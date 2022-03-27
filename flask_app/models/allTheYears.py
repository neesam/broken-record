from ..config.mysqlconnection import connectToMySQL

class allTheYear:
    db = 'rym'
    def __init__(self, data):
        self.input_access_token = data['input_access_token']
        self.input_type = data['input_type']
        self.input_query = data['input_query']
        self.input_offset = data['input_offset']
        self.albums_items_album_type = data['albums_items_album_type']
        self.albums_items_artists_0_external_urls_spotify = data['albums_items_artists_0_external_urls_spotify']
        self.albums_items_artists_0_href = data['albums_items_artists_0_href']
        self.albums_items_artists_0_id = data['albums_items_artists_0_id']
        self.albums_items_artists_0_name = data['albums_items_artists_0_name']        
        self.albums_items_artists_0_type = data['albums_items_artists_0_type']
        self.albums_items_artists_0_uri = data['albums_items_artists_0_uri']
        self.albums_items_available_markets_0 = data['albums_items_available_markets_0'] 
        self.albums_items_external_urls_spotify = data['albums_items_external_urls_spotify']
        self.albums_items_href = data['albums_items_href']
        self.albums_items_id = data['albums_items_id']
        self.albums_items_images_0_height = data['albums_items_images_0_height']
        self.albums_items_images_0_url = data['albums_items_images_0_url']
        self.albums_items_images_0_width = data['albums_items_images_0_width']
        self.albums_items_name = data['albums_items_name']
        self.albums_items_release_date = data['albums_items_release_date']
        self.albums_items_release_date_precision = data['albums_items_release_date_precision']
        self.albums_items_total_tracks = data['albums_items_total_tracks']
        self.albums_items_type = data['albums_items_type']
        self.albums_items_uri = data['albums_items_uri']
        self.albums_href = data['albums_href']
        self.albums_limit = data['albums_limit']
        self.albums_next = data['albums_next']
        self.albums_offset = data['albums_offset']
        self.albums_previous = data['albums_previous']
        self.albums_total = data['albums_total']

    @classmethod

    def get_sixty(cls):

        query = 'SELECT * FROM sixties_years WHERE input_query = "1960" ORDER BY RAND()'

        return connectToMySQL(cls.db).query_db(query)

    @classmethod

    def get_sixty_by_id(cls, data):

        query = 'SELECT * FROM sixties_years WHERE  input_query = "1960" and albums_items_id = %(id)s' 

        results = connectToMySQL(cls.db).query_db(query, data)

        return cls(results[0])

    @classmethod

    def get_sixtyone(cls):

        query = 'SELECT * FROM sixties_years WHERE input_query = "1961" ORDER BY RAND()'

        return connectToMySQL(cls.db).query_db(query)

    @classmethod

    def get_sixtyone_by_id(cls, data):

        query = 'SELECT * FROM sixties_years WHERE  input_query = "1961" and albums_items_id = %(id)s' 

        results = connectToMySQL(cls.db).query_db(query, data)

        return cls(results[0])

    @classmethod

    def get_sixtythree(cls):

        query = 'SELECT * FROM sixties_years WHERE input_query = "1963" ORDER BY RAND()'

        return connectToMySQL(cls.db).query_db(query)

    @classmethod

    def get_sixtythree_by_id(cls, data):

        query = 'SELECT * FROM sixties_years WHERE  input_query = "1963" and albums_items_id = %(id)s' 

        results = connectToMySQL(cls.db).query_db(query, data)

        return cls(results[0])

    @classmethod

    def get_sixtyfour(cls):

        query = 'SELECT * FROM sixties_years WHERE input_query = "1964" ORDER BY RAND()'

        return connectToMySQL(cls.db).query_db(query)

    @classmethod

    def get_sixtyfour_by_id(cls, data):

        query = 'SELECT * FROM sixties_years WHERE  input_query = "1964" and albums_items_id = %(id)s' 

        results = connectToMySQL(cls.db).query_db(query, data)

        return cls(results[0])

    @classmethod

    def get_sixtyfive(cls):

        query = 'SELECT * FROM sixties_years WHERE input_query = "1965" ORDER BY RAND()'

        return connectToMySQL(cls.db).query_db(query)

    @classmethod

    def get_sixtyfive_by_id(cls, data):

        query = 'SELECT * FROM sixties_years WHERE  input_query = "1965" and albums_items_id = %(id)s' 

        results = connectToMySQL(cls.db).query_db(query, data)

        return cls(results[0])

    @classmethod

    def get_sixtysix(cls):

        query = 'SELECT * FROM sixties_years WHERE input_query = "1966" ORDER BY RAND()'

        return connectToMySQL(cls.db).query_db(query)

    @classmethod

    def get_sixtysix_by_id(cls, data):

        query = 'SELECT * FROM sixties_years WHERE  input_query = "1966" and albums_items_id = %(id)s' 

        results = connectToMySQL(cls.db).query_db(query, data)

        return cls(results[0])

    @classmethod

    def get_sixtyseven(cls):

        query = 'SELECT * FROM sixties_years WHERE input_query = "1967" ORDER BY RAND()'

        return connectToMySQL(cls.db).query_db(query)

    @classmethod

    def get_sixtyseven_by_id(cls, data):

        query = 'SELECT * FROM sixties_years WHERE  input_query = "1967" and albums_items_id = %(id)s' 

        results = connectToMySQL(cls.db).query_db(query, data)

        return cls(results[0])

    @classmethod

    def get_sixtyeight(cls):

        query = 'SELECT * FROM sixties_years WHERE input_query = "1968" ORDER BY RAND()'

        return connectToMySQL(cls.db).query_db(query)

    @classmethod

    def get_sixtyeight_by_id(cls, data):

        query = 'SELECT * FROM sixties_years WHERE  input_query = "1968" and albums_items_id = %(id)s' 

        results = connectToMySQL(cls.db).query_db(query, data)

        return cls(results[0])

    @classmethod

    def get_sixtynine(cls):

        query = 'SELECT * FROM sixties_years WHERE input_query = "1969" ORDER BY RAND()'

        return connectToMySQL(cls.db).query_db(query)

    @classmethod

    def get_sixtynine_by_id(cls, data):

        query = 'SELECT * FROM sixties_years WHERE  input_query = "1969" and albums_items_id = %(id)s' 

        results = connectToMySQL(cls.db).query_db(query, data)

        return cls(results[0])