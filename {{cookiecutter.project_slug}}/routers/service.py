from fastapi import APIRouter, Depends, Response, status

from routers import deps
from services.service_example import ServiceInterface
from schemas.service import ServiceScheme


service_router = APIRouter(
    prefix="/spectrum",
    tags=["spectrum functions"],
    responses={404: {"description": "Not found"}},
)

# spectrum_service = SpectrumService()


@service_router.post("/example/")
async def config_spectrum(config: ServiceScheme):
    return {"info": "OK"}


@service_router.post("/exampleWithDependency/")
async def start_stream(response: Response,
                       config: ServiceScheme,
                       service: ServiceInterface = Depends(
                           deps.get_service_example),
                       message_broker: deps.MessageProducer = Depends(deps.get_message_producer)):
    await service.configure(config)
    response.status_code = status.HTTP_200_OK
    return {"info": "OK"}
