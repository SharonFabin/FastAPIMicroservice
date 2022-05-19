import subprocess
import shutil
import os
yaml_path = '{{ cookiecutter.openapi_path }}'
shutil.copyfile(yaml_path, os.getcwd())
with open("/tmp/output.log", "a") as output:
    subprocess.call("docker run --rm -v ${PWD}:/local openapitools/openapi-generator-cli generate -i /local/petstore.yaml -g python-fastapi -o /local/out/python", shell=True, stdout=output, stderr=output)
    # subprocess.call("docker run --rm -v ${PWD}:/local openapitools/openapi-generator-cli generate -i /local/petstore.yaml -g python-fastapi -o /local/out/python", shell=True, stdout=output, stderr=output)

# f = open("demofile2.txt", "a")
# f.write("Now the file has more content!")
# f.close()
