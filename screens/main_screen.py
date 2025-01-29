import asyncio
import os
import flet as ft
from dotenv import load_dotenv
from services.send_cards_to_wb import send_json_to_wb_api
from services.get_cards_wb import get_cards_wb
from services.json_to_xlsx_decorator import save_to_xlsx
from services.send_imgs_to_wb import prepare_image_data_from_excel, send_images_to_wb
from services.set_price import update_prices_in_excel
from services.xlsx_to_json import xlsx_to_json
from ui_components.button import CustomButtonComponent
from ui_components.file_picker import FilePickerComponent
from ui_components.progress_bar import ProgressComponent
from ui_components.status_bar import MultiLineStatusBar

def HomeScreen(page):
    load_dotenv('.env')
    input_prefix = ft.TextField(label="Введите префикс")
    status_bar = MultiLineStatusBar()
    progress_component = ProgressComponent()

    file_picker_xlsx = FilePickerComponent(status_bar=status_bar, page=page, btn_txt='Выберите Excel файл')
    file_picker_json = FilePickerComponent(status_bar=status_bar, page=page, btn_txt='Выберите JSON файл')

    save_cards = save_to_xlsx(output_filename="wb_cards.xlsx", status_bar=status_bar)(get_cards_wb)
    async def on_click_save_cards(e):
        await save_cards(e, api_key=os.getenv('TOKEN_FROM'), status_bar=status_bar)

    async def on_click_save_json_cards(e):
        await xlsx_to_json(e, file_picker_xlsx.selected_file_path, input_prefix.value, status_bar)

    async def on_click_set_price(e):
        await update_prices_in_excel(e, file_picker_xlsx.selected_file_path, os.getenv('TOKEN_FROM'), status_bar)

    async def on_click_send_cards(e):
        await send_json_to_wb_api(e, file_picker_json.selected_file_path, os.getenv('TOKEN_T'), status_bar)

    async def on_click_send_imgs(e):
        data_imgs = await prepare_image_data_from_excel(e, file_picker_xlsx.selected_file_path, os.getenv('TOKEN_T'), status_bar)
        await send_images_to_wb(e, os.getenv('TOKEN_T'), data_imgs, status_bar)


    cards_to_xlsx_btn = CustomButtonComponent(
        label="Карточки в .xlsx из ЛК",
        on_click=lambda e: asyncio.create_task(progress_component.perform_task_with_progress(lambda: on_click_save_cards(e))),
    )

    cards_from_xlsx_to_json_btn = CustomButtonComponent(
        label="Сохранить карточки для ВБ",
        on_click=lambda e: asyncio.create_task(progress_component.perform_task_with_progress(lambda: on_click_save_json_cards(e))),
    )

    add_price_to_xlsx_btn = CustomButtonComponent(
        label="Добавить цены в карточки",
        on_click=lambda e: asyncio.create_task(progress_component.perform_task_with_progress(lambda: on_click_set_price(e))),
    )

    send_cards_to_wb_btn = CustomButtonComponent(
        label="Отправить карточки на ВБ",
        on_click=lambda e: asyncio.create_task(progress_component.perform_task_with_progress(lambda: on_click_send_cards(e))),
    )

    send_imgs_to_wb_btn = CustomButtonComponent(
        label="Отправить картинки на ВБ",
        on_click=lambda e: asyncio.create_task(progress_component.perform_task_with_progress(lambda: on_click_send_imgs(e))),
    )

    # Основной контент в центральной части экрана
    main_content = ft.Row(
        [
            ft.Column(
                [
                    cards_to_xlsx_btn,
                    cards_from_xlsx_to_json_btn,
                    input_prefix,  # Поле префикса
                ],
                expand=True,
            ),

            ft.Column(
                [
                    file_picker_xlsx,
                    file_picker_json,
                ],
                expand=True,
            ),

            ft.Column(
                [
                    add_price_to_xlsx_btn,
                    send_cards_to_wb_btn,
                    send_imgs_to_wb_btn, 
                ],
                expand=True,
            ),
        ],
        expand=True,
    )

    # Нижняя панель с прогресс-баром и статус-баром
    bottom_bar = ft.Column(
        [
            status_bar,
            progress_component,
        ],
        alignment=ft.MainAxisAlignment.END,  # Выравнивание по нижней границе
        expand=True,
    )

    # Общая компоновка страницы
    return ft.Column(
        [
            main_content,  # Основной контент
            bottom_bar,    # Нижняя панель
        ],
        expand=True,
    )
