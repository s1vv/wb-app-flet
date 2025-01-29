import inspect
import flet as ft

class CustomButtonComponent(ft.Column):
    def __init__(self, label, on_click):
        super().__init__()
        self.label = label
        self.on_click = on_click
        self.button = None 
        self.padding = ft.padding.all(4)
        

    def build(self):
        self.button = ft.CupertinoFilledButton(
            content=ft.Text(self.label),
            on_click=self.handle_click,
            padding=self.padding,
            width=260
        )
        
        return ft.Column(
            [
                self.button,  # Включаем кнопку в разметку
            ]
        )

    async def handle_click(self, e):
        """Обработчик нажатия на кнопку, запускает индикатор выполнения и выполняет функцию"""

        self.button.disabled = True
        self.button.update()


        match self.on_click:
            case None:
                print("Функция on_click не передана")

            case _ if not callable(self.on_click):
                print("on_click не является функцией")

            case _ if inspect.iscoroutinefunction(self.on_click):
                await self.on_click(e)  # Асинхронная функция

            case _:
                self.on_click(e)  # Обычная (синхронная) функция
                
        # Включаем кнопку снова после завершения выполнения функции
        self.button.disabled = False
        self.button.update()
