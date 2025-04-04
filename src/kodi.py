import xbmc
import xbmcaddon
import xbmcvfs


def error(msg: str) -> None:
    log(msg, xbmc.LOGERROR)


def log(msg: str, level=xbmc.LOGINFO) -> None:
    if hasattr(xbmc, '__kodistubs__'):
        print(msg)
    _addon_id = xbmcaddon.Addon().getAddonInfo('id')
    xbmc.log("[%s] %s" % (_addon_id, msg), level)


def get_addon_path() -> str:
    if hasattr(xbmc, '__kodistubs__'):
        import pathlib
        path = pathlib.Path().joinpath('temp').resolve()
        path.mkdir(parents=True, exist_ok=True)
        return path.as_posix()
    path = xbmcaddon.Addon().getAddonInfo('path')
    xbmcvfs.mkdirs(path)
    return xbmcvfs.translatePath(path)


def get_data_path() -> str:
    if hasattr(xbmc, '__kodistubs__'):
        import pathlib
        path = pathlib.Path().joinpath('temp').resolve()
        path.mkdir(parents=True, exist_ok=True)
        return path.as_posix()
    path = xbmcaddon.Addon().getAddonInfo('profile')
    xbmcvfs.mkdirs(path)
    return xbmcvfs.translatePath(path)
