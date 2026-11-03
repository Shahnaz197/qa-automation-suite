import pytest
from playwright.sync_api import expect

from pages.login_page import LoginPage

pytestmark = pytest.mark.ui


@pytest.mark.smoke
def test_valid_login_lands_on_inventory(page, base_url):
    LoginPage(page, base_url).open().login("standard_user", "secret_sauce")
    expect(page).to_have_url(f"{base_url}/inventory.html")


def test_locked_out_user_sees_error(page, base_url):
    login = LoginPage(page, base_url).open().login("locked_out_user", "secret_sauce")
    assert "locked out" in login.error_text().lower()


@pytest.mark.parametrize(
    "user, pwd, expected",
    [
        ("standard_user", "wrong_pass", "do not match"),
        ("", "secret_sauce", "Username is required"),
        ("standard_user", "", "Password is required"),
    ],
)
def test_invalid_credentials_show_error(page, base_url, user, pwd, expected):
    login = LoginPage(page, base_url).open().login(user, pwd)
    assert expected in login.error_text()
