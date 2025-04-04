import os
from typing import Dict, Generator, List

from ..kodi import get_data_path
from ijson import items


class Channel:
    type: str = 'live'
    id: int = 0
    name: str = ''
    icon: str = ''
    epg_id: str = ''
    order: int = 0
    categories: List[str] = []
    adult: bool = False
    radio: bool = False
    tv_archive: bool = False
    tv_archive_duration: int = 0
    added: int = 0
    source: str = ''


def parse_categories() -> Dict[int, str]:
    """Return a list of stream categories"""
    path = os.path.join(get_data_path(), 'live_categories.json')
    result = {}
    with open(path, 'rb') as f:
        for category in items(f, 'item'):
            cid = int(category['category_id'])
            cname = category['category_name']
            result[cid] = cname
    return result


def yield_streams() -> Generator[Channel, None, None]:
    """Return JSON-STREAMS formatted data for all live channels"""
    path = os.path.join(get_data_path(), 'live_streams.json')
    categories = parse_categories()
    with open(path, 'rb') as f:
        for stream in items(f, 'item'):
            channel = Channel()
            channel.id = stream['stream_id']
            channel.name = stream['name']
            channel.order = stream['num']
            channel.icon = stream['stream_icon']
            channel.epg_id = stream['epg_channel_id']
            channel.added = stream['added']
            channel.adult = stream['is_adult']
            group_name = [categories.get(c, None) for c in stream['category_ids']]
            channel.categories = [g for g in group_name if g is not None]
            channel.tv_archive = stream['tv_archive']
            channel.tv_archive_duration = stream['tv_archive_duration']
            channel.source = 'http://host/username/password/{}'.format(channel.id)
            yield channel
