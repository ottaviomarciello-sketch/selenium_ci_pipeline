class LoginPage:
    def __init__(self, page):
        self.page = page

        self.username = "#userName"
        self.password = "#password"
        self.login_btn = "#login"
        self.profile = "#userName-value"

    def go(self, base_url):
        self.page.goto(f"{base_url}/login")

    def login(self, user, pwd):
        self.page.fill(self.username, user)
        self.page.fill(self.password, pwd)
        self.page.click(self.login_btn)

    def assert_login_success(self):
        expect(self.page.locator(self.profile)).to_be_visible(timeout=5000)