import pytest
import requests

UI_BASE_URL = "https://www.saucedemo.com"
API_BASE_URL = "https://jsonplaceholder.typicode.com"


@pytest.fixture(scope="session")
def base_url():
    return UI_BASE_URL


@pytest.fixture(scope="session")
def api():
    """Shared HTTP session with a base URL helper for API tests."""
    session = requests.Session()
    session.headers.update({"Content-Type": "application/json"})
    session.base_url = API_BASE_URL
    yield session
    session.close()


@pytest.fixture
def logged_in_page(page, base_url):
    """Browser page already logged in as the standard user."""
    from pages.login_page import LoginPage

    LoginPage(page, base_url).open().login("standard_user", "secret_sauce")
    return page
