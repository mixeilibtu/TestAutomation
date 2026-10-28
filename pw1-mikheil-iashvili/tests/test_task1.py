# ### დავალება 1 · ლოკატორები

# - საიტი: https://www.saucedemo.com/
# - მონაცემები: standard_user / secret_sauce
# - ნაბიჯები: შედი სისტემაში. სამი ელემენტისთვის გამოიყენე **სამი სხვადასხვა ლოკატორი**:
#   - Username → `get_by_placeholder(...)`
#   - Password → CSS ლოკატორი (`#...`)
#   - Login ღილაკი → XPath ლოკატორი
# - შემოწმება:
#   - URL არის `https://www.saucedemo.com/inventory.html`
#   - სათაური `[data-test="title"]` არის `Products`


from playwright.sync_api import Page, expect

URL = "https://www.saucedemo.com/"


def test_task1_login(page: Page):
    # arrange
    page.goto(URL)

    # act
    page.get_by_placeholder("Username").fill("standard_user")

    page.locator("#password").fill("secret_sauce")

    page.locator("//input[@id='login-button']").click()

    # assert
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(page.locator('[data-test="title"]')).to_have_text("Products")