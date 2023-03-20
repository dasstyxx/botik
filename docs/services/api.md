# Api

Объект Api получается следующим образом:

```python
from botik.api import get_api

api = get_api()
```

Если вы запускаете код на двух мессенджерах, вы можете использовать аттрибут api.api_type,
чтобы проверить в рантайме, какая из реализаций запущена.
Это полезно, если вам необходимы специфичные конфигурации объектов, поддерживающиеся только на одном из мессенджеров.

```python
if api.api_type == TgApiType:
    bottom_button = ButtonData("Phone", None, ButtonFunction.request_phone)
elif api.api_type == VkApiType:
    # ВК не поддерживает кнопку для отправки телефона, направляем на Page
    bottom_button = ButtonData("Phone", ButtonCallback(navigator.change_page, path='/phone'))
```

## Когда нехватает функций botik

Вы можете получить прямой доступ к backbone-библиотеке бота, обратившись к аттрибуту api.bot
(так же доступен low-level api библиотеки vkbottle по аттрибуту api.raw_api)

Делать это на регулярной основе — плохая практика, вам предоставлен этот аттрибут для реализации
еще неимплементированного функционала внутри фреймворка.