import asyncio

async def prepare_image_data_from_excel(e, selected_file_path, token, status_bar):
    print(f"Заглушка: Подготовка изображений из файла {selected_file_path}...")
    await asyncio.sleep(2)  # Эмуляция задержки
    status_bar.update_status('Изображения подготовлены')

async def send_images_to_wb(e, token, data_imgs, status_bar):
    print(f"Заглушка: Отправка изображений на ВБ с токеном {token}...")
    await asyncio.sleep(2)  # Эмуляция задержки
    status_bar.update_status('Изображения отправлены на ВБ')