class BasePage:
    def __init__(self, page):
        self.page = page

    def click(self, selector):
        self.page.click(selector)

    def click_by_role(self, role: str, name: str):
        self.page.get_by_role(role, name=name).click()

    def fill(self, selector, text):
        self.page.fill(selector, text)

    def get_text(self, selector):
        return self.page.text_content(selector)

    def is_visible(self, selector):
        return self.page.is_visible(selector)
