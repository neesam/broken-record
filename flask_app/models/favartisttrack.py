from ..config.mysqlconnection import connectToMySQL

class FavArtistTrack:
    db = 'rym'
    def __init__(self, data):
        self.tracks_album_album_type = data['tracks_album_album_type']
        self.tracks_album_artists_0_external_urls_spotify = data['tracks_album_artists_0_external_urls_spotify']
        self.tracks_album_artists_0_href = data['tracks_album_artists_0_href']
        self.tracks_album_artists_0_id = data['tracks_album_artists_0_id']
        self.tracks_album_artists_0_name = data['tracks_album_artists_0_name']
        self.tracks_album_artists_0_type = data['tracks_album_artists_0_type']
        self.tracks_album_artists_0_uri = data['tracks_album_artists_0_uri']
        self.tracks_album_external_urls_spotify = data['tracks_album_external_urls_spotify']
        self.tracks_album_href = data['tracks_album_href']
        self.tracks_album_id = data['tracks_album_id']
        self.tracks_album_images_0_height = data['tracks_album_images_0_height']
        self.tracks_album_images_0_url = data['tracks_album_images_0_url']
        self.tracks_album_images_0_width = data['tracks_album_images_0_width']
        self.tracks_album_name = data['tracks_album_name']
        self.tracks_album_release_date = data['tracks_album_release_date']
        self.tracks_album_release_date_precision = data['tracks_album_release_date_precision']
        self.tracks_album_total_tracks = data['tracks_album_total_tracks']
        self.tracks_album_type = data['tracks_album_type']
        self.tracks_album_uri = data['tracks_album_uri']
        self.tracks_artists_0_external_urls_spotify = data['tracks_artists_0_external_urls_spotify']
        self.tracks_artists_0_href = data['tracks_artists_0_href']
        self.tracks_artists_0_id = data['tracks_artists_0_id']
        self.tracks_artists_0_name = data['tracks_artists_0_name']
        self.tracks_artists_0_type = data['tracks_artists_0_type']
        self.tracks_artists_0_uri = data['tracks_artists_0_uri']
        self.tracks_disc_number = data['tracks_disc_number']
        self.tracks_duration_ms = data['tracks_duration_ms']
        self.tracks_explicit = data['tracks_explicit']
        self.tracks_external_ids_isrc = data['tracks_external_ids_isrc']
        self.tracks_external_urls_spotify = data['tracks_external_urls_spotify']
        self.tracks_href = data['tracks_href']
        self.tracks_id = data['tracks_id']
        self.tracks_is_local = data['tracks_is_local']
        self.tracks_is_playable = data['tracks_is_playable']
        self.tracks_name = data['tracks_name']
        self.tracks_popularity = data['tracks_popularity']
        self.tracks_preview_url = data['tracks_preview_url']
        self.tracks_track_number = data['tracks_track_number']
        self.tracks_type = data['tracks_type']
        self.tracks_uri = data['tracks_uri']
        self.favartists_artists_items_id = data['favartists_artists_items_id']