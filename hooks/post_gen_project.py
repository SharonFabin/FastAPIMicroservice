from pathlib import Path
import os, fnmatch
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

def handle_tests(src_path, trg_path):
    tests_path = 'tests'
    for src_file in Path(f'{src_path}/{tests_path}').glob('test_*.py'):
        with open(src_file, 'r+') as file:
            file.write(file.read().replace("openapi_server.",""))
        shutil.move(src_file, os.path.join(f'{trg_path}/tests/api',os.path.basename(src_file)))

def handle_models(src_path, trg_path):
    models_path = 'src/openapi_server/models'
    for src_file in Path(f'{src_path}/{models_path}').glob('*.py'):
        shutil.move(src_file, os.path.join(f'{trg_path}/models',os.path.basename(src_file)))

def handle_routes(src_path, trg_path):
    routes_path = 'src/openapi_server/apis'
    for src_file in Path(f'{src_path}/{routes_path}').glob('*_api.py'):
        shutil.move(src_file, os.path.join(f'{trg_path}/routers',os.path.basename(src_file)))

def handle_docker(src_path, trg_path):
    shutil.move(Path(f'{src_path}/docker-compose.yaml'), Path(f'{trg_path}/docker-compose.yaml'))
    shutil.move(Path(f'{src_path}/Dockerfile'), Path(f'{trg_path}/Dockerfile'))

def handle_misc(src_path, trg_path):
    main_path = 'src/openapi_server/main.py'
    auth_path = 'src/openapi_server/security_api.py'
    shutil.move(Path(f'{src_path}/{main_path}'), Path(f'{trg_path}/openapi_main.py'))
    shutil.move(Path(f'{src_path}/{auth_path}'), Path(f'{trg_path}/auth.py'))

def findReplace(directory, find, replace, filePattern):
    for path, dirs, files in os.walk(os.path.abspath(directory)):
        for filename in fnmatch.filter(files, filePattern):
            filepath = os.path.join(path, filename)
            with open(filepath) as f:
                s = f.read()
            s = s.replace(find, replace)
            with open(filepath, "w") as f:
                f.write(s)

def clean_files(src_path, trg_path):
    shutil.rmtree(Path(src_path))


if({{cookiecutter.openapi_path!=""}}):
    # Copy conftest to project root
    current_directory = os.getcwd()
    shutil.move(f'{current_directory}/out/tests/conftest.py', f'{current_directory}/conftest.py')

    src_path = f'{current_directory}/out'
    trg_path = f'{current_directory}'

    # TODO: correct path names for imports (openapi_server to correct path name)

    findReplace(src_path, 'openapi_server.', '', '*.*')
    findReplace(src_path, 'security_api import', 'auth import', '*.py')

    handle_tests(src_path, trg_path)
    handle_models(src_path, trg_path)
    handle_routes(src_path, trg_path)
    handle_docker(src_path, trg_path)
    handle_misc(src_path, trg_path)
    # clean_files(src_path, trg_path)


