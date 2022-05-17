import logging
from aiokafka import AIOKafkaConsumer


class KafkaClient():
    def __init__(self):
        self.consumer: AIOKafkaConsumer
        # self.last_message: str | None
        self.running = False
        self.last_message = [0]

    async def connect(self, ip: str, topic: str):
        self.consumer = AIOKafkaConsumer(
            topic, bootstrap_servers=ip)
        await self.consumer.start()
        logging.debug('meow')

    async def consume_messages(self):
        try:
            async for message in self.consumer:
                self.last_message = list(bytearray(message.value))
        except Exception as e:
            logging.error(e)

    def stop_consuming(self):
        self.running = False

    async def close(self):
        await self.consumer.stop()
