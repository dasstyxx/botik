# Страница ввода

Если вам нужен Page с обработкой текста пользователя, а не нажатия кнопок, вы можете наследовать класс от InputPage.

Он предоставляет методы для валидации введённых данных, методы при валидном вводе и наоборот.

Пример Page с вводом номера телефона:

```python
from botik.page.input_page import InputPage
```

```python
class PhonePage(InputPage):
    async def success(self, user, text):
        await self.send(user, f"Номер {text} получен")
        await navigator.change_page(user, '/success')

    async def fail(self, user, text):
        await self.send(user, f"Некорректный номер")

    async def filter_input(self, user, text):
        return re.match(r"^(\+\d{1,3}[- ]?)?\d{10}$", text)

    async def make_page_content(self, user):
        # Здесь могут быть кнопки, если требуется
        await self.send(user, "Введите телефон")
```