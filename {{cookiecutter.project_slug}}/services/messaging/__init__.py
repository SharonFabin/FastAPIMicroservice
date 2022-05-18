from .message_producer import MessageProducer

{%- if cookiecutter.messaging_technology == 'Kafka' %}
from .kafka_message_producer import KafkaMessageProducer
{%- elif cookiecutter.messaging_technology == 'RabbitMQ' %}
from .rabbitmq_producer import RabbitMQProducer
{%+ endif +%}
