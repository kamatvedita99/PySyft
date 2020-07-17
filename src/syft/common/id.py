import uuid
from ..typecheck import type_hints
from typing import final


@final
class UID(object):
    """A unique id"""

    def __init__(self):
        # TODO find out what type is smaller for protobuf msgs.
        self.value = str(uuid.UUID(int=0x12345678123456781234567812345678))
