import abc
from schemas.service import ServiceScheme


class ServiceInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def configure(self, service_scheme: ServiceScheme):
        raise NotImplementedError
