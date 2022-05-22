import subprocess
import shutil
import os

# Copy spec file to project root
yaml_path = '{{ cookiecutter.openapi_path }}'
current_directory = os.getcwd()
shutil.copyfile(yaml_path, f'{current_directory}/openapi.yaml')

# Generate OpenAPI project with docker
with open("/tmp/output.log", "a") as output:
    subprocess.call("docker run --rm -v ${PWD}:/local openapitools/openapi-generator-cli generate -i /local/openapi.yaml -g python-fastapi -o /local/out", shell=True, stdout=output, stderr=output)