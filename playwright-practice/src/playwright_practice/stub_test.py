from playwright.sync_api import Page, expect


def test_name_field_is_visible(page: Page):
    page.goto("https://demoqa.com/text-box")
    expect(page.locator("#userName")).to_be_visible()