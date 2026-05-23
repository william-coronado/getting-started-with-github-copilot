import copy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app


@pytest.fixture(scope="session")
def baseline_activities():
    return copy.deepcopy(activities)


@pytest.fixture(autouse=True)
def reset_activities(baseline_activities):
    # Keep endpoint tests isolated because activity data is stored in-memory.
    activities.clear()
    activities.update(copy.deepcopy(baseline_activities))
    yield
    activities.clear()
    activities.update(copy.deepcopy(baseline_activities))


@pytest.fixture
def client():
    with TestClient(app) as test_client:
        yield test_client
