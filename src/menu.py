import xbmcgui
import xbmcplugin

PLUGIN_ROOT = 'plugin://plugin.video.xtream/'


def show_menu(handle: int) -> None:
    xbmcplugin.setContent(handle, 'video')
    xbmcplugin.addDirectoryItem(handle, PLUGIN_ROOT + 'movies/', xbmcgui.ListItem('Movies'), True)
    xbmcplugin.addDirectoryItem(handle, PLUGIN_ROOT + 'tvshows/', xbmcgui.ListItem('TV Shows'), True)
    xbmcplugin.endOfDirectory(handle)
