from ..config.mysqlconnection import connectToMySQL
from datetime import datetime

class SOS:
    db = 'rym'
    def __init__(self, data):
        self.items_added_at = data['items_added_at']
        self.items_added_by_external_urls_spotify = data['items_added_by_external_urls_spotify']
        self.items_added_by_href = data['items_added_by_href']
        self.items_added_by_id = data['items_added_by_id']
        self.items_added_by_type = data['items_added_by_type']
        self.items_added_by_uri = data['items_added_by_uri']
        self.items_is_local = data['items_is_local']
        self.items_primary_color = data['items_primary_color']
        self.items_track_album_album_type = data['items_track_album_album_type']
        self.items_track_album_artist_0_external_urls_spotify = data['items_track_album_artists_0_external_urls_spotify']
        self.items_track_album_artists_0_href = data['items_track_album_artists_0_href']
        self.items_track_album_artists_0_id = data['items_track_album_artists_0_id']
        self.items_track_album_artists_0_name = data['items_track_album_artists_0_name']
        self.items_track_album_artists_0_type = data['items_track_album_artists_0_type']
        self.items_track_album_artists_0_uri = data['items_track_album_artists_0_uri']
        self.items_track_album_available_markets_0 = data['items_track_album_available_markets_0']
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
        self.items_track_available_markets_0 = data['items_track_available_markets_0']
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
        self.items_video_thumbnail_url = data['items_video_thumbnail_url']
        self.href = data['href']
        self.limit = data['limit']
        self.next = data['next']
        self.offset	= data['offset']
        self.previous = data['previous']
        self.total = data['total']

    