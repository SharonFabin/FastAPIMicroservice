from email.generator import Generator
from typing import AsyncGenerator
import pytest
import pytest_asyncio
from unittest.mock import AsyncMock
from schemas.service import ServiceScheme
from services.service_example import ServiceExample, ServiceInterface


@pytest_asyncio.fixture()
async def service() -> ServiceInterface:
    service = ServiceExample()
    return service


@pytest.mark.asyncio
async def test_spectrum_configuration(service: ServiceInterface):
    # Set

    # Act

    # Assert
    pass
