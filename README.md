# FastAPI Base Project Generator

Uses [OpenAPI Generator](https://openapi-generator.tech/ "OpenAPI Generator") to generate models and routes from an OpenAPI spec.

Uses [Cookiecutter](https://github.com/cookiecutter/cookiecutter "Cookiecutter") to generate project template.

Uses custom scripts to organize files from both generators

Inorder to use the OpenAPI generator, you must specify the path for the OpenAPI spec file during setup.
In addition, you must have the docker image **openapitools/openapi-generator-cli** downloaded locally.

Setup options:
- Project Name
- Database technology
- MessageQueue technology
- Add Websocket features
- Generate Service-Pattern template
- Use an OpenAPI spec file to auto generate routes and models
