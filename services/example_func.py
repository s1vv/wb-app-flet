import asyncio


async def  example_func(status_bar, e):
    print("Button clicked, executing example function...")
    await asyncio.sleep(5)  # Эмуляция выполнения функции
    status_bar.update_status('1')
    await asyncio.sleep(3)  # Эмуляция выполнения функции
    status_bar.update_status('2')

    # Отправка события для обновления статуса
    print("Function complete")


def handle_text_input(value):
    print(f"Полученное значение: {value}")
