import logging
import asyncio
from services.messaging import KafkaMessageProducer, kafka_message_producer
from email.generator import Generator
from typing import AsyncGenerator
import pytest
import pytest_asyncio
from unittest.mock import AsyncMock
from services.messaging.message_producer import MessageProducer
from ..mocks.kafka_client import KafkaClient

HOST_IP = 'localhost:9092'
TOPIC = 'quickstart'


@pytest_asyncio.fixture()
async def kafka_message_producer() -> AsyncGenerator:
    kafka_message_producer = KafkaMessageProducer()
    async with kafka_message_producer.connect(HOST_IP):
        yield kafka_message_producer


@pytest_asyncio.fixture()
async def kafka_client() -> AsyncGenerator:
    kafka_client = KafkaClient()
    await kafka_client.connect(HOST_IP, TOPIC)
    yield kafka_client
    await kafka_client.close()


@pytest.mark.asyncio
async def test_producer_sends_messages(kafka_message_producer: MessageProducer, kafka_client: KafkaClient):
    expected_message = [1, 2, 3]
    await kafka_message_producer.send(TOPIC, expected_message, '')
    consumer_timeout_task = asyncio.create_task(
        consumer_timeout(kafka_client, 1))
    consumer_task = asyncio.create_task(kafka_client.consume_messages())
    await asyncio.gather(consumer_task, consumer_timeout_task)
    assert expected_message == kafka_client.last_message


async def consumer_timeout(consumer: KafkaClient, timeout):
    await asyncio.sleep(timeout)
    await consumer.close()


@pytest.mark.asyncio
async def test_large_messageing_sequence(kafka_message_producer: MessageProducer, kafka_client: KafkaClient):
    expected_message = [1 for i in range(100000)]

    consumer_timeout_task = asyncio.create_task(
        consumer_timeout(kafka_client, 2))
    producer_timeout_task = asyncio.create_task(
        producer_timeout(kafka_message_producer, 2))
    consumer_task = asyncio.create_task(kafka_client.consume_messages())
    producer_task = asyncio.create_task(
        produce_messages(kafka_message_producer, expected_message, 100))

    await asyncio.gather(producer_task, consumer_task, consumer_timeout_task, producer_timeout_task)


async def producer_timeout(producer: MessageProducer, timeout):
    await asyncio.sleep(timeout)
    await producer.close()


async def produce_messages(producer, message, count):
    for i in range(count):
        await producer.send(TOPIC, message, '')
