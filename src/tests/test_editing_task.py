from playwright.sync_api import expect
from src.steps.create_new_task import create_new_task_home_page
from src.steps.edit_existing_task import edit_existing_task, edit_task_as_done

import pytest
pytestmark = [pytest.mark.ui, pytest.mark.edit_task]

def test_edit_task(page):
    create_new_task_home_page("adi", "my first test", page)
    expect(page.get_by_role("heading", name="adi")).to_be_visible()
    edit_existing_task("adi",page, "my new task name", "my new description")

def test_mark_as_done(page):
    create_new_task_home_page("adi done task", "my done test", page)
    expect(page.get_by_role("heading", name="adi")).to_be_visible()
    edit_task_as_done("adi done task", page)
    row = page.locator("tr:has(th:text('Done:'))")
    expect(row.locator("td")).to_contain_text("true")
