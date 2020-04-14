import urllib.request
import json


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


if __name__ == '__main__':
    print(get_bing_image_url())
