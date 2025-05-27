from playwright.sync_api import expect

from src.pom.home_page import HomePage
from src.steps.create_new_task import create_new_task_home_page

import pytest
pytestmark = [pytest.mark.ui, pytest.mark.search_task]

def test_add_task_from_home_page(page):
    create_new_task_home_page("adi", "my first test", page)
    expect(page.get_by_role("heading", name="adi")).to_be_visible()
    create_new_task_home_page("Dan", "just another test", page)
    expect(page.get_by_role("heading", name="Dan")).to_be_visible()
    home_page = HomePage(page)
    home_page.search_task("adi")
    expect(page.get_by_role("heading", name="adi")).to_be_visible()
    expect(page.get_by_role("heading", name="Dan")).not_to_be_visible()



