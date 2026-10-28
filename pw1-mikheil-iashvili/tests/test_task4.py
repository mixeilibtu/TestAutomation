# ### დავალება 4 · ალერტები

# - საიტი: https://demoqa.com/alerts
# - დაწერე **ორი** ტესტი:
#   - On button click, prompt box will appear Click me ღილაკს დააჭირეთ

#   - ველში `Please enter your name` ჩაწერე შენი სახელი → დააჭირე `Alert` OK → ტექსტი უნდა გამოჩნდეს გვერდზე `You entered {name}`
#   - შეამოწმეთ რომ ტექსტი მჭვანეა

import re

from playwright.sync_api import Page, expect

URL = "https://demoqa.com/alerts"
NAME = "Mikheil"


def open_prompt_and_answer(page: Page, name: str):
    page.goto(URL, wait_until="domcontentloaded")

    page.once("dialog", lambda dialog: dialog.accept(name))

    page.locator("#promtButton").click()


def test_task4_prompt_shows_entered_name(page: Page):
    open_prompt_and_answer(page, NAME)

    expect(page.locator("#promptResult")).to_have_text(f"You entered {NAME}")


def test_task4_prompt_result_is_green(page: Page):
    open_prompt_and_answer(page, NAME)

    result = page.locator("#promptResult")

    expect(result).to_have_class(re.compile(r"\btext-success\b"))

    expect(result).to_have_css("color", "rgb(25, 135, 84)")
