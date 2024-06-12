from flet import *
import flet
from routes import on_route_change, on_view_pop, route_change

width = 720
height = 1280

class MenuButton(UserControl):
    def __init__(self, icon, text, width, hover_color, route, update_content):
        super().__init__()
        self.icon = icon
        self.text = text
        self.hover_color = hover_color
        self.route = route
        self.update_content = update_content
        
        self.button = Container(
            Row([
                Icon(
                    self.icon,
                    color='white',
                    size=16,
                ),
                Text(
                    self.text,
                    color='white',
                    size=16,
                    weight='w600'
                )
            ]),
            width=width,
            bgcolor=self.hover_color,
            blur=Blur(12,12,BlurTileMode.MIRROR),           
            padding=padding.only(15,10,0,10),
            border_radius=6,
            on_click=self.navigate,
        )
        
        
    def navigate(self,e):
        self.update_content(self.route)
        
    def build(self):
        return self.button

class SideBar(UserControl):
    def __init__(self,update_content,page):
        super().__init__()
        self.bgcolor= "#44000000"
        self.update_content=update_content
        self.page = page
        self.menubar=Container(
            Row([
                Container(
                    width=10,
                    height=10,
                    border_radius=360,
                    bgcolor='red'
                ),
                Container(
                    width=10,
                    height=10,
                    border_radius=360,
                    bgcolor='blue'
                ),
                Container(
                    width=10,
                    height=10,
                    border_radius=360,
                    bgcolor='green',
                    blur=Blur(12,12,BlurTileMode.MIRROR)
                ),
            ]),
            height=40,
            width=240,
            padding=padding.only(20,10,0,10),
            bgcolor=self.bgcolor,
        )
        self.body=Container(
            Column([
                self.menubar,
                Container(
                    Text("Menu",color='#999999',size=16,weight='w500'),
                    padding=padding.only(20),
                ),
                Container(
                    Column([
                        MenuButton(icons.HOME,"Home",240,self.bgcolor,"/",self.update_content),
                        MenuButton(icons.HOME,"Page 2",240,self.bgcolor,"/page2",self.update_content),
                        MenuButton(icons.CAMERA,"Test Cam",240,self.bgcolor,"/captureTest",self.update_content),
                    ]),
                    padding=padding.only(20),
                ),
                Container(
                    Row([
                        Icon(
                            icons.LIGHT_MODE,
                            color='white',
                            size=16                            
                        ),
                        Switch(
                            value=True,
                            active_color='#999999',
                            on_change=self.Mode_change,
                        ),
                        Icon(
                            icons.DARK_MODE,
                            color='#999999',
                            size=16
                        )
                    ])
                )
                
            ]),
            width=240,
            height=height,
            left=10,
            top=10,
            border_radius=6,
            bgcolor=self.bgcolor,
            blur=Blur(12,12,BlurTileMode.MIRROR),
        )
    
    def Mode_change(self,e):
        if e.control.value == True:
            self.bgcolor="#44000000"  # Color de fondo oscuro para el modo oscuro
            self.page.theme_mode = ThemeMode.DARK
        else:
            self.bgcolor="#44f4f4f4"  # Color de fondo claro para el modo claro
            self.page.theme_mode = ThemeMode.LIGHT
        self.body.bgcolor = self.bgcolor
        self.body.update()
        self.page.update()
        
    def update_pos(self,e):
        self.body.top = max(0,self.body.top+e.delta_y)
        self.body.left = max(0,self.body.left+e.delta_x)
        self.body.update()
        
        
    def build(self):
        return self.body

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

    content_container = Container(
        Column([
            Text("Mensaje Principal", size=24, weight='bold', color='white'),
            Text("Contenido de prueba", size=16, color='white')
        ]),
        padding=padding.all(5),
        bgcolor='rgba(51, 51, 51, 0.5)',
        border_radius=10,
        expand=True,
        height=height,
        left=250,
    )

    def update_content(route):
        content_container.content = route_change(page, route)
        content_container.width = page.window_width - 260  # Ajustar según el ancho de la barra lateral
        content_container.height = height
        
        content_container.update()

    page.on_route_change = on_route_change(page)
    page.on_view_pop = on_view_pop(page)

    page.add(
        Container(
            Stack([
                Image(
                    src='assets/icon.png',
                    width=page.window_width,
                    height=page.window_height,
                    left=0,
                    top=0
                ),
                SideBar(update_content,page),
                content_container
            ]),
            width=page.window_width,
            height=page.window_height,
        )
    )

flet.app(target=main)
