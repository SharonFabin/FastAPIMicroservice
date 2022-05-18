from services.service_example import ServiceInterface, ServiceExample
from services.messaging import MessageProducer

service_example = ServiceExample()

{%- if cookiecutter.messaging_technology == "Kafka" -%}
from services.messaging import KafkaMessageProducer
message_producer = KafkaMessageProducer()
{%- elif cookiecutter.messagin_technology == "RabbitMQ" -%}
from services.messaging import RabbitMQProducer
message_producer = RabbitMQProducer()
{% endif %}


{%- if cookiecutter.messaging_technology != "None" -%}
def get_message_producer() -> MessageProducer:
    return message_producer
{% endif %}


{%- if cookiecutter.using_websocket == true -%}
def get_service_example() -> ServiceInterface:
    return service_example
{% endif %}


