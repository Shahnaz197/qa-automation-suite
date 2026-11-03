import pytest
from playwright.sync_api import expect

from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage

pytestmark = pytest.mark.ui


@pytest.mark.smoke
def test_inventory_shows_six_products(logged_in_page):
    assert InventoryPage(logged_in_page).item_count() == 6


def test_add_and_remove_item_updates_badge(logged_in_page):
    inv = InventoryPage(logged_in_page)
    badge = logged_in_page.locator(inv.CART_BADGE)
    inv.add_to_cart("sauce-labs-backpack")
    expect(badge).to_have_text("1")
    inv.remove_from_cart("sauce-labs-backpack")
    expect(badge).to_have_count(0)


def test_cart_contains_selected_items(logged_in_page):
    inv = InventoryPage(logged_in_page)
    inv.add_to_cart("sauce-labs-backpack").add_to_cart("sauce-labs-bike-light")
    inv.open_cart()
    names = CartPage(logged_in_page).item_names()
    assert sorted(names) == ["Sauce Labs Backpack", "Sauce Labs Bike Light"]


def test_sort_price_low_to_high(logged_in_page):
    inv = InventoryPage(logged_in_page).sort_by("lohi")
    prices = inv.prices()
    assert prices == sorted(prices)
