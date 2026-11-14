# დავალება 3 · პროდუქტის გვერდი parametrize-ით

# - საიტი: [https://www.saucedemo.com/](https://www.saucedemo.com/) · მონაცემები: standard_user / secret_sauce
# - დაწერე **ერთი** ტესტ-ფუნქცია `@pytest.mark.parametrize`-ით. შესვლა გააკეთე fixture-ში.
# - ნაბიჯები: პროდუქტების სიაში დააჭირე პროდუქტის **სახელს** → პროდუქტის გვერდზე შეამოწმე სახელი და ფასი → `Back to products` → სათაური `[data-test="title"]` არის `Products`

# | პროდუქტი                | ფასი     |
# |:----------------------- |:-------- |
# | `Sauce Labs Backpack`   | `$29.99` |
# | `Sauce Labs Bike Light` | `$9.99`  |
# | `Sauce Labs Onesie`     | `$7.99`  |

# - ლოკატორები: `[data-test="inventory-item-name"]`, `[data-test="inventory-item-price"]`
# - დამატებით: URL შეიცავს `inventory-item.html` → `to_have_url(re.compile("inventory-item.html"))`
# - შედეგი: `3 passed` ამ ფუნქციისთვის

import re

import pytest
from playwright.sync_api import Page, expect

URL = "https://www.saucedemo.com/"


@pytest.fixture
def logged_in_page(page: Page) -> Page:
    page.goto(URL)
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()
    expect(page.locator('[data-test="title"]')).to_have_text("Products")
    return page


@pytest.mark.parametrize(
    "product_name, price",
    [
        ("Sauce Labs Backpack", "$29.99"),
        ("Sauce Labs Bike Light", "$9.99"),
        ("Sauce Labs Onesie", "$7.99"),
    ],
)
def test_task_3_product_details(
    logged_in_page: Page, product_name: str, price: str
):
    product = logged_in_page.locator('[data-test="inventory-item-name"]').get_by_text(
        product_name, exact=True
    )
    product.click()

    expect(logged_in_page).to_have_url(re.compile("inventory-item.html"))
    expect(logged_in_page.locator('[data-test="inventory-item-name"]')).to_have_text(
        product_name
    )
    expect(logged_in_page.locator('[data-test="inventory-item-price"]')).to_have_text(
        price
    )

    logged_in_page.get_by_role("button", name="Back to products").click()
    expect(logged_in_page.locator('[data-test="title"]')).to_have_text("Products")