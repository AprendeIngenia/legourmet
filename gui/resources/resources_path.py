from pydantic import BaseModel

from gui.resources.images.bot import bot_image_path
from gui.resources.images.bot_shade import bot_shade_path
from gui.resources.images.brick import brick_path
from gui.resources.images.brick_2 import brick_2_path
from gui.resources.images.bricks import bricks_path
from gui.resources.images.logo_geniia import logo_geniia_path
from gui.resources.images.tapas import tapas_path
from gui.resources.images.plate import plate_path


class ImagePaths(BaseModel):
    bot_img: str = bot_image_path
    bot_shade_img: str = bot_shade_path
    brick_img: str = brick_path
    brick_2_img: str = brick_2_path
    bricks_img: str = bricks_path
    logo_geniia_img: str = logo_geniia_path
    tapas_img: str = tapas_path
    plate_img: str = plate_path
