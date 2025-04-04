import os
from typing import Dict, Generator, List

from ijson import items

from ..kodi import get_data_path

"""
{
"num":1,
"name":"TOP - Den of Thieves 2: Pantera (2025)",
"stream_type":"movie",
"stream_id":1301910,
"stream_icon":"https:\/\/image.tmdb.org\/t\/p\/w600_and_h900_bestv2\/p6Zz0gETvkC33Pst1h6sh9Js6x.jpg",
"rating":"6.3",
"rating_5based":3.2,
"tmdb":"604685",
"trailer":"1kmjAnvFw3I",
"added":"1738102877",
"is_adult":0,
"category_id":"92",
"category_ids":[92],
"container_extension":"mkv",
"custom_sid":null,
"direct_source":""}
"""


class Movie:
    type: str = 'movie'
    id: int = 0
    name: str = ''
    extension: str = 'mkv'
    categories: List[str] = []
    adult = False
    added: int = 0
    trailer: str = ''
    tmdb: int = 0


def parse_categories() -> Dict[int, str]:
    """Return a list of stream categories"""
    path = os.path.join(get_data_path(), 'movie_categories.json')
    result = {}
    with open(path, 'rb') as f:
        for category in items(f, 'item'):
            cid = int(category['category_id'])
            cname = category['category_name']
            result[cid] = cname
    return result


def yield_streams() -> Generator[Movie, None, None]:
    """Return JSON-STREAMS formatted data for all live channels"""
    path = os.path.join(get_data_path(), 'movie_streams.json')
    categories = parse_categories()
    with open(path, 'rb') as f:
        count = 0
        for stream in items(f, 'item'):
            if count > 100:
                break
            movie = Movie()
            movie.id = stream['stream_id']
            movie.name = stream['name']
            movie.extension = stream['container_extension']
            group_name = [categories.get(c, None) for c in stream['category_ids']]
            movie.categories = [g for g in group_name if g is not None]
            movie.tmdb = stream['tmdb']
            count += 1
            yield movie
