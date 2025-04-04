import os

from .iptvparser import yield_streams
from ..kodi import get_data_path


def generate_m3u8() -> None:
    path = os.path.join(get_data_path(), 'live_channels.m3u8')
    with open(path, 'wb') as f:
        _ = f.write('#EXTM3U'.encode())
        for channel in yield_streams():
            # #EXTINF:0  ,Channel X
            # #EXTINF:0 Channel B
            m3u8_data = '#EXTINF:-1 tvg-name="{}"'.format(channel.name)
            if channel.epg_id:
                m3u8_data += ' tvg-id="{}"'.format(channel.epg_id)
            if channel.icon:
                m3u8_data += ' tvg-logo="{}"'.format(channel.icon)
            if channel.order:
                m3u8_data += ' tvg-chno="{}"'.format(channel.order)
            if channel.categories:
                m3u8_data += ' group-title="{}"'.format(';'.join(str(x) for x in channel.categories))
            if channel.radio:
                m3u8_data += ' radio="true"'
            if channel.tv_archive:
                m3u8_data += ' catchup="xc"'
            if channel.tv_archive_duration:
                m3u8_data += ' catchup-days="{}"'.format(channel.tv_archive_duration)
            m3u8_data += ',{}\n'.format(channel.name)
            m3u8_data += '{}\n\n'.format(channel.source)
            _ = f.write(m3u8_data.encode())
