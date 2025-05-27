from playwright.sync_api import expect
from src.steps.create_new_task import create_new_task_home_page
from src.steps.delete_task import delete_existing_task

import pytest
pytestmark = [pytest.mark.ui, pytest.mark.delete_task]

def test_delete_task(page):
    create_new_task_home_page("adi", "my first test", page)
    expect(page.get_by_role("heading", name="adi")).to_be_visible()
    delete_existing_task("adi", page)
