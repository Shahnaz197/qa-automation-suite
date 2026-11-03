from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page, base_url: str = "https://www.saucedemo.com"):
        self.page = page
        self.base_url = base_url

    def goto(self, path: str = "/"):
        self.page.goto(f"{self.base_url}{path}")
        return self
