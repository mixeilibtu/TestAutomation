#  დავალება 1 · Checkbox, Radio და Dropdown

# - საიტი: [https://www.selenium.dev/selenium/web/web-form.html](https://www.selenium.dev/selenium/web/web-form.html)
# - ნაბიჯები და შემოწმება:
#   - თავიდან `#my-check-1` მონიშნულია, `#my-check-2` — არა
#   - მოხსენი `#my-check-1` და მონიშნე `#my-check-2` → შეამოწმე ორივე
#   - აირჩიე radio `#my-radio-2` → `to_be_checked()`, ხოლო `#my-radio-1` → `not_to_be_checked()`
#   - dropdown `select[name="my-select"]`-ში აირჩიე `Two` → `to_have_value("2")`
# - მინიშნება: `check()`, `uncheck()`, `select_option("Two")`

from playwright.sync_api import Page, expect

URL = "https://www.selenium.dev/selenium/web/web-form.html"


def test_task_1_checkbox_radio_dropdown(page: Page):
    page.goto(URL)

    check_1 = page.locator("#my-check-1")
    check_2 = page.locator("#my-check-2")
    expect(check_1).to_be_checked()
    expect(check_2).not_to_be_checked()

    check_1.uncheck()
    check_2.check()
    expect(check_1).not_to_be_checked()
    expect(check_2).to_be_checked()

    radio_1 = page.locator("#my-radio-1")
    radio_2 = page.locator("#my-radio-2")
    radio_2.check()
    expect(radio_2).to_be_checked()
    expect(radio_1).not_to_be_checked()

    dropdown = page.locator('select[name="my-select"]')
    dropdown.select_option(label="Two")
    expect(dropdown).to_have_value("2")