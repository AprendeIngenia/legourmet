from pydantic import BaseModel

from gui.resources.images.start_page.image_1 import image_1_path
from gui.resources.images.start_page.image_2 import image_2_path
from gui.resources.images.start_page.image_3 import image_3_path
from gui.resources.images.welcome_page.image_4 import image_4_path
from gui.resources.images.bot import bot_image_path
from gui.resources.images.bot_shade import bot_shade_path
from gui.resources.images.brick import brick_path
from gui.resources.images.brick_2 import brick_2_path
from gui.resources.images.bricks import bricks_path
from gui.resources.images.logo_geniia import logo_geniia_path
from gui.resources.images.tapas import tapas_path
from gui.resources.images.plate import plate_path

from gui.resources.fonts.brittany_font import brittany_font_path
from gui.resources.fonts.cardo_font import cardo_font_path


class ImagePaths(BaseModel):
    # start page
    image_1: str = image_1_path
    image_2: str = image_2_path
    image_3: str = image_3_path
    image_4: str = image_4_path

    bot_img: str = bot_image_path
    bot_shade_img: str = bot_shade_path
    brick_img: str = brick_path
    brick_2_img: str = brick_2_path
    bricks_img: str = bricks_path
    logo_geniia_img: str = logo_geniia_path
    tapas_img: str = tapas_path
    plate_img: str = plate_path


class FontsPath(BaseModel):
    brittany_font: str = brittany_font_path
    cardo_font: str = cardo_font_path
