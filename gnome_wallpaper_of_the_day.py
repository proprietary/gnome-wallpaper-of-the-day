#!/usr/bin/env python3

# WOTD -- Wallpaper Of The Day
# Get a new wallpaper every day for the GNOME desktop environment for GNU/Linux
#
# Zelly Snyder <zelly@outlook.com>

import subprocess
import json
import urllib.error
import urllib.request
import tempfile
import os
import sys
from get_bing_image import get_bing_image_url
from time import sleep
import shutil


def download(url):
    with tempfile.NamedTemporaryFile(delete=False) as f:
        filename, _ = urllib.request.urlretrieve(url, filename=f.name)
        return filename


def set_wallpaper(filename):
    for target in ["org.gnome.desktop.background", "org.gnome.desktop.screensaver"]:
        subprocess.run(["gsettings", "set", target, "picture-uri", filename])
        subprocess.run(["gsettings", "set", target, "picture-options", "scaled"])


if __name__ == "__main__":
    done = False
    backoff = 30
    while done is False:
        try:
            img_file = download(get_bing_image_url())
        except urllib.error.URLError as e:
            # Keep trying until network comes back
            print(e, file=sys.stderr)
            sleep(backoff)
            backoff *= 2
        else:
            # Save permanently to a specified path
            # By default, for now, the path is $XDG_DATA_HOME/wotd/wallpaper.jpg
            home = os.path.expanduser("~")
            xdg_data_home = os.environ.get("XDG_DATA_HOME") or os.path.join(
                home, ".local", "share"
            )
            DATA_DIR = os.path.join(xdg_data_home, "wotd")
            try:
                os.mkdir(DATA_DIR)
            except FileExistsError:
                pass
            wallpaper_path = os.path.join(DATA_DIR, "wallpaper.jpg")
            try:
                os.remove(wallpaper_path)
            except OSError:
                pass
            shutil.move(img_file, wallpaper_path)
            done = True
    set_wallpaper(wallpaper_path)
