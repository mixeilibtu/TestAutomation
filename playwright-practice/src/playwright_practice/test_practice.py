from playwright.sync_api import Page, expect

BASE = "https://the-internet.herokuapp.com"

# class PracticeTests:

#     def __init__(self):
#         self.suceededTests = 0


#     def test_nothing_tc0(self, page:Page):
#         page.goto(BASE + "/login")
#         expect(page.get_by_role("heading", name="Login Page")).to_be_visible()
        


def test_nothing_tc0(page:Page):
    page.goto(BASE + "/login")
    expect(page.get_by_role("heading", name="Login Page")).to_be_visible()


def test_something_tc1(page:Page):
    page.goto(BASE + '/login')

    # page.get_by_label("Username").fill("tomsmith")
    page.locator("#username").fill("tomsmith")
    page.get_by_label("Password").fill("SuperSecretPassword!")
    page.get_by_role("button", name="Login").click()

    expect(page).to_have_url(BASE + "/secure")
    expect(page.locator("#flash")).to_contain_text("You logged into a secure area!")
        