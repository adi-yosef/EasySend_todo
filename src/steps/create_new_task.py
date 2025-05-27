from playwright.sync_api import Page, expect

from src.pom.task_page import TaskPage
from src.pom.home_page import HomePage


def create_new_task_home_page(
        task_name: str,
        description: str,
        page: Page,
        visible_create_button = True
) -> None:
    home_page = HomePage(page)
    home_page.click_new_task()
    task_page = TaskPage(page)
    expect(task_page.create_task_button).to_be_visible()
    task_page.fill_task_name(task_name)
    task_page.fill_description(description)
    if visible_create_button:
        task_page.click_create_task()




def create_new_task_sidebar(
        task_name: str,
        description: str,
        page: Page
) -> None:
    home_page = HomePage(page)
    home_page.click_sidebar()
    home_page.click_new_task_sidebar()
    add_new_task_page = TaskPage(page)
    expect(add_new_task_page.create_task_button).to_be_visible()
    add_new_task_page.fill_task_name(task_name)
    add_new_task_page.fill_description(description)
    add_new_task_page.click_create_task()

