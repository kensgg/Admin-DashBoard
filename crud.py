import flet as ft

data = [
    {"id": 1, "nombre": "Ejemplo 1", "edad": 25, "correo": "ejemplo1@test.com", "telefono": "123456789"},
    {"id": 2, "nombre": "Ejemplo 2", "edad": 30, "correo": "ejemplo2@test.com", "telefono": "987654321"},
    {"id": 3, "nombre": "Ejemplo 3", "edad": 22, "correo": "ejemplo3@test.com", "telefono": "456789123"},
]

def get_crud():
    return ft.Container(
        expand=True,
        padding=20,
        bgcolor="#23243d",
        border_radius=10,
        content=ft.Column(
            spacing=20,
            expand=True,
            controls=[
                ft.Container(
                    height=120,  
                    bgcolor="#484a66",
                    border_radius=10,
                    padding=15,
                    alignment=ft.alignment.top_center,  
                    content=ft.Column(
                        alignment=ft.MainAxisAlignment.CENTER, 
                        spacing=10,
                        controls=[
                            ft.Text("Gestión de Usuarios", size=24, weight="bold", color=ft.colors.WHITE),
                            ft.Row(
                                alignment=ft.MainAxisAlignment.CENTER,
                                spacing=10,
                                controls=[
                                    ft.TextField(
                                        hint_text="Buscar por ID",
                                        bgcolor="white",
                                        border_radius=5,
                                        height=40,
                                    ),
                                    ft.IconButton(
                                        icon=ft.icons.SEARCH,
                                        icon_color="white",
                                        bgcolor="#88ddfb",
                                    ),
                                ],
                            ),
                        ],
                    ),
                ),

                # Contenedor para la tabla (centrada y expandida)
                ft.Container(
                    expand=True,  # Hace que la tabla se expanda
                    alignment=ft.alignment.top_center,  # Centrar tabla en la parte superior
                    bgcolor="#484a66",
                    border_radius=10,
                    padding=15,
                    content=ft.DataTable(
                        columns=[
                            ft.DataColumn(ft.Text("ID", weight="bold", color=ft.colors.WHITE)),
                            ft.DataColumn(ft.Text("Nombre", weight="bold", color=ft.colors.WHITE)),
                            ft.DataColumn(ft.Text("Edad", weight="bold", color=ft.colors.WHITE)),
                            ft.DataColumn(ft.Text("Correo", weight="bold", color=ft.colors.WHITE)),
                            ft.DataColumn(ft.Text("Teléfono", weight="bold", color=ft.colors.WHITE)),
                            ft.DataColumn(ft.Text("Acciones", weight="bold", color=ft.colors.WHITE)),
                        ],
                        rows=[
                            ft.DataRow(
                                cells=[
                                    ft.DataCell(ft.Text(str(item["id"]), color=ft.colors.WHITE)),
                                    ft.DataCell(ft.Text(item["nombre"], color=ft.colors.WHITE)),
                                    ft.DataCell(ft.Text(str(item["edad"]), color=ft.colors.WHITE)),
                                    ft.DataCell(ft.Text(item["correo"], color=ft.colors.WHITE)),
                                    ft.DataCell(ft.Text(item["telefono"], color=ft.colors.WHITE)),
                                    ft.DataCell(
                                        ft.Row(
                                            spacing=5,
                                            controls=[
                                                ft.IconButton(
                                                    icon=ft.icons.EDIT,
                                                    icon_color="#88ddfb",
                                                ),
                                                ft.IconButton(
                                                    icon=ft.icons.DELETE,
                                                    icon_color="red",
                                                ),
                                                ft.IconButton(  # Botón QR dentro de la tabla
                                                    icon=ft.icons.QR_CODE_SCANNER,
                                                    icon_color="white",
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            )
                            for item in data  
                        ],
                    ),
                )
            ]
        ),
    )
