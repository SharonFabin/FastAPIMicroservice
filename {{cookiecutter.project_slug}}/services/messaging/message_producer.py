import abc


class MessageProducer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def connect(self):
        raise NotImplementedError

    @abc.abstractmethod
    def send(self, topic: str, value, key):
        raise NotImplementedError

    @abc.abstractmethod
    def close(self):
        raise NotImplementedError
