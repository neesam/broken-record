from ..config.mysqlconnection import connectToMySQL

class myList:
    db = 'rym'
    def __init__(self, data):
        self.albums_items_album_type = data['albums_items_album_type']
        self.albums_items_artists_0_external_urls_spotify = data['albums_items_artists_0_external_urls_spotify']
        self.albums_items_artists_0_href = data['albums_items_artists_0_href']
        self.albums_items_artists_0_id = data['albums_items_artists_0_id']
        self.albums_items_artists_0_name = data['albums_items_artists_0_name']
        self.albums_items_artists_0_type = data['albums_items_artists_0_type']
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

    def get_all_mylist(cls):

        query = 'SELECT * FROM mylist ORDER BY RAND()'

        return connectToMySQL(cls.db).query_db(query)

    @classmethod

    def get_mylist_by_id(cls, data):

        query = 'SELECT * FROM mylist WHERE albums_items_id = %(id)s'

        results = connectToMySQL(cls.db).query_db(query, data)

        return cls(results[0])