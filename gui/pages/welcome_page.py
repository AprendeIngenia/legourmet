from flet import *


class Welcome:
    def __init__(self, page):
        super().__init__()
        self.page = page

    def main(self):
        legourmet_watermark = Text(
            value="Legourmet by Geniiia", font_family='Poppins', size=10, weight='bold', color='#FFFFFF')
        welcome = Text("¡Bienvenidos!", font_family='Poppins', size=72, weight='bold', color='#FF7F50')
        text_2 = Text("A Legourmet, el único restaurante dirigido por inteligencia artificial.", size=24,
                      color='#00FFA3', font_family='Open sans')
        text_3 = Text("Antes de empezar con la experiencia indicanos el número de platos que deseas ordenar:", size=24,
                      color='#00FFA3', font_family='Open sans')
        gradiente = LinearGradient(
            begin=alignment.top_left, end=alignment.bottom_right, colors=['#0B0B24', '#1A1C1E'])

        food_plates_input = TextField(label='Vemos que nos acompañan # visitantes, ¿desean ordenar # platos?', adaptive=True)

        elements = Container(
            content=Column(
                [
                    Row(
                        [
                            legourmet_watermark
                        ], alignment='start'
                    ),
                    Row(
                        [
                            welcome
                        ], alignment='center'
                    ),
                    Row(
                        [
                            text_2
                        ], alignment='center'
                    ),
                    Row(
                        [
                            text_3
                        ], alignment='center'
                    ),
                    Row(
                        [
                            food_plates_input
                        ], alignment='center'
                    )
                ]
            ), gradient=gradiente, expand=True
        )
        return elements
