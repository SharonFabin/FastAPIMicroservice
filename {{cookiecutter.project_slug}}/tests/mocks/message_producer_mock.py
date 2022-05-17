from services.messaging import MessageProducer


class MessageProducerMock(MessageProducer):
    def __init__(self):
        pass

    def connect(self):
        pass

    def send(self, topic: str, value, key):
        pass

    def close(self):
        pass
