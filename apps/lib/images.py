"""
Modify images
"""
from io import BytesIO

from PIL import Image, ImageOps

from django.core.files import File


class Imaging:
    """Modify images and return a django friendly object"""
    def __init__(self, image: object):
        self.image = image
        self.img = Image.open(image)
        self.img.convert('RGB')
        self.height, self.width = self.img.size

    def resize_by_max(self, new_width=0, new_height=0):
        """Resize by either width or height maintaining aspect ratio"""
        ratio = self.height / self.width

        if new_width:
            self.img = self.img.resize(
                (int(new_width * ratio), new_width),
                Image.ANTIALIAS
            )

        elif new_height:
            self.img = self.img.resize(
                (new_height, int(new_height * ratio)),
                Image.ANTIALIAS
            )

    def save_image(self) -> object:
        """Save the image and return the object"""
        ImageOps.exif_transpose(self.img)
        img_io = BytesIO()
        self.img.save(img_io, 'JPEG', quality=85)
        image_object = File(img_io, name=self.image.name)
        return image_object
