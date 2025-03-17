import flet as ft

def get_settings():
    return ft.Container(
        expand=True,
        padding=20,
        bgcolor="#f5f5f5",
        border_radius=10,
        content=ft.Column(
            controls=[
                ft.Text("Configuraciones", size=24, weight="bold"),
                ft.Text("Opciones para personalizar la aplicación.", size=16),
            ]
        ),
    )
