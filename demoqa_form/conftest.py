import pytest

@pytest.fixture(scope="session")
def browser_type_launch_args():
    return {
        "headless": False,
        "slow_mo": 500
    }

@pytest.fixture(scope="session")
def browser_context_args():
    return {
        "viewport": {"width": 1280, "height": 720},
      }

@pytest.fixture
def user_data():
    return {
        "username": "testuser",
        "password": "Password123!"
    }