import flet as ft 

def main(page: ft.Page):
    page.window_width = 800
    page.window_height = 520
    page.padding = 0
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    page.bgcolor = "#FFFFFF"  
    
    login_container = ft.Container(
        width=400,
        height=480,
        padding=20,
        bgcolor="#23243d", 
        border_radius=15,
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
            controls=[
                ft.Image(src='logo.png', width=80),
                ft.Text("Iniciar Sesión", size=26, weight="bold", color="#FFFFFF"),  # Texto en blanco
                ft.TextField(
                    width=320,
                    height=45,
                    hint_text='Correo electrónico',
                    border_color="#333333", 
                    color='#333333',  
                    prefix_icon=ft.icons.EMAIL,
                    bgcolor="#ffffff",  
                    border_radius=8,
                ),
                ft.TextField(
                    width=320,
                    height=45,
                    hint_text='Contraseña',
                    border_color="#333333",  
                    color='#333333', 
                    prefix_icon=ft.icons.LOCK,
                    password=True,
                    can_reveal_password=True,
                    bgcolor="#ffffff",  
                    border_radius=8,
                ),
                ft.Checkbox(
                    label='Recordar contraseña',
                    check_color='#FFFFFF',  # Color de la marca de verificación
                    fill_color="#ffffff",   # Color de fondo del checkbox
                    label_style=ft.TextStyle(color="#FFFFFF")  # Color del texto en blanco
                ),
                ft.ElevatedButton(
                    text="INICIAR",
                    width=320,
                    bgcolor="#484a66",  
                    color="white", 
                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8))
                ),
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=5,
                    controls=[
                        ft.Text("¿No tiene una cuenta?", color="#FFFFFF"), 
                        ft.TextButton("Crear una cuenta", on_click=lambda e: print("Registro"),
                                    style=ft.ButtonStyle(color="white"))  
                    ]
                )
            ]
        )
    )
    
    page.add(login_container)

ft.app(target=main)