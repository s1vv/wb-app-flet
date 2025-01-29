import flet as ft
from ui_components.menu import HomeScreen, Menu
from ui_components.progress_bar import ProgressComponent

def main(page: ft.Page):
    page.title = "Flet App"
    page.window.width = 900
    page.window.height = 340


    # Создаем контейнер для смены контента
    content_container = ft.Column(expand=True)

    # Добавляем меню и контент на страницу
    page.add(Menu(page, content_container))

    # Изначально загружаем главный экран
    content_container.controls.append(HomeScreen(page))

    page.update()

ft.app(target=main)
