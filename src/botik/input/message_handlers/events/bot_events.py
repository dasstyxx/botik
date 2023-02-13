from botik.input.message_handlers.events.contact_share_event import ContactShareEvent
from botik.input.message_handlers.events.geo_share_event import GeoShareEvent


class BotEvents:
    def __init__(self):
        self.contact_share = ContactShareEvent()
        self.geo_share = GeoShareEvent()
