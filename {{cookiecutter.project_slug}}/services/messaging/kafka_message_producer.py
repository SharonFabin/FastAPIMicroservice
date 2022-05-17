from contextlib import asynccontextmanager
import logging
from .message_producer import MessageProducer
from aiokafka import AIOKafkaProducer


class KafkaMessageProducer(MessageProducer):
    def __init__(self) -> None:
        self.producer: AIOKafkaProducer

    @asynccontextmanager
    async def connect(self, ip: str):
        self.producer = AIOKafkaProducer(bootstrap_servers=ip)
        await self.producer.start()
        yield
        await self.close()
        logging.info(f'Kafka producer connected to {ip}')

    async def send(self, topic: str, value, key):
        try:
            key_bytes = bytes(key, encoding='utf-8')
            # value_bytes = bytes(value, encoding='utf-8')
            value_bytes = bytes(value)
            await self.producer.send(topic, key=key_bytes, value=value_bytes)
        except Exception as e:
            logging.error(e)

    async def close(self):
        await self.producer.stop()
        logging.info(f'Kafka producer closed')
