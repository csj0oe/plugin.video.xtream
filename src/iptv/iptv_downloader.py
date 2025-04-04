import os
from urllib.request import urlretrieve

from ..kodi import get_data_path


def download_live_categories() -> None:
    url = 'http://host/player_api.php?username=username&password=password&action=get_live_categories'
    path = os.path.join(get_data_path(), 'live_categories.json')
    urlretrieve(url, path)


def download_live_streams() -> None:
    url = 'http://host/player_api.php?username=username&password=password&action=get_live_streams'
    path = os.path.join(get_data_path(), 'live_streams.json')
    urlretrieve(url, path)


def download_live_epg() -> None:
    url = 'http://host/xmltv.php?username=username&password=password'
    path = os.path.join(get_data_path(), 'live_epg.xml')
    urlretrieve(url, path)


def download_movies_categories() -> None:
    url = 'http://host/player_api.php?username=username&password=password&action=get_vod_categories'
    path = os.path.join(get_data_path(), 'movie_categories.json')
    urlretrieve(url, path)


def download_movies_streams() -> None:
    url = 'http://host/player_api.php?username=username&password=password&action=get_vod_streams'
    path = os.path.join(get_data_path(), 'movie_streams.json')
    urlretrieve(url, path)


def download_series_categories() -> None:
    url = 'http://host/player_api.php?username=username&password=password&action=get_series_categories'
    path = os.path.join(get_data_path(), 'series_categories.json')
    urlretrieve(url, path)


def download_series_streams() -> None:
    url = 'http://host/player_api.php?username=username&password=password&action=get_series'
    path = os.path.join(get_data_path(), 'series_streams.json')
    urlretrieve(url, path)

def download_playlist() -> None:
    url = 'http://host/get.php?username=username&password=password&type=m3u_plus&output=ts'
    path = os.path.join(get_data_path(), 'full_playlist.m3u8')
    urlretrieve(url, path)
