# Page

Основная сущность для разработки интерфейса бота.
Все страницы записываются в стек переходов юзера, с возможностью перехода назад.
Для подробностей как в фреймворке обрабатываются сообщения юзера переходите на страницу:
[Порядок обработки пользовательского ввода](handling_order.md)

## Пример создания Page

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

## Специфичные кейсы

* [Динамическая страница](dynamic_page.md)
* [Страница ввода](input_page.md)