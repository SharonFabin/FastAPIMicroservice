import logging
from fastapi.testclient import TestClient
from typing import Generator
from unittest.mock import AsyncMock
import pytest
from main import app
from routers import deps
from services.messaging import message_producer
from ..mocks import ServiceMock, MessageProducerMock
from schemas.service import ServiceScheme


service_mock = AsyncMock(ServiceMock)
message_producer_mock = AsyncMock(MessageProducerMock)


@pytest.fixture()
def client() -> Generator:
    with TestClient(app) as client:
        app.dependency_overrides[deps.get_service_example] = lambda: service_mock
        app.dependency_overrides[deps.get_message_producer] = lambda: message_producer_mock
        yield client
        app.dependency_overrides = {}


def test_service_configuration(client: TestClient):
    service_scheme = ServiceScheme(variable=0)
    response = client.post('/service/example/', json=service_scheme)
    assert response.status_code == 200
