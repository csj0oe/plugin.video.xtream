import time

import xbmc
from xbmcaddon import Addon

import src.kodi


def is_refresh_required():
    """Returns if we should trigger an update based on the settings."""
    refresh_interval = Addon.getSettingInt('refresh_interval', 24) * 3600
    last_refreshed = Addon.getSettingInt('last_refreshed', 0)
    return (last_refreshed + refresh_interval) <= time.time()


if __name__ == '__main__':
    monitor = xbmc.Monitor()
    while not monitor.abortRequested():
        # Sleep/wait for abort for 10 seconds
        if monitor.waitForAbort(60):
            # Abort was requested while waiting. We should exit
            break
        src.kodi.log("hello addon! %s" % time.time())
