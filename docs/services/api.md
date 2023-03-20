# Api

Объект Api получается следующим образом:

```python
from botik.api import get_api

api = get_api()
```

Если вы запускаете код на двух мессенджерах, вы можете использовать аттрибут api.api_type,
чтобы проверить в рантайме какая из реализаций запущена.
Это полезно, если вам необходимы специфичные конфигурации объектов, поддерживающиеся только на одном из мессенджеров.

```python
if api.api_type == TgApiType:
    bottom_button = ButtonData("Phone", None, ButtonFunction.request_phone)
elif api.api_type == VkApiType:
    # ВК не поддерживает кнопку для отправки телефона, направляем на Page
    bottom_button = ButtonData("Phone", ButtonCallback(navigator.change_page, path='/phone'))
```