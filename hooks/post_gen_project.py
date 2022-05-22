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
    # Copy conftest to project root
    current_directory = os.getcwd()
    shutil.move(f'{current_directory}/out/tests/conftest.py', f'{current_directory}/conftest.py')

    src_path = f'{current_directory}/out'
    trg_path = f'{current_directory}'
    tests_path = 'tests'
    models_path = 'src/openapi_server/models'
    routes_path = 'src/openapi_server/api'
    main_path = 'src/openapi_server/main.py'

    # Copy API tests to tests folder
    for src_file in Path(f'{src_path}/{tests_path}').glob('test_*.py'):
        shutil.move(src_file, os.path.join(f'{trg_path}/tests/api',os.path.basename(src_file)))

    # Copy models and schemas
    for src_file in Path(f'{src_path}/{models_path}').glob('*.py'):
        shutil.move(src_file, os.path.join(f'{trg_path}/models',os.path.basename(src_file)))
    
    # Copy routes
    for src_file in Path(f'{src_path}/{routes_path}').glob('*_api.py'):
        shutil.move(src_file, os.path.join(f'{trg_path}/routers',os.path.basename(src_file)))

    # Copy generated main
    shutil.move(Path(f'{src_path}/{main_path}'), Path(f'{trg_path}/openapi_main.py'))

    # Copy docker components
    shutil.move(Path(f'{src_path}/docker-compose.yaml'), Path(f'{trg_path}/docker-compose.yaml'))
    shutil.move(Path(f'{src_path}/Dockerfile'), Path(f'{trg_path}/Dockerfile'))

    #Delete unnecessary files
    # shutil.rmtree(Path(src_path))

