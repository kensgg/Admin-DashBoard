import flet as ft
from request_admin import eliminar_administrador, obtener_administradores, obtener_administrador_por_id

def get_settings(page, mostrar_formulario_callback):
    # Definir la tabla de administradores
    table = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("ID", weight="bold", color=ft.colors.WHITE)),
            ft.DataColumn(ft.Text("Username", weight="bold", color=ft.colors.WHITE)),
            ft.DataColumn(ft.Text("Email", weight="bold", color=ft.colors.WHITE)),
            ft.DataColumn(ft.Text("Tipo de Usuario", weight="bold", color=ft.colors.WHITE)),
            ft.DataColumn(ft.Text("Acciones", weight="bold", color=ft.colors.WHITE)),
        ],
        rows=[]
    )

    # Campo de entrada para buscar
    search_field = ft.TextField(
        hint_text="Buscar por ID",
        bgcolor="white",
        border_radius=5,
        height=40,
    )

    # Función para cargar administradores
    def cargar_administradores():
        """Carga todos los administradores en la tabla."""
        data = obtener_administradores()
        actualizar_tabla(data)

    # Función para actualizar la tabla
    def actualizar_tabla(data):
        """Actualiza la tabla con los datos proporcionados."""
        table.rows = [
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(str(item.get("_id", "")), color=ft.colors.WHITE)),
                    ft.DataCell(ft.Text(item.get("username", ""), color=ft.colors.WHITE)),
                    ft.DataCell(ft.Text(item.get("email", ""), color=ft.colors.WHITE)),
                    ft.DataCell(ft.Text(item.get("tipoUsuario", ""), color=ft.colors.WHITE)),
                    ft.DataCell(
                        ft.Row(
                            spacing=5,
                            controls=[
                                ft.IconButton(
                                    icon=ft.icons.EDIT,
                                    icon_color="#88ddfb",
                                    on_click=lambda e, id=item["_id"]: editar_administrador(id),
                                ),
                                ft.IconButton(
                                    icon=ft.icons.DELETE,
                                    icon_color="red",
                                    on_click=lambda e, id=item["_id"]: eliminar_y_actualizar(id),
                                ),
                            ]
                        )
                    ),
                ]
            )
            for item in data
        ]
        page.update()

    # Función para eliminar un administrador
    def eliminar_y_actualizar(id_admin):
        """Elimina un administrador y actualiza la tabla."""
        if eliminar_administrador(id_admin):
            cargar_administradores()

    # Función para buscar y actualizar la tabla
    def buscar_y_actualizar(e):
        """Busca un administrador por ID y actualiza la tabla."""
        search_value = search_field.value.strip()
        if search_value:
            admin = obtener_administrador_por_id(search_value)
            if admin:
                actualizar_tabla([admin])
            else:
                page.snack_bar = ft.SnackBar(ft.Text("Administrador no encontrado"), bgcolor="red")
                page.snack_bar.open = True
                page.update()
        else:
            cargar_administradores()

    # Función para editar un administrador
    def editar_administrador(id_admin):
        """Carga los datos del administrador y abre el formulario de edición."""
        admin = obtener_administrador_por_id(id_admin)
        if admin:
            mostrar_formulario_callback(admin)
        else:
            page.snack_bar = ft.SnackBar(ft.Text("Administrador no encontrado"), bgcolor="red")
            page.snack_bar.open = True
            page.update()

    # Cargar administradores al inicio
    cargar_administradores()

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
                            ft.Text("Gestión de Administradores", size=24, weight="bold", color=ft.colors.WHITE),
                            ft.Row(
                                alignment=ft.MainAxisAlignment.CENTER,
                                spacing=10,
                                controls=[
                                    search_field,
                                    ft.IconButton(
                                        icon=ft.icons.SEARCH,
                                        icon_color="white",
                                        bgcolor="#88ddfb",
                                        on_click=buscar_y_actualizar,
                                    ),
                                    ft.IconButton(
                                        icon=ft.icons.ADD,
                                        icon_color="white",
                                        bgcolor="#88ddfb",
                                        on_click=lambda e: mostrar_formulario_callback(),
                                    ),
                                ],
                            ),
                        ],
                    ),
                ),
                ft.Container(
                    expand=True,
                    alignment=ft.alignment.top_center,
                    bgcolor="#484a66",
                    border_radius=10,
                    padding=15,
                    content=table,
                ),
            ]
        ),
    )