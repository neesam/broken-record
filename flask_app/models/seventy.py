from ..config.mysqlconnection import connectToMySQL

class Seventy:
    db = 'rym'
    def __init__(self, data):
        self.input_access_token = data['input_access_token']
        self.input_market = data['input_market']
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

    def get_seventyone(cls):

        query = 'SELECT * FROM seventies_years WHERE input_query = "1971.0" ORDER BY RAND()'

        return connectToMySQL(cls.db).query_db(query)

    @classmethod

    def get_seventyone_by_id(cls, data):

        query = 'SELECT * FROM seventies_years WHERE input_query = "1971.0" and albums_items_id = %(id)s' 

        results = connectToMySQL(cls.db).query_db(query, data)

        return cls(results[0])

    @classmethod

    def get_seventytwo(cls):

        query = 'SELECT * FROM seventies_years WHERE input_query = "1972.0" ORDER BY RAND()'

        return connectToMySQL(cls.db).query_db(query)

    @classmethod

    def get_seventytwo_by_id(cls, data):

        query = 'SELECT * FROM seventies_years WHERE input_query = "1972.0" and albums_items_id = %(id)s' 

        results = connectToMySQL(cls.db).query_db(query, data)

        return cls(results[0])

    @classmethod

    def get_seventythree(cls):

        query = 'SELECT * FROM seventies_years WHERE input_query = "1973.0" ORDER BY RAND()'

        return connectToMySQL(cls.db).query_db(query)

    @classmethod

    def get_seventythree_by_id(cls, data):

        query = 'SELECT * FROM seventies_years WHERE input_query = "1973.0" and albums_items_id = %(id)s' 

        results = connectToMySQL(cls.db).query_db(query, data)

        return cls(results[0])

    @classmethod

    def get_seventyfour(cls):

        query = 'SELECT * FROM seventies_years WHERE input_query = "1974.0" ORDER BY RAND()'

        return connectToMySQL(cls.db).query_db(query)

    @classmethod

    def get_seventyfour_by_id(cls, data):

        query = 'SELECT * FROM seventies_years WHERE input_query = "1974.0" and albums_items_id = %(id)s' 

        results = connectToMySQL(cls.db).query_db(query, data)

        return cls(results[0])

    @classmethod

    def get_seventyfive(cls):

        query = 'SELECT * FROM seventies_years WHERE input_query = "1975.0" ORDER BY RAND()'

        return connectToMySQL(cls.db).query_db(query)

    @classmethod

    def get_seventyfive_by_id(cls, data):

        query = 'SELECT * FROM seventies_years WHERE input_query = "1975.0" and albums_items_id = %(id)s' 

        results = connectToMySQL(cls.db).query_db(query, data)

        return cls(results[0])

    @classmethod

    def get_seventysix(cls):

        query = 'SELECT * FROM seventies_years WHERE input_query = "1976.0" ORDER BY RAND()'

        return connectToMySQL(cls.db).query_db(query)

    @classmethod

    def get_seventysix_by_id(cls, data):

        query = 'SELECT * FROM seventies_years WHERE input_query = "1976.0" and albums_items_id = %(id)s' 

        results = connectToMySQL(cls.db).query_db(query, data)

        return cls(results[0])

    @classmethod

    def get_seventyseven(cls):

        query = 'SELECT * FROM seventies_years WHERE input_query = "1977.0" ORDER BY RAND()'

        return connectToMySQL(cls.db).query_db(query)

    @classmethod

    def get_seventyseven_by_id(cls, data):

        query = 'SELECT * FROM seventies_years WHERE input_query = "1977.0" and albums_items_id = %(id)s' 

        results = connectToMySQL(cls.db).query_db(query, data)

        return cls(results[0])

    @classmethod

    def get_seventyeight(cls):

        query = 'SELECT * FROM seventies_years WHERE input_query = "1978.0" ORDER BY RAND()'

        return connectToMySQL(cls.db).query_db(query)

    @classmethod

    def get_seventyeight_by_id(cls, data):

        query = 'SELECT * FROM seventies_years WHERE input_query = "1978.0" and albums_items_id = %(id)s' 

        results = connectToMySQL(cls.db).query_db(query, data)

        return cls(results[0])

    @classmethod

    def get_seventynine(cls):

        query = 'SELECT * FROM seventies_years WHERE input_query = "1979.0" ORDER BY RAND()'

        return connectToMySQL(cls.db).query_db(query)

    @classmethod

    def get_seventynine_by_id(cls, data):

        query = 'SELECT * FROM seventies_years WHERE input_query = "1979.0" and albums_items_id = %(id)s' 

        results = connectToMySQL(cls.db).query_db(query, data)

        return cls(results[0])