import flet as ft
import json

def format_json(data):
    if isinstance(data, str):
        # Если это уже строка JSON, просто возвращаем ее
        return data
    else:
        # Если это Python-объект, форматируем в JSON
        return json.dumps(data, indent=4)
        
class MultiLineStatusBar(ft.Container):
    def __init__(self, data='', **kwargs):
        # Преобразуем JSON-ответ в читаемый формат
        self.formatted_json = format_json(data)
        
        # Инициализация текстового поля
        self.status_text = ft.Text(
            value=self.formatted_json,
            selectable=True,
            expand=True,
            color=ft.colors.AMBER_500,
            max_lines=10,
            overflow=ft.TextOverflow.ELLIPSIS,
        )
        
        # Настройки контейнера
        super().__init__(
            content=self.status_text,
            # padding=10,
            height=100,
            width=800,
            bgcolor=ft.colors.BLACK,
            border=ft.border.all(1, ft.colors.GREY_400),
            border_radius=5,
            **kwargs
        )
    
    def update_status(self, new_status):
        # Обновление текста с новым значением
        self.status_text.value = new_status
        self.status_text.update()

