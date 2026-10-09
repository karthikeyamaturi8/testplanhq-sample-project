import os

def test_login_page(page):
    base_url = os.environ.get("BASE_URL")
    page.goto(f"{base_url}/login")
    page.locator("#email").fill("user@example.com")
    page.locator("#password").fill("password123")
    page.locator("button[type='submit']").click()
    page.wait_for_selector(".dashboard")
    assert page.locator(".dashboard").is_visible()
