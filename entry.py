import sys
from urllib.parse import urlsplit, parse_qs

from src.kodi import log
from src.menu import show_menu
from src.video_library import show_library

if __name__ == "__main__":
    log('original %s' % sys.argv)
    path = urlsplit(sys.argv[0]).path.strip('/')
    handle = int(sys.argv[1])
    params = parse_qs(sys.argv[2][1:])
    unknown = sys.argv[3]
    log('parsed %s %s' % (path, params))
    if not path:
        show_menu(handle)
    show_library(path, params, handle)
