import flet as ft
from request import agregar_usuario, eliminar_usuario, obtener_usuarios, obtener_usuario_por_id
from formulario import get_formulario

def get_crud(page, mostrar_formulario_callback):
    # Definir la tabla de usuarios
    table = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("ID", weight="bold", color=ft.colors.WHITE)),
            ft.DataColumn(ft.Text("Nombre P.", weight="bold", color=ft.colors.WHITE)),
            ft.DataColumn(ft.Text("Nombre H.", weight="bold", color=ft.colors.WHITE)),
            ft.DataColumn(ft.Text("Correo", weight="bold", color=ft.colors.WHITE)),
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

    def cargar_usuarios():
        """Carga todos los usuarios en la tabla."""
        data = obtener_usuarios()
        actualizar_tabla(data)

    def actualizar_tabla(data):
        """Actualiza la tabla con los datos proporcionados."""
        table.rows = [
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(str(item.get("_id", "")), color=ft.colors.WHITE)),
                    ft.DataCell(ft.Text(item.get("username", ""), color=ft.colors.WHITE)),
                    ft.DataCell(ft.Text(item.get("sonName", ""), color=ft.colors.WHITE)),
                    ft.DataCell(ft.Text(item.get("email", ""), color=ft.colors.WHITE)),
                    ft.DataCell(
                        ft.Row(
                            spacing=5,
                            controls=[
                                ft.IconButton(
                                    icon=ft.icons.EDIT,
                                    icon_color="#88ddfb",
                                    on_click=lambda e, id=item["_id"]: editar_usuario(id),  # Llamar a la función de edición
                                ),
                                ft.IconButton(
                                    icon=ft.icons.DELETE,
                                    icon_color="red",
                                    on_click=lambda e, id=item["_id"]: print(f"El id es: {id}"),
                                ),
                                ft.IconButton(  
                                    icon=ft.icons.QR_CODE_SCANNER,
                                    icon_color="white",
                                ),
                            ]
                        )
                    ),
                ]
            )
            for item in data
        ]
        page.update()  # Se actualiza la página para reflejar cambios

    def eliminar_y_actualizar(id_usuario):
        """Elimina un usuario y actualiza la tabla."""
        if eliminar_usuario(id_usuario):
            cargar_usuarios()
    
    def editar_usuario(id_usuario):
        usuario = obtener_usuario_por_id(id_usuario)
        print(f"Usuario obtenido: {usuario}")  # Verifica que los datos sean correctos
        if usuario:
            mostrar_formulario_callback(usuario)
        else:
            page.snack_bar = ft.SnackBar(ft.Text("Usuario no encontrado"), bgcolor="red")
            page.snack_bar.open = True
            page.update()



    def buscar_y_actualizar(e):
        """Busca un usuario por ID y actualiza la tabla."""
        id_usuario = search_field.value.strip()  # Obtener ID ingresado
        print(f"ID ingresado: {id_usuario}")  # Imprimir el valor ingresado

        if not id_usuario:
            return  # No hacer nada si el campo está vacío

        usuario = obtener_usuario_por_id(id_usuario)
        if usuario:
            actualizar_tabla([usuario])  # Mostrar solo el usuario encontrado
        else:
            page.snack_bar = ft.SnackBar(ft.Text("Usuario no encontrado"), bgcolor="red")
            page.snack_bar.open = True
            page.update()


    # Cargar los usuarios al inicio
    cargar_usuarios()

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
                                    search_field,  # Campo de búsqueda por ID
                                    ft.IconButton(
                                        icon=ft.icons.SEARCH,
                                        icon_color="white",
                                        bgcolor="#88ddfb",
                                        on_click=buscar_y_actualizar,  # Llama a la función de búsqueda
                                    ),
                                    ft.IconButton(
                                        icon=ft.icons.ADD,
                                        icon_color="white",
                                        bgcolor="#88ddfb",
                                        on_click=mostrar_formulario_callback,  # Usa el callback para mostrar el formulario
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