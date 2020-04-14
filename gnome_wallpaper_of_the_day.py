#!/usr/bin/env python3

import subprocess
import json
import urllib.error
import urllib.request
import tempfile
import os
import sys
from get_bing_image import get_bing_image_url

def download(url):
    with tempfile.NamedTemporaryFile(delete=False) as f:
        filename, _ = urllib.request.urlretrieve(url, filename=f.name)
        return filename


def set_wallpaper(filename):
    for target in ["org.gnome.desktop.background", "org.gnome.desktop.screensaver"]:
        subprocess.run(["gsettings", "set", target, "picture-uri", filename])
        subprocess.run(["gsettings", "set", target, "picture-options", "scaled"])


if __name__ == "__main__":
    try:
        img_file = download(get_bing_image_url())
    except e:
        print(e, file=sys.stderr)
        sys.exit(1)
    set_wallpaper(img_file)
