from playwright.sync_api import expect
from src.steps.create_new_task import create_new_task_home_page, create_new_task_sidebar
import pytest

pytestmark = [pytest.mark.ui, pytest.mark.new_task]

def test_add_task_from_home_page(page):
    create_new_task_home_page("adi", "my first test", page)
    expect(page.get_by_role("heading", name="adi")).to_be_visible()


def test_add_task_from_sidebar(page):
    create_new_task_sidebar("adi2","my 2nd test", page)
    expect(page.get_by_role("heading", name="adi2")).to_be_visible()

def test_add_task_with_long_name(page):
    create_new_task_home_page("a new task with a very long name", "my long name task", page)
    expect(page.get_by_role("heading", name="a new task with a very long name")).to_be_visible()

def test_add_task_with_a_very_long_name_that_fails(page):
    create_new_task_home_page("a new task with a very long name that will fail", "my long name task",
                              page, False)
    expect(page.get_by_text("Name should be less than or")).to_be_visible()

def test_add_task_with_empty_name(page):
    create_new_task_home_page("", "an empty task name", page)
    expect(page.get_by_text("Task name is required.")).to_be_visible()




