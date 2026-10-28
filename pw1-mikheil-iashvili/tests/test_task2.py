# - საიტი: https://www.saucedemo.com/
# - დაწერე **ერთი** ტესტ-ფუნქცია `@pytest.mark.parametrize`-ით, რომელიც 4 შემთხვევას ამოწმებს:

# | Username        | Password     | შეცდომის ტექსტი                                                             |
# | --------------- | ------------ | --------------------------------------------------------------------------- |
# | locked_out_user | secret_sauce | `Epic sadface: Sorry, this user has been locked out.`                       |
# | standard_user   | wrong        | `Epic sadface: Username and password do not match any user in this service` |
# | (ცარიელი)       | secret_sauce | `Epic sadface: Username is required`                                        |
# | standard_user   | (ცარიელი)    | `Epic sadface: Password is required`                                        |

# - შემოწმება: შეცდომა `[data-test="error"]` ზუსტად ამ ტექსტს შეიცავს (`to_have_text`)
# - შედეგი: `4 passed` მხოლოდ ამ ფუნქციისთვის
import pytest
from playwright.sync_api import Page, expect

URL = "https://www.saucedemo.com/"


@pytest.mark.parametrize(
    "username, password, error_text",
    [
        (
            "locked_out_user",
            "secret_sauce",
            "Epic sadface: Sorry, this user has been locked out.",
        ),
        (
            "standard_user",
            "wrong",
            "Epic sadface: Username and password do not match any user in this service",
        ),
        (
            "",
            "secret_sauce",
            "Epic sadface: Username is required",
        ),
        (
            "standard_user",
            "",
            "Epic sadface: Password is required",
        ),
    ],
    ids=["locked_out", "wrong_password", "empty_username", "empty_password"],
)
def test_task2_login_shows_error(
    page: Page, username: str, password: str, error_text: str
):
    # arrange
    page.goto(URL)

    # act
    page.locator("#user-name").fill(username)
    page.locator("#password").fill(password)
    page.locator("#login-button").click()

    # assert
    expect(page.locator('[data-test="error"]')).to_have_text(error_text)

