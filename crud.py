import flet as ft

def get_crud():
    return ft.Container(
        expand=True,
        padding=20,
        bgcolor="#e0e0e0",
        border_radius=10,
        content=ft.Column(
            controls=[
                ft.Text("CRUD de Usuarios", size=24, weight="bold"),
                ft.Text("Aquí puedes agregar, editar o eliminar registros.", size=16),
            ]
        ),
    )
