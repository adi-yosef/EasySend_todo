import src.config.config

class LoginPage:
    def __init__(self, page) -> None:
        self.page = page

        self.user_name = src.config.config.TestData.USER_NAME
        self.sidebar_button = page.get_by_role("button", name="Sidebar")
        