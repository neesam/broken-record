from ..config.mysqlconnection import connectToMySQL

class SOS2:
    db = 'rym'
    def __init__(self, data):
        self.input_access_token = data['input_access_token']
        self.input_playlist_id = data['input_playlist_id']
        self.input_offset = data['input_offset']
        self.items_track_album_artists_external_urls_spotify = data['items_track_album_artists_external_urls_spotify']
        self.items_track_album_artists_href = data['items_track_album_artists_href']
        self.items_track_album_artists_id = data['items_track_album_artists_id']
        self.items_track_album_artists_name = data['items_track_album_artists_name']
        self.items_track_album_artists_type = data['items_track_album_artists_type']
        self.items_track_album_artists_uri = data['items_track_album_artists_uri']
        self.items_track_album_album_type = data['items_track_album_album_type']
        self.items_track_album_external_urls_spotify = data['items_track_album_external_urls_spotify']
        self.items_track_album_href = data['items_track_album_href']
        self.items_track_album_id = data['items_track_album_id']
        self.items_track_album_images_0_height = data['items_track_album_images_0_height']
        self.items_track_album_images_0_url = data['items_track_album_images_0_url']
        self.items_track_album_images_0_width = data['items_track_album_images_0_width']
        self.items_track_album_name = data['items_track_album_name']
        self.items_track_album_release_date = data['items_track_album_release_date']
        self.items_track_album_release_date_precision = data['items_track_album_release_date_precision']
        self.items_track_album_total_tracks = data['items_track_album_total_tracks']
        self.items_track_album_type = data['items_track_album_type']
        self.items_track_album_uri = data['items_track_album_uri']
        self.items_track_artists_0_external_urls_spotify = data['items_track_artists_0_external_urls_spotify']
        self.items_track_artists_0_href = data['items_track_artists_0_href']
        self.items_track_artists_0_id = data['items_track_artists_0_id']
        self.items_track_artists_0_name = data['items_track_artists_0_name']
        self.items_track_artists_0_type = data['items_track_artists_0_type']
        self.items_track_artists_0_uri = data['items_track_artists_0_uri']
        self.items_track_disc_number = data['items_track_disc_number']
        self.items_track_duration_ms = data['items_track_duration_ms']
        self.items_track_episode = data['items_track_episode']
        self.items_track_explicit = data['items_track_explicit']
        self.items_track_external_ids_isrc = data['items_track_external_ids_isrc']
        self.items_track_external_urls_spotify = data['items_track_external_urls_spotify']
        self.items_track_href = data['items_track_href']
        self.items_track_id = data['items_track_id']
        self.items_track_is_local = data['items_track_is_local']
        self.items_track_name = data['items_track_name'] 
        self.items_track_popularity = data['items_track_popularity']
        self.items_track_preview_url = data['items_track_preview_url']
        self.items_track_track = data['items_track_track']
        self.items_track_track_number = data['items_track_track_number']
        self.items_track_type = data['items_track_type']
        self.items_track_uri = data['items_track_uri']
        self.items_added_at = data['items_added_at']
        self.items_added_by_external_urls_spotify = data['items_added_by_external_urls_spotify']
        self.items_added_by_href = data['items_added_by_href']
        self.items_added_by_id = data['items_added_by_id']
        self.items_added_by_type = data['items_added_by_type']
        self.items_added_by_uri = data['items_added_by_uri']
        self.items_is_local = data['items_is_local']
        self.items_primary_color = data['items_primary_color']
        self.items_video_thumbnail_url = data['items_video_thumbnail_url']
        self.href = data['href']
        self.limit = data['limit']
        self.next = data['next']
        self.offset = data['offset']
        self.previous = data['previous']
        self.total = data['total']

    @classmethod

    def get_all(cls):

        query = 'SELECT * FROM allsos'

        return connectToMySQL(cls.db).query_db(query)

    @classmethod

    def get_all_new_romantic(cls):

        query = 'SELECT * FROM sound_of_new_romantic ORDER BY RAND()'

        return connectToMySQL(cls.db).query_db(query)

    @classmethod 

    def get_all_dance_rock(cls):

        query = 'SELECT * FROM sound_of_dance_rock ORDER BY RAND()'

        return connectToMySQL(cls.db).query_db(query)

    @classmethod 

    def get_all_instrumentalpostrock(cls):

        query = 'SELECT * FROM sound_of_instrumental_post_rock ORDER BY RAND()'

        return connectToMySQL(cls.db).query_db(query)

    @classmethod 

    def get_all_poppunk(cls):

        query = 'SELECT * FROM sound_of_pop_punk ORDER BY RAND()'

        return connectToMySQL(cls.db).query_db(query)

    @classmethod 

    def get_all_italiandisco(cls):

        query = 'SELECT * FROM sound_of_italian_disco ORDER BY RAND()'

        return connectToMySQL(cls.db).query_db(query)

    @classmethod 

    def get_all_midwest(cls):

        query = 'SELECT * FROM sound_of_midwest_emo ORDER BY RAND()'

        return connectToMySQL(cls.db).query_db(query)

    @classmethod 

    def get_all_math_rock(cls):

        query = 'SELECT * FROM sound_of_math_rock ORDER BY RAND()'

        return connectToMySQL(cls.db).query_db(query)

    @classmethod 

    def get_all_freestyle(cls):

        query = 'SELECT * FROM the_sound_of_freestyle ORDER BY RAND()'

        return connectToMySQL(cls.db).query_db(query)

    @classmethod 

    def get_all_replay2018(cls):

        query = 'SELECT * FROM replay_2018'

        return connectToMySQL(cls.db).query_db(query)

    @classmethod 

    def get_all_replay2019(cls):

        query = 'SELECT * FROM replay_2019'

        return connectToMySQL(cls.db).query_db(query)

    @classmethod 

    def get_all_replay2015(cls):

        query = 'SELECT * FROM replay_2015'

        return connectToMySQL(cls.db).query_db(query)

    @classmethod 

    def get_all_replay2016(cls):

        query = 'SELECT * FROM replay_2016'

        return connectToMySQL(cls.db).query_db(query)

    @classmethod 

    def get_all_replay2020(cls):

        query = 'SELECT * FROM replay_2020'

        return connectToMySQL(cls.db).query_db(query)

    @classmethod 

    def get_all_replay2017(cls):

        query = 'SELECT * FROM replay_2017'

        return connectToMySQL(cls.db).query_db(query)

    @classmethod 

    def get_all_replay2021(cls):

        query = 'SELECT * FROM replay_2021'

        return connectToMySQL(cls.db).query_db(query)

    @classmethod

    def get_all_top_albums(cls):

        query = 'SELECT * FROM top_albums_playlists ORDER BY RAND() LIMIT 250'

        return connectToMySQL(cls.db).query_db(query)

    @classmethod

    def get_top_by_id(cls, data):

        query = 'SELECT * FROM top_albums_playlists WHERE items_track_album_id = %(id)s'

        results = connectToMySQL(cls.db).query_db(query, data)
        print(results)

        return cls(results[0])

    @classmethod
        
    def get_songs_from_synthpop(cls):

        query = 'SELECT * FROM the_sound_of_synthpop ORDER BY RAND()'

        return connectToMySQL(cls.db).query_db(query)

    @classmethod

    def get_synthpop_by_id(cls, data):

        query = 'SELECT * FROM the_sound_of_synthpop WHERE items_track_album_id = %(id)s'

        results = connectToMySQL(cls.db).query_db(query, data)
        print(results)

        return cls(results[0])

    @classmethod
        
    def get_songs_from_electro(cls):

        query = 'SELECT * FROM the_sound_of_electro ORDER BY RAND()'

        return connectToMySQL(cls.db).query_db(query)

    @classmethod
        
    def get_electro_by_id(cls, data):

        query = 'SELECT * FROM the_sound_of_electro WHERE items_track_album_id = %(id)s'

        results = connectToMySQL(cls.db).query_db(query, data)

        return cls(results[0])

    @classmethod
        
    def get_songs_from_altemo(cls):

        query = 'SELECT * FROM the_sound_of_alternative_emo ORDER BY RAND()'

        return connectToMySQL(cls.db).query_db(query)

    @classmethod
        
    def get_altemo_by_id(cls, data):

        query = 'SELECT * FROM the_sound_of_alternative_emo WHERE items_track_album_id = %(id)s'

        results = connectToMySQL(cls.db).query_db(query, data)

        return cls(results[0])

    @classmethod
        
    def get_songs_from_sophisti(cls):

        query = 'SELECT * FROM the_sound_of_sophisti_pop ORDER BY RAND()'

        return connectToMySQL(cls.db).query_db(query)

    @classmethod

    def get_sos_by_id(cls, data):

        query = 'SELECT * FROM allsos WHERE items_track_album_id = %(id)s'

        results = connectToMySQL(cls.db).query_db(query, data)

        return cls(results[0])