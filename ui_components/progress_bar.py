import flet as ft

class ProgressComponent(ft.Column):
    def __init__(self):
        super().__init__()
        # Создаем внутренние элементы
        self.progress_bar = ft.ProgressBar(width=800, color="amber", bgcolor="#eeeeee", value=0)
        self.status_text = ft.Text(value="")

        # Добавляем элементы в Column
        self.controls = [self.progress_bar, self.status_text]

    def start_progress(self):
        """Метод для запуска индикации выполнения."""
        self.status_text.value = "В процессе..."
        self.progress_bar.value = None  # Устанавливаем в неопределенный режим
        self.update()

    def stop_progress(self):
        """Метод для остановки индикации выполнения."""
        self.status_text.value = "Готово"
        self.progress_bar.value = 0  # Сброс прогресс-бара
        self.update()

    async def perform_task_with_progress(self, task):
        """Асинхронный метод для выполнения задачи с индикацией прогресса."""
        self.start_progress()
        await task()  # Выполняем задачу
        self.stop_progress()
