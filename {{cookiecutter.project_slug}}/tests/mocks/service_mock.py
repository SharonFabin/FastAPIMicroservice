from schemas.service import ServiceScheme
from services.service_example.service_interface import ServiceInterface
from services.messaging import MessageProducer


class ServiceMock(ServiceInterface):
    def __init__(self):
        pass

    async def configure(self, service_scheme: ServiceScheme):
        pass
