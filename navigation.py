import flet as ft

def get_navigation(on_change):
    return ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        min_width=100,
        min_extended_width=400,
        leading=ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
            controls=[
                ft.Text("Hola, Admin", size=15),
                ft.Icon(ft.Icons.FLUTTER_DASH),
            ],
        ),
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.Icons.SPACE_DASHBOARD_OUTLINED,
                selected_icon=ft.Icons.SPACE_DASHBOARD_ROUNDED,
                label="Dashboard",
            ),
            ft.NavigationRailDestination(
                icon=ft.Icons.MODE_EDIT_OUTLINED,
                selected_icon=ft.Icons.MODE_EDIT_OUTLINE,
                label="CRUD",
            ),
            ft.NavigationRailDestination(
                icon=ft.Icons.SETTINGS_OUTLINED,
                selected_icon=ft.Icons.SETTINGS,
                label="Settings",
            ),
        ],
        on_change=on_change,  # Función que maneja el cambio de sección
    )
