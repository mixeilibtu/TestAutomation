# ### დავალება 3 · Checkbox, Radio და Dropdown

# - საიტი: https://rahulshettyacademy.com/AutomationPractice/
# - ნაბიჯები და შემოწმება:
#   - checkbox `Option1` (`#checkBoxOption1`) მონიშნე → `to_be_checked()`, შემდეგ მოხსენი → `not_to_be_checked()`
#   - radio `Radio2` (`value="radio2"`) აირჩიე → `to_be_checked()`
#   - dropdown `#dropdown-class-example`-ში აირჩიე `Option3` → `to_have_value("option3")`
# - მინიშნება: `check()`, `uncheck()`, `select_option(...)`


from playwright.sync_api import Page, expect

URL = "https://rahulshettyacademy.com/AutomationPractice/"


def test_task3_checkbox_radio_dropdown(page: Page):
    page.goto(URL)

    checkbox = page.locator("#checkBoxOption1")
    checkbox.check()
    expect(checkbox).to_be_checked()
    checkbox.uncheck()
    expect(checkbox).not_to_be_checked()

    radio = page.locator("input[value='radio2']")
    radio.check()
    expect(radio).to_be_checked()

    dropdown = page.locator("#dropdown-class-example")
    dropdown.select_option("option3")
    expect(dropdown).to_have_value("option3")