from typing import Dict, List

import xbmc
import xbmcgui
import xbmcplugin

from .kodi import error
from .movies.movie_parser import yield_streams, Movie

PLUGIN_ROOT = "plugin://plugin.video.xtream/"
IPTV_MOVIES = "http://host/%s/username/password/%i.%s"


def show_movies(handle):
    xbmcplugin.setContent(handle, "movies")
    for movie in yield_streams():
        item = create_movie(movie)
        xbmcplugin.addDirectoryItem(handle, item.getPath(), item, item.isFolder())
    xbmcplugin.endOfDirectory(handle)
    pass


def create_movie(movie: Movie):
    name = '%s {tmdb=%s}' % (movie.name, movie.tmdb)
    path = "%s/movies?id=%i&ext=%s" % (PLUGIN_ROOT[:-1], movie.id, movie.extension)
    item = xbmcgui.ListItem(name)
    item.setPath(path)
    item.setIsFolder(False) # test this with series
    item.setContentLookup(True) # test this when using direct link to iptv
    item.setProperty("IsPlayable", "true")
    info_tag: xbmc.InfoTagVideo = item.getVideoInfoTag()
    info_tag.setMediaType('movie')
    info_tag.setTitle(name)
    info_tag.setOriginalTitle(name)
    info_tag.setPath(path)
    info_tag.setFilenameAndPath(path)
    return item


def resolve_movie(handle: int, movie_id: int, extension: str) -> None:
    path = IPTV_MOVIES % ("movie", movie_id, extension)
    item = xbmcgui.ListItem(path=path, offscreen=True)
    xbmcplugin.setResolvedUrl(handle, True, item)


def show_library(path: str, params: Dict[str, List[str]], handle: int) -> None:
    if path == "movies":
        if "id" in params:
            movie_id = int(params["id"][0])
            extension = params["ext"][0]
            resolve_movie(handle, movie_id, extension)
        show_movies(handle)
    elif path == "series":
        error("[show_library] path unknown %s" % path)
    else:
        error("[show_library] path unknown %s" % path)
