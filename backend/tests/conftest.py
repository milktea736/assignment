import pytest
from fastapi.testclient import TestClient

from backend.db.client import DBClient
from backend.main import app


@pytest.fixture(scope='session')
def doc_title() -> str:
    return 'Galactica Model Abstract'


@pytest.fixture(scope='session')
def doc_content() -> str:
    return (
        'Information overload is a major obstacle to scientific progress. The explosive '
        'growth in scientific literature and data has made it ever harder to discover useful insights '
        'in a large mass of information. Today scientific knowledge is accessed through search '
        'engines, but they are unable to organize scientific knowledge alone. In this paper we '
        'introduce Galactica: a large language model that can store, combine and reason about '
        'scientific knowledge.'
    )


@pytest.fixture(scope='session')
def db_client() -> DBClient:
    return DBClient()


@pytest.fixture(scope='session')
def test_client() -> TestClient:
    return TestClient(app)
