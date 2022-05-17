from contextlib import asynccontextmanager
import logging
import asyncio
from aiokafka import AIOKafkaConsumer
import websockets


class KafkaClient():
    def __init__(self):
        self.consumer: AIOKafkaConsumer
        # self.last_message: str | None
        self.running = False
        self.last_message = [0]
        self.websocket = None

    async def start(self):
        async with websockets.serve(self.handler, "localhost", 8000):  # type: ignore
            await asyncio.Future()

    @asynccontextmanager
    async def connect(self, ip: str, topic: str):
        self.consumer = AIOKafkaConsumer(
            topic, bootstrap_servers=ip)
        await self.consumer.start()
        logging.debug('meow')
        yield
        # yield self.consumer
        await self.close()

    async def consume_messages(self, websocket):
        try:
            print('started consume')
            while True:
                async for message in self.consumer:
                    self.last_message = list(bytearray(message.value))
                    # self.websocket.send(self.last_message)  # type: ignore
                    print(self.last_message)
                    if(websocket):
                        print('sending from websocket')
                        await websocket.send(message.value)
        except Exception as e:
            logging.error(e)

    async def handler(self, websocket, path):
        # self.websocket = websocket
        # while True:
        #     await asyncio.sleep(1)
        #     await self.websocket.send('meow')
        # print('started')
        await self.consume_messages(websocket)
        pass

    def stop_consuming(self):
        self.running = False

    async def close(self):
        await self.consumer.stop()


async def main():
    HOST_IP = 'localhost:9092'
    TOPIC = 'quickstart'
    kafka_client = KafkaClient()
    async with kafka_client.connect(HOST_IP, TOPIC):
        await kafka_client.start()
        # await kafka_client.consume_messages()


asyncio.run(main())
