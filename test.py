import os
import time

from src.iptv.iptv_downloader import download_live_categories, download_live_streams, download_live_epg, \
    download_movies_categories, download_movies_streams, download_series_categories, download_series_streams, \
    download_playlist
from src.iptv.iptvgenerator import generate_m3u8
from src.kodi import get_data_path
from src.movies.movie_parser import yield_streams


def test_download() -> None:
    t0 = time.time()
    download_live_categories()
    download_live_streams()
    download_movies_categories()
    download_movies_streams()
    download_series_categories()
    download_series_streams()
    t1 = time.time()
    download_playlist()
    t2 = time.time()
    download_live_epg()
    t3 = time.time()
    generate_m3u8()
    t4 = time.time()
    print('api = {}', t1 - t0, end='\n')
    print('get = {}', t2 - t1, end='\n')
    print('epg = {}', t3 - t2, end='\n')
    print('gen = {}', t4 - t3, end='\n')

import re

def test_movie_parse() -> None:
    path = os.path.join(get_data_path(), 'movie_list.txt')
    with open(path, 'wb') as f:
        cat = {}
        for movie in yield_streams():
            try:
                name = movie.name.replace('.', ' ')
                x = re.search('^(.+) [-:] ?(.*)', name)
                parsed_prefix = x.group(1)
                parsed_name = x.group(2)
            except:
                print(movie.name, name)
                parsed_prefix = 'ERROR'
                parsed_name = 'ERROR'
            cat[parsed_prefix] = cat.get(parsed_prefix, 0) + 1
            data = '"%s" -> "%s"\n' % (parsed_name, movie.name)
            # _ = f.write(data.encode())
        sort_cat = dict(sorted(cat.items(), key=lambda item: item[1], reverse=True))
        for c in sort_cat:
            data = '{:5d} {}\n'.format(cat[c], c)
            _ = f.write(data.encode())


if __name__ == '__main__':
    test_download()
    #test_movie_parse()
