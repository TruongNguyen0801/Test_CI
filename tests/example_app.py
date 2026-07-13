from playwright.sync_api import Page

def test_app_example(page:Page):
    page.goto("http://localhost:8000/example.html")
    page.locator("button.btn-primary").click()
    page.locator("button.btn-success").click()