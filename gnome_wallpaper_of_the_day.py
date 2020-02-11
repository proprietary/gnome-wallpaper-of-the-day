#!/usr/bin/env python3

import subprocess
import json
import urllib.error
import urllib.request
import tempfile
import os
import sys


def get_bing_image_url():
    """Retrieve image of the day from Bing's service"""
    # TODO figure out what other locales Bing accepts
    locale = "en-US"
    url = f"https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mbl=1&mkt={locale}"
    req = urllib.request.Request(url=url)
    with urllib.request.urlopen(req) as resp:
        resp = json.loads(resp.read())
        url = "https://bing.com" + resp["images"][0]["url"]
        return url


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
