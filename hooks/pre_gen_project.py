import subprocess

with open("/tmp/output.log", "a") as output:
    subprocess.call("docker run --rm -v $PWD:/local openapitools/openapi-generator-cli generate -i /local/petstore.yaml -g python-fastapi -o /local/out/python", shell=True, stdout=output, stderr=output)
