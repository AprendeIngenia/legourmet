from flet import *

class Page2(UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page

    def build(self):
        return Container(
            Column([
                Text("Bienvenido a la página 2", size=24, weight='bold', color='white'),
                Text("Este es el contenido de la página 2.", size=16, color='white')
            ]),
            padding=padding.all(20),
            #bgcolor='rgba(0, 0, 0, 0.5)',
            bgcolor='red',
            border_radius=10,
            expand=True,
            #image_src="path/to/your/background_image_page2.jpg"  # Ruta a la imagen de fondo
        )