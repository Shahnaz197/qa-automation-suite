from .base_page import BasePage


class CheckoutPage(BasePage):
    FIRST = '[data-test="firstName"]'
    LAST = '[data-test="lastName"]'
    ZIP = '[data-test="postalCode"]'
    CONTINUE = '[data-test="continue"]'
    FINISH = '[data-test="finish"]'
    ERROR = '[data-test="error"]'
    COMPLETE = ".complete-header"

    def fill_info(self, first: str, last: str, postal: str):
        self.page.fill(self.FIRST, first)
        self.page.fill(self.LAST, last)
        self.page.fill(self.ZIP, postal)
        self.page.click(self.CONTINUE)
        return self

    def finish(self):
        self.page.click(self.FINISH)
        return self

    def confirmation_text(self) -> str:
        return self.page.inner_text(self.COMPLETE)

    def error_text(self) -> str:
        return self.page.inner_text(self.ERROR)
