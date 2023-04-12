# Botik

Botik позволяет вам писать код для ботов, одновременно исполняемый на разных мессенджерах.
Так же вам предлагается перейти от типичного написания функций-хендлеров на новую абстракцию страниц.

[Техническая документация](https://botik.readthedocs.io)

## Установка

```python
# Telegram
pip install botik-telebot
# VK
pip install botik-vkbottle
```

## Пример кода страницы

Ваше приложение на Botik будет представлять собой набор страниц.
Страница — это объект для обработки пользовательского ввода и вывода.

```python
class ExamplePage(Page):
    async def make_page_content(self, user):
        text = "Пример страницы"
        
        # ButtonCallback ожидает асинхронный метод с первым аргументом user,
        # и всеми последующими с явным указанием их имен
        self.markup.add_row([
            ButtonData("Нажми меня!", ButtonCallback(self.send, message="Привет, мир!"))
        ])
        self.markup.add_row([
            ButtonData("Back", ButtonCallback(navigator.get_back)),
            ButtonData("Home", ButtonCallback(navigator.change_page, path=f"~/"))
        ])
        
        await self.send(user, text, markup=True)
```

## Запуск бота

### Создаем два модуля-входных точек для нашего приложения.

Сперва инициализируем Backbone фреймворк для работы с мессенджером и прокидываем его в конструктор ядра приложения.

```python
# Telegram
from telebot.async_telebot import AsyncTeleBot
from botik_telebot.app import TgApp

token = "токен бота"
bot = AsyncTeleBot(token)

app = TgApp(bot)
```

```python
# VK
from vkbottle import API
from vkbottle.bot import Bot
from botik_vkbottle.app import VkApp

token = "токен бота"

# Текущая реализация фреймворка требует ссылки на High и Low Level API
bot = Bot(token=token)
low_api = API(token)

app = VkApp(bot, low_api)
```

### Создаем экземпляры, описывающие наши будущие страницы

```python
# Первым аргументом тип страницы, вторым относительный адрес, третьим адрес или объект родительской страницы
main_data = PageData(MainPage, '/', '', inline=True, one_time=True)
page1 = PageData(FirstPage, '/page1', main_data, inline=False, one_time=False)
# ...

# Собираем их в список
pages = [main_data, page1]
```

### Устанавливаем странички и запускаем приложение!

```python
app.set_pages(pages)

app.start()
```

###### Основан на [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI) и [VKBottle](https://github.com/vkbottle/vkbottle)