from typing import Generator
from unittest.mock import MagicMock, AsyncMock

import pytest
from fastapi.testclient import TestClient

from main import app
from routers import deps


# async def override_reddit_dependency() -> MagicMock:
#     mock = MagicMock()  # 4
#     reddit_stub = {
#         "recipes": [
#             "baz",
#         ],
#         "easyrecipes": [
#             "bar",
#         ],
#         "TopSecretRecipes": [
#             "foo"
#         ],
#     }
#     mock.get_reddit_top.return_value = reddit_stub  # 5
#     return mock

# async def override_reddit_dependency() -> AsyncMock:
#     mock = AsyncMock()  # 4
#     reddit_stub = {
#         "recipes": [
#             "baz",
#         ],
#         "easyrecipes": [
#             "bar",
#         ],
#         "TopSecretRecipes": [
#             "foo"
#         ],
#     }
#     mock.get_reddit_top.return_value = reddit_stub  # 5
#     return mock


# @pytest.fixture()
# def client() -> Generator:
#     with TestClient(app) as client:
#         app.dependency_overrides[deps.get_spectrum_service] = override_reddit_dependency
#         yield client
#         app.dependency_overrides = {}
