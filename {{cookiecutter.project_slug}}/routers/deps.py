from services.service_example import ServiceInterface, ServiceExample
from services.messaging import MessageProducer, KafkaMessageProducer

service_example = ServiceExample()
kafka_message_producer = KafkaMessageProducer()


def get_service_example() -> ServiceInterface:
    return service_example


def get_message_producer() -> MessageProducer:
    return kafka_message_producer
