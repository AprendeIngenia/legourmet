from flet import *

class Home(UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page

    def build(self):
        return Container(
            Column([
                Text("Bienvenido a la página de inicio", size=24, weight='bold', color='white'),
                Text("Este es el contenido de la página de inicio.", size=16, color='white')
            ]),
            padding=padding.all(20),
            #bgcolor='rgba(0, 0, 0, 0.5)',
            bgcolor='blue',
            border_radius=10,
            expand=True,
            #image_src="path/to/your/background_image_home.jpg"  # Ruta a la imagen de fondo
        )