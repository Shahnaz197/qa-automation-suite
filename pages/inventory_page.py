from .base_page import BasePage


class InventoryPage(BasePage):
    ITEM = ".inventory_item"
    PRICE = ".inventory_item_price"
    SORT = '[data-test="product-sort-container"]'
    CART_LINK = ".shopping_cart_link"
    CART_BADGE = ".shopping_cart_badge"

    def item_count(self) -> int:
        self.page.wait_for_selector(self.ITEM)
        return self.page.locator(self.ITEM).count()

    def add_to_cart(self, slug: str):
        """slug example: 'sauce-labs-backpack'"""
        self.page.click(f'[data-test="add-to-cart-{slug}"]')
        return self

    def remove_from_cart(self, slug: str):
        self.page.click(f'[data-test="remove-{slug}"]')
        return self

    def cart_count(self) -> int:
        badge = self.page.locator(self.CART_BADGE)
        return int(badge.inner_text()) if badge.count() else 0

    def sort_by(self, value: str):
        """'az', 'za', 'lohi', 'hilo'"""
        self.page.select_option(self.SORT, value)
        return self

    def prices(self) -> list[float]:
        texts = self.page.locator(self.PRICE).all_inner_texts()
        return [float(t.replace("$", "")) for t in texts]

    def open_cart(self):
        self.page.click(self.CART_LINK)
        return self
