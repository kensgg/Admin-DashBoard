import flet as ft

def get_formulario_admin(page, admin=None, on_guardar=None, on_cancelar=None):
    titulo = "Editar Administrador" if admin else "Agregar Administrador"

    # Campos del formulario
    campo_username = ft.TextField(
        width=320,
        height=45,
        hint_text="Nombre de usuario",
        value=admin["username"] if admin else "",
        border_color="#333333",
        color="#333333",
        prefix_icon=ft.icons.PERSON,
        bgcolor="#ffffff",
        border_radius=8,
    )

    campo_email = ft.TextField(
        width=320,
        height=45,
        hint_text="Correo electrónico",
        value=admin["email"] if admin else "",
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
            "_id": admin.get("_id") if admin else None,  # Cambia "id" a "_id"
            "username": campo_username.value,
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

    # Estructura del formulario
    return ft.Container(
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
                campo_email,
                campo_password,
                boton_guardar,
                boton_cancelar,
            ],
        ),
    )