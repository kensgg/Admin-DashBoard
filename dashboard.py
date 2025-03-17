import flet as ft

def get_dashboard():
    return ft.Container(
        expand=True, 
        content=ft.Column(
            spacing=20,
            expand=True,  
            controls=[
                ft.Row(
                    spacing=20,
                    controls=[
                        ft.Container(
                            height=280,  
                            padding=10,
                            bgcolor="#484a66",
                            border_radius=10,
                            expand=True,
                            content=ft.Column(
                                controls=[
                                    ft.Row(
                                        controls=[
                                            ft.Icon(ft.Icons.FLUTTER_DASH, size=50, color=ft.colors.WHITE),
                                            ft.Text("Gráfica 1", size=20, color=ft.colors.WHITE),
                                        ]
                                    )
                                ]
                            ),
                        ),
                        ft.Container(
                            height=280,  
                            padding=10,
                            bgcolor="#484a66",
                            border_radius=10,
                            expand=True,
                            content=ft.Column(
                                controls=[
                                    ft.Row(
                                        controls=[
                                            ft.Icon(ft.Icons.FLUTTER_DASH, size=50, color=ft.colors.WHITE),
                                            ft.Text("Gráfica 2", size=20, color=ft.colors.WHITE),
                                        ]
                                    )
                                ]
                            ),
                        ),
                    ],
                ),
                
                # Sección de estadísticas (se expande automáticamente)
                ft.Container(
                    bgcolor="#23243d",
                    padding=15,
                    border_radius=10,
                    expand=True,  # Se expande para ocupar el espacio restante
                    content=ft.Column(
                        expand=True,  # Hace que la columna interna se expanda
                        spacing=10,
                        controls=[
                            ft.Row(
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                controls=[
                                    ft.Text("Estadísticas de uso", size=24, weight="bold", color=ft.colors.WHITE),
                                    ft.Container(
                                        bgcolor="green",
                                        height=20,
                                        width=20,
                                        border_radius=10,
                                    ),
                                ],
                            ),
                            ft.Row(
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                controls=[
                                    ft.Text("Usuarios activos", size=18, color=ft.colors.WHITE),
                                    ft.Text("100", size=18, weight="bold", color=ft.colors.WHITE),
                                ],
                            ),
                        ],
                    ),
                ),
            ],
        ),
    )
