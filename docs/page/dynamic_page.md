# Динамическая Page

Если вам требуется динамически обновлять вид страницы после пользовательского ввода (например, страница каталога с
пагинацией и базой данных), одним из простейших способов будет переход на ту же самую страницу с использованием
сессионного хранилища.

Вот пример сниппета, где пользователь может переключаться между страницами, выдаваемыми базой данных:

```python
async def update_page(self, user, value):
    page_index = await user.storage.get("page_index")
    page_index += value
    await user.storage.set("page_index", page_index)

    # Обновляем страницу, чтобы загрузить новые данные
    navigator.update_page(user, '/')


async def make_page_content(self, user):
    page_index = await user.storage.get("page_index")
    data = await handler.get_page(page_index)

    text = '\n'.join([f"{entry.id}) {entry.text}" for entry in data])

    buttons = []
    if page_index < self.max_page_index:
        buttons.append(
            ButtonData("Следующая", ButtonCallback(self.update_page, value=1))
        )
    if page_index > 0:
        buttons.append(
            ButtonData("Предыдущая", ButtonCallback(self.update_page, value=-1))
        )

    self.markup.add_row(buttons)
    await self.send(user, text, markup=True)
```