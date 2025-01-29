import flet as ft
from screens.main_screen import HomeScreen
from screens.lisense_screen import LicenseScreen
from screens.settings_screen import SettingsScreen


def Menu(page, content_container):
    def change_view(e):
        selected_index = e.control.selected_index

        # Очистка текущего содержимого
        content_container.controls.clear()

        # В зависимости от выбранного пункта меняем содержимое
        if selected_index == 0:
            content_container.controls.append(HomeScreen(page))
        elif selected_index == 1:
            content_container.controls.append(SettingsScreen(page))
        elif selected_index == 2:
            content_container.controls.append(LicenseScreen(page))

        # Обновляем страницу
        page.update()

    rail = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        min_width=100,
        min_extended_width=200,
        group_alignment=-0.9,
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.icons.COMPUTER, selected_icon=ft.icons.COMPUTER, label="Главная"
            ),
            ft.NavigationRailDestination(
                icon_content=ft.Icon(ft.icons.SETTINGS_OUTLINED),
                selected_icon_content=ft.Icon(ft.icons.SETTINGS_ROUNDED),
                label="Настройки",
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.VPN_KEY_OUTLINED,
                selected_icon_content=ft.Icon(ft.icons.VPN_KEY_SHARP),
                label_content=ft.Text("Ключи"),
            ),
        ],
        on_change=change_view,
    )

    return ft.Row(
        [
            rail,
            ft.VerticalDivider(width=1),
            content_container,  # Контейнер для смены экранов
        ],
        width=900,
        height=310
    )


