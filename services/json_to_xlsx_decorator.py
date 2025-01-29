import asyncio

def save_to_xlsx(output_filename, status_bar):
    def wrapper(func):
        async def wrapped(e, *args, **kwargs):
            print(f"Заглушка: Сохранение данных в файл {output_filename}...")
            await asyncio.sleep(2)  # Эмуляция задержки
            status_bar.update_status(f"Данные сохранены в {output_filename}")
        return wrapped
    return wrapper
