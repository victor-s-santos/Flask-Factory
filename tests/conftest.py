import pytest
from blog.app import create_app

@pytest.fixture(scope='module')
def app():
    """Init the application"""
    return create_app()
