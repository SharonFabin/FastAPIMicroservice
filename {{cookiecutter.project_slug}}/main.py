import logging
from fastapi import APIRouter, FastAPI
{% if cookiecutter.service_pattern_template == 'True'}
from routers import service_router
{% endif %}
import routers.deps
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

logging.basicConfig(filename='app.log', filemode='w',
                    format='%(asctime)s %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)
logging.info(f'App started\n')

app = FastAPI()

# @app.on_event("startup")
# async def startup_event():
#     global producer
#     producer = AIOProducer(
#         {"bootstrap.servers": "localhost:9092"})

# @app.on_event("shutdown")
# def shutdown_event():
#     producer.close()


@app.get("/")
async def root():
    return {"info": "OK"}

api_routers = [{% if cookiecutter.service_pattern_template == 'True' %}service_router{% endif %}]

for router in api_routers:
    app.include_router(router)


# @app.exception_handler(StarletteHTTPException)
# async def custom_http_exception_handler(request, e):
#     return await http_exception_handler(request, e)


# @app.exception_handler(RequestValidationError)
# async def custom_validation_exception_handler(request, e):
#     return await request_validation_exception_handler(request, e)


# @app.exception_handler(AppExceptionCase)
# async def custom_app_exception_handler(request, e):
#     return await app_exception_handler(request, e)
