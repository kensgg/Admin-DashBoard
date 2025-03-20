import flet as ft
def get_formulario(page, usuario=None, on_guardar=None, on_cancelar=None):
    titulo = "Editar Usuario" if usuario else "Agregar Usuario"

    # Campos del formulario
    campo_username = ft.TextField(
        width=320,
        height=45,
        hint_text="Nombre de usuario",
        value=usuario["username"] if usuario else "",
        border_color="#333333",
        color="#333333",
        prefix_icon=ft.icons.PERSON,
        bgcolor="#ffffff",
        border_radius=8,
    )

    campo_son_name = ft.TextField(
        width=320,
        height=45,
        hint_text="Nombre del hijo/a",
        value=usuario["sonName"] if usuario else "",
        border_color="#333333",
        color="#333333",
        prefix_icon=ft.icons.CHILD_CARE,
        bgcolor="#ffffff",
        border_radius=8,
    )

    campo_email = ft.TextField(
        width=320,
        height=45,
        hint_text="Correo electrónico",
        value=usuario["email"] if usuario else "",
        border_color="#333333",
        color="#333333",
        prefix_icon=ft.icons.EMAIL,
        bgcolor="#ffffff",
        border_radius=8,
    )

    campo_password = ft.TextField(
        width=320,
        height=45,
        hint_text="Contraseña",
        value="",
        border_color="#333333",
        color="#333333",
        prefix_icon=ft.icons.LOCK,
        password=True,
        can_reveal_password=True,
        bgcolor="#ffffff",
        border_radius=8,
    )

    # Botones
    boton_guardar = ft.ElevatedButton(
        text="GUARDAR",
        width=320,
        bgcolor="#484a66",
        color="white",
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8)),
        on_click=lambda e: on_guardar({
            "id": usuario["_id"] if usuario else None,  # Asegúrate de usar "_id" si es el campo correcto
            "username": campo_username.value,
            "sonName": campo_son_name.value,
            "email": campo_email.value,
            "password": campo_password.value,
        }),
    )

    boton_cancelar = ft.ElevatedButton(
        text="CANCELAR",
        width=320,
        color="white",
        bgcolor="#ff3838",
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8)),
        on_click=on_cancelar,
    )

    formulario = ft.Container(
        width=400,
        padding=20,
        bgcolor="#23243d",
        border_radius=15,
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
            controls=[
                ft.Text(titulo, size=26, weight="bold", color="#FFFFFF"),
                campo_username,
                campo_son_name,
                campo_email,
                campo_password,
                boton_guardar,
                boton_cancelar,
            ],
        ),
    )

    return ft.Column(
        expand=True,
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[formulario]
            )
        ],
    )