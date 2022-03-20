from ..config.mysqlconnection import connectToMySQL
from flask_app.models import favartistalbum
from flask_app.models import favartisttrack

class favArtist:
    db = 'rym'
    def __init__(self, data):
        self.artists_href = data['artists_href']
        self.artists_items_0_external_urls_spotify = data
        ['artists_items_0_external_urls_spotify'] 
        self.artists_items_0_followers_href = data['artists_items_0_followers_href']
        self.artists_items_0_followers_total = data['artists_items_0_followers_total']
        self.artists_items_0_genres_0 = data['artists_items_0_genres_0']
        self.artists_items_0_href = data['artists_items_0_href']
        self.artists_items_0_id = data['artists_items_0_id']
        self.artists_items_0_images_0_height = data['artists_items_0_images_0_height']
        self.artists_items_0_images_0_url = data['artists_items_0_images_0_url']
        self.artists_items_0_images_0_width = data['artists_items_0_images_0_width']
        self.artists_items_0_name = data['artists_items_0_name']
        self.artists_items_0_popularity = data['artists_items_0_popularity']
        self.artists_items_0_type = data['artists_items_0_type']
        self.artists_items_0_uri = data['artists_items_0_uri']
        self.artists_limit = data['artists_limit']
        self.artists_next = data['artists_next']
        self.artists_offset = data['artists_offset']
        self.artists_previous = data['artists_previous']
        self.artists_total = data['artists_total']
        self.albums = []
        self.tracks = []
        
    @classmethod

    def get_all(cls):

        query = 'SELECT * FROM favartists ORDER BY RAND()'

        results = connectToMySQL(cls.db).query_db(query)
        print(results)

        return results

    @classmethod

    def get_by_id(cls, data):

        query = 'SELECT * FROM favartists WHERE artists_items_0_id = %(id)s'

        results = connectToMySQL(cls.db).query_db(query, data)

        return cls(results[0])

    @classmethod

    def get_artist_with_albums(cls, data):

        query = 'SELECT * FROM favartists LEFT JOIN favartistsalbums ON favartists.artists_items_0_id = favartistsalbums.favartists_artists_items_id WHERE favartists.artists_items_0_id = %(id)s ORDER BY RAND()'
        
        results = connectToMySQL(cls.db).query_db(query, data)

        artist = []

        for row in results:
            album_info = {
        'albums_items_album_type': row['albums_items_album_type'],
        'albums_items_artists_0_external_urls_spotify': row
        ['albums_items_artists_0_external_urls_spotify'], 
        'albums_items_artists_0_href': row['albums_items_artists_0_href'],
        'albums_items_artists_0_id': row['albums_items_artists_0_id'],
        'albums_items_artists_0_name': row['albums_items_artists_0_name'],
        'albums_items_artists_0_type': row['albums_items_artists_0_type'],
        'albums_items_artists_0_uri': row['albums_items_artists_0_uri'],
        'albums_items_available_markets_0': row['albums_items_available_markets_0'],
        'albums_items_external_urls_spotify': row['albums_items_external_urls_spotify'],
        'albums_items_href': row['albums_items_href'],
        'albums_items_id': row['albums_items_id'],
        'albums_items_images_0_height': row['albums_items_images_0_height'],
        'albums_items_images_0_url': row['albums_items_images_0_url'],
        'albums_items_images_0_width': row['albums_items_images_0_width'],
        'albums_items_name': row['albums_items_name'],
        'albums_items_release_dateNO': row['albums_items_release_dateNO'],
        'albums_items_release_dateYES': row['albums_items_release_dateYES'],
        'albums_items_release_date_precision': row['albums_items_release_date_precision'],
        'albums_items_total_tracks': row['albums_items_total_tracks'],
        'albums_items_type': row['albums_items_type'],
        'albums_items_uri': row['albums_items_uri'],
        'favartists_artists_items_id': row['favartists_artists_items_id']
            }
            
            artist.append(favartistalbum.favArtistAlbum(album_info))
        return artist

    @classmethod

    def get_artist_tracks(cls, data):

        query = 'SELECT * FROM favartists LEFT JOIN favartistracks ON favartists.artists_items_0_id = favartistracks.favartists_artists_items_id WHERE favartists.artists_items_0_id = %(id)s ORDER BY favartistracks.tracks_popularity DESC'

        results = connectToMySQL(cls.db).query_db(query, data)

        tracks = []

        for row in results:

            track_info = {
                'tracks_album_album_type': row['tracks_album_album_type'],
        'tracks_album_artists_0_external_urls_spotify': row['tracks_album_artists_0_external_urls_spotify'],
        'tracks_album_artists_0_href': row['tracks_album_artists_0_href'],
        'tracks_album_artists_0_id': row['tracks_album_artists_0_id'],
        'tracks_album_artists_0_name': row['tracks_album_artists_0_name'],
        'tracks_album_artists_0_type': row['tracks_album_artists_0_type'],
        'tracks_album_artists_0_uri': row['tracks_album_artists_0_uri'],
        'tracks_album_external_urls_spotify': row['tracks_album_external_urls_spotify'],
        'tracks_album_href': row['tracks_album_href'],
        'tracks_album_id': row['tracks_album_id'],
        'tracks_album_images_0_height': row['tracks_album_images_0_height'],
        'tracks_album_images_0_url': row['tracks_album_images_0_url'],
        'tracks_album_images_0_width': row['tracks_album_images_0_width'],
        'tracks_album_name': row['tracks_album_name'],
        'tracks_album_release_date': row['tracks_album_release_date'],
        'tracks_album_release_date_precision': row['tracks_album_release_date_precision'],
        'tracks_album_total_tracks': row['tracks_album_total_tracks'],
        'tracks_album_type': row['tracks_album_type'],
        'tracks_album_uri': row['tracks_album_uri'],
        'tracks_artists_0_external_urls_spotify': row['tracks_artists_0_external_urls_spotify'],
        'tracks_artists_0_href': row['tracks_artists_0_href'],
        'tracks_artists_0_id': row['tracks_artists_0_id'],
        'tracks_artists_0_name': row['tracks_artists_0_name'],
        'tracks_artists_0_type': row['tracks_artists_0_type'],
        'tracks_artists_0_uri': row['tracks_artists_0_uri'],
        'tracks_disc_number': row['tracks_disc_number'],
        'tracks_duration_ms': row['tracks_duration_ms'],
        'tracks_explicit': row['tracks_explicit'],
        'tracks_external_ids_isrc': row['tracks_external_ids_isrc'],
        'tracks_external_urls_spotify': row['tracks_external_urls_spotify'],
        'tracks_href': row['tracks_href'],
        'tracks_id': row['tracks_id'],
        'tracks_is_local': row['tracks_is_local'],
        'tracks_is_playable': row['tracks_is_playable'],
        'tracks_name': row['tracks_name'],
        'tracks_popularity': row['tracks_popularity'],
        'tracks_preview_url': row['tracks_preview_url'],
        'tracks_track_number': row['tracks_track_number'],
        'tracks_type': row['tracks_type'],
        'tracks_uri': row['tracks_uri'],
        'favartists_artists_items_id': row['favartists_artists_items_id']
            }

            tracks.append(favartisttrack.FavArtistTrack(track_info))

        return tracks