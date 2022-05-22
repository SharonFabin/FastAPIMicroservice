from pathlib import Path
import os
import shutil


for path in Path(".").glob("**/*.sh"):
    data = path.read_bytes()
    lf_data = data.replace(b"\r\n", b"\n")
    path.write_bytes(lf_data)

REMOVE_PATHS = [
    '{% if cookiecutter.messaging_technology != "Kafka" %} services/messaging/kafka_message_producer.py {% endif %}',
    '{% if cookiecutter.messaging_technology != "RabbitMQ" %} services/messaging/rabbitmq_message_producer.py {% endif %}',

    '{% if cookiecutter.using_websocket != "True" %} utils/kafka_to_websocket.py {% endif %}',

    '{% if cookiecutter.service_pattern_template != "True" %} services/service_example {% endif %}',
    '{% if cookiecutter.service_pattern_template != "True" %} schemes/service.py {% endif %}',
    '{% if cookiecutter.service_pattern_template != "True" %} routers/service.py {% endif %}',
    '{% if cookiecutter.service_pattern_template != "True" %} tests/service {% endif %}',
    '{% if cookiecutter.service_pattern_template != "True" %} tests/mocks/service_mock.py {% endif %}',

    '{% if cookiecutter.messaging_technology != "Kafka" %} services/messaging/kafka_message_producer.py {% endif %}',
    '{% if cookiecutter.messaging_technology != "Kafka" %} tests/messaging/test_kafka_messaging.py {% endif %}',
    '{% if cookiecutter.messaging_technology != "Kafka" %} tests/mocks/kafka_client.py {% endif %}',
    '{% if cookiecutter.messaging_technology != "RabbitMQ" %} services/messaging/rabbitmq_producer.py {% endif %}',
    '{% if cookiecutter.messaging_technology != "RabbitMQ" %} tests/messaging/test_rabbitmq_messaging.py {% endif %}',
    '{% if cookiecutter.messaging_technology != "RabbitMQ" %} tests/mocks/rabbitmq_client.py {% endif %}',
    '{% if cookiecutter.messaging_technology == "None" %} services/messaging {% endif %}',
    '{% if cookiecutter.messaging_technology == "None" %} tests/messaging {% endif %}',
    '{% if cookiecutter.messaging_technology == "None" %} tests/mocks/message_producer_mock.py {% endif %}',

    # TODO: handle app tests 
    'tests/app'
]

for path in REMOVE_PATHS:
    path = path.strip()
    if path and os.path.exists(path):
        if os.path.isdir(path):
            shutil.rmtree(path)
        else:
            os.unlink(path)

if({{cookiecutter.openapi_path!=""}}):
    current_directory = os.getcwd()
    shutil.move(f'{current_directory}/out/tests/conftest.py', f'{current_directory}/conftest.py')

    src_path = f'{current_directory}/out/tests'
    trg_path = f'{current_directory}/tests/api/'
#
    for src_file in Path(src_path).glob('test_*.py'):
        shutil.copy(os.path.join(src_path,src_file), trg_path)
