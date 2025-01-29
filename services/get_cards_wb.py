import asyncio

async def get_cards_wb(e, api_key, status_bar):
    print("Заглушка: Получение карточек с ВБ...")
    await asyncio.sleep(2)  # Эмуляция задержки
    status_bar.update_status('Карточки получены')