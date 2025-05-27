from playwright.sync_api import expect
from src.steps.create_new_task import create_new_task_home_page

import pytest
pytestmark = [pytest.mark.ui, pytest.mark.refresh_page]

def test_add_task_from_home_page(page):
    create_new_task_home_page("test refresh", "my first test", page)
    expect(page.get_by_role("heading", name="test refresh")).to_be_visible()
    page.reload(wait_until="networkidle")
    print("refresh page")
    expect(page.get_by_role("heading", name="test refresh")).to_be_visible()
