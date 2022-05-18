{%+ if cookiecutter.service_pattern_template == True +%}
from services.service_example import ServiceInterface, ServiceExample
{%+ endif +%}
{%+ if cookiecutter.messaging_technology == 'Kafka' +%}
from services.messaging import MessageProducer, KafkaMessageProducer
{%+ endif +%}
{%+ if cookiecutter.messaging_technology == 'RabbitMQ' +%}
from services.messaging import MessageProducer, RabbitMQProducer
{%+ endif +%}


{%+ if cookiecutter.service_pattern_template == True +%}
service_example = ServiceExample()
def get_service_example() -> ServiceInterface:
    return service_example
{%+ endif +%}


{%+ if cookiecutter.messaging_technology == "Kafka" +%}
from services.messaging import KafkaMessageProducer
message_producer = KafkaMessageProducer()
{%+ elif cookiecutter.messagin_technology == "RabbitMQ" +%}
from services.messaging import RabbitMQProducer
message_producer = RabbitMQProducer()
{%+ endif +%}
{%+ if cookiecutter.messaging_technology != "None" +%}
def get_message_producer() -> MessageProducer:
    return message_producer
{%+ endif +%}




