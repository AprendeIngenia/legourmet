from flet import *
import flet
from routes import on_route_change, on_view_pop, route_change

def main(page: Page):
    # Hacer la ventana redimensionable
    page.window_resizable = True
    page.padding = 0

    # Definir dimensiones de la ventana
    page.window_max_height = 720
    page.window_max_width = 1280
    page.window_width = 1280
    page.window_height = 720
    page.theme_mode = ThemeMode.SYSTEM    

    # Redirigir a la página de inicio
    page.on_route_change = on_route_change(page)
    page.on_view_pop = on_view_pop(page)
    page.go("/")

flet.app(target=main)
