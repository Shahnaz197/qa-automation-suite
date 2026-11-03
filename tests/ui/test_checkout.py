import pytest

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage

pytestmark = pytest.mark.ui


def _go_to_checkout(page):
    InventoryPage(page).add_to_cart("sauce-labs-backpack").open_cart()
    CartPage(page).checkout()
    return CheckoutPage(page)


@pytest.mark.smoke
def test_full_checkout_flow(logged_in_page):
    checkout = _go_to_checkout(logged_in_page)
    checkout.fill_info("Shahnaz", "Tester", "10100").finish()
    assert "Thank you for your order" in checkout.confirmation_text()


def test_checkout_requires_first_name(logged_in_page):
    checkout = _go_to_checkout(logged_in_page)
    checkout.fill_info("", "Tester", "10100")
    assert "First Name is required" in checkout.error_text()
