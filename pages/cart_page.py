from .base_page import BasePage


class CartPage(BasePage):
    ITEM = ".cart_item"
    CHECKOUT_BTN = '[data-test="checkout"]'

    def item_names(self) -> list[str]:
        return self.page.locator(".inventory_item_name").all_inner_texts()

    def checkout(self):
        self.page.click(self.CHECKOUT_BTN)
        return self
