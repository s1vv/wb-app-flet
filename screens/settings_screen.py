import os
import flet as ft
from dotenv import load_dotenv, set_key
from ui_components.button import CustomButtonComponent

# Загрузка переменных из .env
load_dotenv()

# Функция для сохранения значений токенов
def save_tokens(token_from, token_to):
    set_key('.env', 'TOKEN_FROM', token_from)
    set_key('.env', 'TOKEN_T', token_to)
    
    # Обновляем значения переменных в текущем окружении
    os.environ['TOKEN_FROM'] = token_from
    os.environ['TOKEN_T'] = token_to
    print("Токены сохранены:", token_from, token_to)

# Функция для очистки значений токенов и обновления полей ввода
def clear_tokens(input_from_field, input_to_field):
    set_key('.env', 'TOKEN_FROM', '')
    set_key('.env', 'TOKEN_T', '')
    print("Токены очищены")

    # Очищаем переменные в текущем окружении
    os.environ.pop('TOKEN_FROM', None)
    os.environ.pop('TOKEN_T', None)

    # Обнуляем значения полей ввода
    input_from_field.value = ''
    input_to_field.value = ''
    input_from_field.update()
    input_to_field.update()

# Основной экран настроек
def SettingsScreen(page):
    # Поля ввода для токенов
    input_token_from = ft.TextField(
        label="Введите токен откуда копируем", 
        value=os.environ.get('TOKEN_FROM')
        )
    
    input_token_to = ft.TextField(
        label="Введите токен куда копируем", 
        value=os.environ.get('TOKEN_T')
        )
    
    # Кнопка сохранения токенов
    save_token_btn = CustomButtonComponent(
        label="Сохранить токены",
        on_click=lambda e: save_tokens(input_token_from.value, input_token_to.value),
    )

    # Кнопка очистки токенов
    clear_token_btn = CustomButtonComponent(
        label="Очистить токены",
        on_click=lambda e: clear_tokens(input_token_from, input_token_to),
    )

    return ft.Column(
        [
            ft.Text("Настройки"),
            input_token_from,
            input_token_to,

            ft.Row(
                [
                    save_token_btn,
                    clear_token_btn
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                expand=True
            )
        ],
        expand=True,
    )
