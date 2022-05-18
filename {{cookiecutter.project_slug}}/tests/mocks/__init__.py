{%- if cookiecutter.messaging_technology != 'None' %}
from .message_producer_mock import MessageProducerMock
{%+ endif +%}
{%- if cookiecutter.messaging_technology == 'Kafka' %}
from .kafka_client import KafkaClient
{%- elif cookiecutter.messaging_technology == 'RabbitMQ' %}
from .rabbitmq_client import RabbitMQClient
{%+ endif +%}
{%- if cookiecutter.service_pattern_template == 'True' %}
from .service_mock import ServiceMock
{%+ endif +%}

