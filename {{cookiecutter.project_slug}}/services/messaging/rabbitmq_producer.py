from contextlib import asynccontextmanager
import logging
from .message_producer import MessageProducer


class RabbitMQProducer(MessageProducer):
    def __init__(self) -> None:
        pass

    @asynccontextmanager
    async def connect(self, ip: str):
        yield

    async def send(self, topic: str, value, key):
        pass

    async def close(self):
        pass
