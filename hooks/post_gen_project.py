from pathlib import Path
import os
import shutil


# path: Path
# for path in Path(".").glob("**/*.sh"):
#     data = path.read_bytes()
#     lf_data = data.replace(b"\r\n", b"\n")
#     path.write_bytes(lf_data)

REMOVE_PATHS = [
    '{% if cookiecutter.messaging_technology != "Kafka" %} services/messaging/kafka_message_producer.py {% endif %}',
    '{% if cookiecutter.messaging_technology != "RabbitMQ" %} services/messaging/rabbitmq_message_producer.py {% endif %}',
    '{% if cookiecutter.using_websocket != true %} utils/__init__.py {% endif %}',
    '{% if cookiecutter.service_pattern_template != true %} services/service_example {% endif %}',
    '{% if cookiecutter.service_pattern_template != true %} schemes/service.py {% endif %}',
    '{% if cookiecutter.service_pattern_template != true %} routers/service.py {% endif %}',
]

for path in REMOVE_PATHS:
    path = path.strip()
    if path and os.path.exists(path):
        if os.path.isdir(path):
            shutil.rmtree(path)
        else:
            os.unlink(path)