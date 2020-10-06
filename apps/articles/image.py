from PIL import Image

from kennisdeler.settings import base


class Imaging:
    """Edit and modify images"""
    def __init__(self, url):
        self.img = Image.open(url)
        self.short_url = url
        self.url = f"{base.MEDIA_ROOT}/{url}"
        self.height, self.width = self.img.size

    def resize_by_max(self, new_width=0, new_height=0):
        ratio = self.height / self.width

        if new_width & new_height:
            image = self.img.resize(
                (int(new_width), int(new_height)),
                Image.ANTIALIAS
            )
            image.save(self.url)

        elif new_width:
            image = self.img.resize(
                (int(new_width * ratio), new_width),
                Image.ANTIALIAS
            )
            image.save(self.url)

        elif new_height:
            image = self.img.resize(
                (new_height, int(new_height * ratio)),
                Image.ANTIALIAS
            )
            image.save(self.url)
