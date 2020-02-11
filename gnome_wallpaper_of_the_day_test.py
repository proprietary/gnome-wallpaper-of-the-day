import unittest
import os
from gnome_wallpaper_of_the_day import get_bing_image_url, download

class test_bing_image_resolution(unittest.TestCase):
    def test_fetch_urls(self):
        url = get_bing_image_url()
        self.assertTrue(len(url) > 0)


    def test_save_image(self):
        img_file = download(get_bing_image_url())
        self.assertTrue(os.stat(img_file).st_size > 0)


if __name__ == '__main__':
    unittest.main()
