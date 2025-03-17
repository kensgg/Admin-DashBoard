import flet as ft
from navigation import get_navigation
from dashboard import get_dashboard
from crud import get_crud
from settings import get_settings

def main(page: ft.Page):
    page.bgcolor = ft.colors.WHITE

    content_area = ft.Column(expand=True)

    def change_view(e):
        """Cambia el contenido de la interfaz al seleccionar en la barra de navegación."""
        index = e.control.selected_index
        if index == 0:
            content_area.controls = [get_dashboard()]
        elif index == 1:
            content_area.controls = [get_crud()]
        elif index == 2:
            content_area.controls = [get_settings()]
        page.update()

    page.add(
        ft.Row(
            spacing=20,
            controls=[
                get_navigation(change_view), 
                ft.VerticalDivider(width=1),
                content_area,  
            ],
            expand=True,
        )
    )
    content_area.controls.append(get_dashboard())
    page.update()

ft.app(target=main)
