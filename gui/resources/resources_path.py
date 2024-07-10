from pydantic import BaseModel

from gui.resources.images.start_page.image_1 import image_1_path
from gui.resources.images.start_page.image_2 import image_2_path
from gui.resources.images.start_page.image_3 import image_3_path
from gui.resources.images.welcome_page.image_4 import image_4_path
from gui.resources.images.food_build_page.image_5 import image_5_path
from gui.resources.images.food_build_page.image_6 import image_6_path
from gui.resources.images.food_build_page.image_7 import image_7_path
from gui.resources.images.food_input_page.image_8 import image_8_path
from gui.resources.images.food_input_page.image_9 import image_9_path

from gui.resources.fonts.brittany_font import brittany_font_path
from gui.resources.fonts.cardo_font import cardo_font_path


class ImagePaths(BaseModel):
    # start page
    image_1: str = image_1_path
    image_2: str = image_2_path
    image_3: str = image_3_path
    # welcome page
    image_4: str = image_4_path
    # food build page
    image_5: str = image_5_path
    image_6: str = image_6_path
    image_7: str = image_7_path
    # food input page
    image_8: str = image_8_path
    image_9: str = image_9_path


class FontsPath(BaseModel):
    brittany_font: str = brittany_font_path
    cardo_font: str = cardo_font_path
