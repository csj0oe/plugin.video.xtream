import xbmcgui

from src.iptv.iptv_downloader import download_live_categories, download_live_streams, download_live_epg, \
    download_movies_categories, download_movies_streams, download_series_categories, download_series_streams
from src.iptv.iptvgenerator import generate_m3u8

if __name__ == "__main__":
    download_live_categories()
    download_live_streams()
    download_live_epg()
    generate_m3u8()
    download_movies_categories()
    download_movies_streams()
    download_series_categories()
    download_series_streams()
    dialog = xbmcgui.Dialog()
    dialog.notification('Movie Trailers', 'Finding Nemo download finished.', xbmcgui.NOTIFICATION_INFO, 5000)
