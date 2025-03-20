import flet as ft
from navigation import get_navigation
from dashboard import get_dashboard
from crud import get_crud
from settings import get_settings
from formulario import get_formulario
from formulario_admin import get_formulario_admin

def main(page: ft.Page):
    page.bgcolor = ft.colors.WHITE
    content_area = ft.Column(expand=True)

    def change_view(e):
        index = e.control.selected_index
        if index == 0:
            content_area.controls = [get_dashboard()]
        elif index == 1:
            content_area.controls = [get_crud(page, mostrar_formulario_callback)]
        elif index == 2:
            content_area.controls = [get_settings(page, mostrar_formulario_admin_callback)]
        page.update()

    navigation_area = get_navigation(change_view)

    def mostrar_formulario_callback(usuario=None):
        content_area.controls = [get_formulario(page, usuario=usuario, on_guardar=guardar_usuario, on_cancelar=cancelar_formulario)]
        page.update()

    def mostrar_formulario_admin_callback(admin=None):
        content_area.controls = [get_formulario_admin(page, admin=admin, on_guardar=guardar_administrador, on_cancelar=cancelar_formulario_admin)]
        page.update()

    def guardar_usuario(usuario):
        from request import agregar_usuario, actualizar_usuario

        print("Usuario a guardar/actualizar:", usuario)  # 🔎 Verifica los datos enviados

        if usuario.get("id"):  # Si hay un ID, es una edición
            if actualizar_usuario(usuario):
                print("✅ Usuario actualizado correctamente")
                page.snack_bar = ft.SnackBar(ft.Text("Usuario actualizado correctamente"), bgcolor="green")
            else:
                print("❌ Error al actualizar el usuario")
                page.snack_bar = ft.SnackBar(ft.Text("Error al actualizar el usuario"), bgcolor="red")
        else:
            if agregar_usuario(usuario):
                print("✅ Usuario guardado correctamente")
                page.snack_bar = ft.SnackBar(ft.Text("Usuario guardado correctamente"), bgcolor="green")
            else:
                print("❌ Error al guardar el usuario")
                page.snack_bar = ft.SnackBar(ft.Text("Error al guardar el usuario"), bgcolor="red")
        
        content_area.controls = [get_crud(page, mostrar_formulario_callback)]
        page.snack_bar.open = True
        page.update()
        
        
    def guardar_administrador(admin):
        from request_admin import agregar_administrador, actualizar_administrador

        print("Administrador a guardar/actualizar:", admin)  # 🔎 Verifica los datos enviados
        print(f"EL id recibido es: ",admin.get("_id"))
        # Verifica si estamos editando (cuando el admin tiene un _id)
        if admin.get("_id"):  # Cambia "id" a "_id"
            # Si la contraseña está vacía, no la enviamos al servidor
            if admin.get("password") == "":
                admin.pop("password", None)  # Eliminamos la clave "password" si está vacía

            # Ahora intentamos actualizar el administrador
            if actualizar_administrador(admin):
                print("✅ Administrador actualizado correctamente")
                page.snack_bar = ft.SnackBar(ft.Text("Administrador actualizado correctamente"), bgcolor="green")
            else:
                print("❌ Error al actualizar el administrador")
                page.snack_bar = ft.SnackBar(ft.Text("Error al actualizar el administrador"), bgcolor="red")

        else:  # Si no hay _id, es un nuevo administrador (agregar)
            # Verifica que la contraseña no esté vacía antes de agregar un administrador
            if admin.get("password"):
                if agregar_administrador(admin["username"], admin["email"], admin["password"]):
                    print("✅ Administrador guardado correctamente")
                    page.snack_bar = ft.SnackBar(ft.Text("Administrador guardado correctamente"), bgcolor="green")
                else:
                    print("❌ Error al guardar el administrador")
                    page.snack_bar = ft.SnackBar(ft.Text("Error al guardar el administrador"), bgcolor="red")
            else:
                print("❌ La contraseña es obligatoria al agregar un administrador.")
                page.snack_bar = ft.SnackBar(ft.Text("La contraseña es obligatoria al agregar un administrador."), bgcolor="red")

        content_area.controls = [get_settings(page, mostrar_formulario_admin_callback)]
        page.snack_bar.open = True
        page.update()
        
    def cancelar_formulario(e):
        content_area.controls = [get_crud(page, mostrar_formulario_callback)]
        page.update()

    def cancelar_formulario_admin(e):
        content_area.controls = [get_settings(page, mostrar_formulario_admin_callback)]
        page.update()

    page.add(
        ft.Row(
            spacing=20,
            controls=[
                navigation_area,
                ft.VerticalDivider(width=1),
                content_area,
            ],
            expand=True,
        )
    )

    content_area.controls.append(get_dashboard())
    page.update()

ft.app(target=main)
