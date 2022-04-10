from ..config.mysqlconnection import connectToMySQL

class allAlbum:
    db = 'rym'
    def __init__(self, data):
        self.albums_items_album_type = data['albums_items_album_type']
        self.albums_items_artists_0_external_urls_spotify = data['albums_items_artists_0_external_urls_spotify']
        self.albums_items_artists_0_href = data['albums_items_artists_0_href']
        self.albums_items_artists_0_id = data['albums_items_artists_0_id']
        self.albums_items_artists_0_name = data['albums_items_artists_0_name']
        self.albums_items_artists_0_type = data['albums_items_artists_0_type']
        self.albums_items_artists_0_uri = data['albums_items_artists_0_uri']
        self.albums_items_available_markets_0_ = data['albums_items_available_markets_0_']
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
        self.Column_27 = data['Column_27']
        self.Column_28 = data['Column_28']
        self.Column_29 = data['Column_29']
        self.Column_30 = data['Column_30']
        self.Column_31 = data['Column_31']
        self.Column_32 = data['Column_32']
        self.Column_33 = data['Column_33']
        self.Column_34 = data['Column_34']
        self.Column_35 = data['Column_35']
        self.Column_36 = data['Column_36']
        self.Column_37 = data['Column_37']
        self.Column_38 = data['Column_38']
        self.Column_39 = data['Column_39']
        self.Column_40 = data['Column_40']
        self.Column_41 = data['Column_41']
        self.Column_42 = data['Column_42']
        self.Column_43 = data['Column_43']
        self.Column_44 = data['Column_44']
        self.Column_45 = data['Column_45']
        self.Column_46 = data['Column_46']
        self.Column_47 = data['Column_47']
        self.Column_48 = data['Column_48']
        self.Column_49 = data['Column_49']
        self.Column_50 = data['Column_50']
        self.Column_51 = data['Column_51']
        self.Column_52 = data['Column_52']
        self.Column_53 = data['Column_53']
        self.Column_54 = data['Column_54']
        self.Column_55 = data['Column_55']
        self.Column_56 = data['Column_56']
        self.Column_57 = data['Column_57']
        self.Column_58 = data['Column_58']
        self.Column_59 = data['Column_59']
        self.Column_60 = data['Column_60']

    @classmethod

    def get_random_from_all(cls):

        query = 'SELECT * FROM all_albums ORDER BY RAND() LIMIT 1'

        results = connectToMySQL(cls.db).query_db(query)
        print(results)

        return results