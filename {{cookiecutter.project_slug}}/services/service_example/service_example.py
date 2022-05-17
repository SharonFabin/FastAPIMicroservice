import logging
from schemas.service import ServiceScheme
from .service_interface import ServiceInterface


class ServiceExample(ServiceInterface):
    def __init__(self) -> None:
        pass

    async def configure(self, service_scheme: ServiceScheme):
        pass
