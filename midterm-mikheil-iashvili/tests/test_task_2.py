#  დავალება 2 · Radio ღილაკები

# - საიტი: [https://demoqa.com/radio-button](https://demoqa.com/radio-button)
# - ნაბიჯები და შემოწმება:
#   - აირჩიე `Yes` → ტექსტი `You have selected Yes`
#   - აირჩიე `Impressive` → ტექსტი `You have selected Impressive`
#   - `No` გათიშულია → `#noRadio` → `to_be_disabled()`
# - მინიშნება: ტექსტი არის `p.mt-3`-ში, არჩეული სიტყვა — `.text-success`-ში; დააჭირე label-ს: `get_by_text("Yes", exact=True)`

from playwright.sync_api import Page, expect

URL = "https://demoqa.com/radio-button"


def test_task_2_radio_buttons(page: Page):
    page.goto(URL)

    page.get_by_text("Yes", exact=True).click()
    expect(page.locator("p.mt-3")).to_have_text("You have selected Yes")
    expect(page.locator(".text-success")).to_have_text("Yes")

    page.get_by_text("Impressive", exact=True).click()
    expect(page.locator("p.mt-3")).to_have_text("You have selected Impressive")
    expect(page.locator(".text-success")).to_have_text("Impressive")

    expect(page.locator("#noRadio")).to_be_disabled()
