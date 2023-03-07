from botik.input.message_handlers.events.contact_share_event import ContactShareEvent
from botik.input.message_handlers.events.geo_share_event import GeoShareEvent
from botik.input.message_handlers.events.got_attachment_event import GotAttachmentEvent


# TODO: Replace by service locator
class BotEvents:
    def __init__(self):
        self.contact_share = ContactShareEvent()
        self.geo_share = GeoShareEvent()
        self.got_attachment = GotAttachmentEvent()
