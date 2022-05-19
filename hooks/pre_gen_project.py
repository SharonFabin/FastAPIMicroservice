import subprocess
import shutil
import os
yaml_path = '{{ cookiecutter.openapi_path }}'
current_directory = os.getcwd()
shutil.copyfile(yaml_path, f'{current_directory}/openapi.yaml')
with open("/tmp/output.log", "a") as output:
    subprocess.call("docker run --rm -v ${PWD}:/local openapitools/openapi-generator-cli generate -i /local/openapi.yaml -g python-fastapi -o /local/out", shell=True, stdout=output, stderr=output)
shutil.rmtree(f'{current_directory}/conftest.py')
# shutil.move(f'{current_directory}/tests/conftest.py', f'{current_directory}/conftest.py')