import flet as ft

class FilePickerComponent(ft.Column):
    def __init__(self, status_bar, page, btn_txt='select file', **kwargs):
        super().__init__(**kwargs)
        self.page = page
        self.status_bar = status_bar
        self.selected_file = ft.Text(value="No file selected", color="gray")
        self.btn_txt = btn_txt
        self.padding = ft.padding.all(4)
        self.selected_file_path = None

        
        # Кнопка выбора файла
        self.pick_file_button = ft.CupertinoFilledButton(
            content=ft.Text(self.btn_txt),
            on_click=self.pick_file,
            width=260,
            padding = self.padding
        )

        # Создание экземпляра FilePicker
        self.file_picker = ft.FilePicker(on_result=self.file_picked)

        # Добавляем компоненты в компоновку
        self.controls.append(self.pick_file_button)

    def did_mount(self):
        # Добавляем FilePicker в overlay после монтирования компонента
        self.page.overlay.append(self.file_picker)
        self.page.update()  # Обновляем страницу

    def pick_file(self, e):
        # Вызов диалога выбора файла
        self.file_picker.pick_files(allow_multiple=False)

    def file_picked(self, e: ft.FilePickerResultEvent):
        # Отправляем имя выбранного файла в статус-бар
        if e.files:
            self.selected_file_path = e.files[0].path
            self.status_bar.update_status(f"Выбран: {e.files[0].name}")
        else:
            self.status_bar.update_status("Файл не выбран")
