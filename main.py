import flet as ft


def main(page: ft.Page):
    page.title = "LEGOURMET"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)

    def minus_click(e):
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()

    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()

    def hola(e):
        txt_number.value = 'hola'
        page.update()

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.SMART_BUTTON, on_click=minus_click),
                txt_number,
                ft.IconButton(ft.icons.ADD, on_click=plus_click),
                ft.IconButton(ft.icons.RADIO_BUTTON_ON, on_click=hola),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )


ft.app(main)