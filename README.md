### Описание функционала программы

Программа представляет собой приложение для работы с карточками товаров и изображениями, предназначенное для интеграции с торговой платформой Wildberries (ВБ). Внутри приложения реализованы различные функции, такие как получение карточек, добавление цен, конвертация данных и отправка изображений, все это с использованием данных из файлов Excel и JSON.

Приложение разработано с использованием **Flet** (фреймворк для создания GUI приложений на Python) и предоставляет графический интерфейс для пользователя. Программа также взаимодействует с API Wildberries и использует другие внешние сервисы для обработки данных. Примерный функционал включает:

### Основные функции программы:

1. **Загрузка и обработка данных**:
   - **Загрузка карточек товаров** с Wildberries: Программа позволяет получить список карточек товаров с платформы ВБ в виде JSON, который затем может быть использован для дальнейших операций.
   - **Конвертация Excel в JSON**: Программа поддерживает конвертацию данных из Excel (файл с карточками товаров) в формат JSON, что может быть полезно для отправки данных на платформу Wildberries.
   - **Сохранение данных в Excel**: Программа может извлечь карточки товаров из платформы и сохранить их в формате Excel.

2. **Обработка изображений**:
   - **Подготовка изображений из Excel**: Из изображений, связанных с карточками товаров (например, ссылок на изображения в Excel), может быть подготовлен пакет для отправки на платформу Wildberries.
   - **Отправка изображений**: Программа позволяет отправить изображения товаров на ВБ через API.

3. **Управление ценами**:
   - **Обновление цен в карточках**: Программа может обновить цены товаров в файле Excel с учетом актуальных данных.

4. **Интерфейс**:
   - **Панель с кнопками** для выполнения различных операций (например, сохранение карточек, обновление цен, отправка изображений и т.д.).
   - **Панель прогресса** для отображения текущего состояния выполнения операций (например, сколько времени займет отправка данных или их обработка).
   - **Статус-бар**, который показывает текущее состояние операции или сообщения об ошибках.

5. **Безопасность и проверка лицензии**:
   - **Лицензионный ключ**: Программа требует наличия действующего лицензионного ключа для запуска. Ключ проверяется с сервером, и если он невалиден, пользователь не сможет использовать приложение.

6. **Файловый менеджер**:
   - **Выбор файлов**: Программа позволяет выбирать файлы Excel и JSON, которые будут использоваться для операций с карточками товаров и изображениями.
   
### Как работает программа:

1. **Запуск**: При запуске приложение сначала проверяет лицензионный ключ пользователя. Если ключ невалиден, пользователю предлагается ввести новый ключ для проверки.

2. **Работа с карточками товаров**:
   - Пользователь выбирает файлы Excel и JSON для дальнейших операций.
   - Программа позволяет выполнить несколько операций с карточками, таких как:
     - Загрузка карточек товаров из Wildberries.
     - Сохранение карточек в Excel.
     - Преобразование данных из Excel в JSON.
     - Отправка карточек товаров в формате JSON на Wildberries.
   
3. **Работа с изображениями**:
   - Пользователь может выбрать Excel файл с изображениями, и программа подготавливает их для отправки на Wildberries.
   - После подготовки изображений пользователь может отправить их через API.

4. **Управление ценами**:
   - Программа также позволяет обновить цены в карточках товаров в файле Excel.

5. **Прогресс и статус**:
   - В процессе выполнения операций на экране показывается прогресс выполнения задачи (например, индикатор выполнения отправки данных или обработки карточек).
   - Статус-бар отображает текущие сообщения и ошибки, если они возникли.

6. **Гибкость и расширяемость**:
   - Программа использует компоненты, которые легко можно настроить или расширить, например, добавив новые функции для обработки других типов данных или интеграций с другими платформами.

### Взаимодействие с сервером Wildberries:

- Программа взаимодействует с API Wildberries для выполнения различных операций, таких как отправка карточек товаров, получение карточек и отправка изображений.
- Для отправки данных на сервер используется токен, который должен быть предоставлен пользователем. Этот токен должен быть валидирован через сервер перед его использованием.

---

### В общем, программа предоставляет удобный интерфейс для работы с товарами на платформе Wildberries, облегчая процесс обработки данных, работы с файлами и отправки информации на платформу через API.