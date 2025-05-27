from typing import Optional
from playwright.sync_api import Page
from src.pom.task_page import TaskPage


def edit_existing_task(
        task_name: str, # todo when multiple task are created to edit the right one
        page: Page,
        new_task_name: Optional[str] = None,
        new_description: Optional[str]= None,

) -> None:
    task_page = TaskPage(page)
    task_page.click_task_3dot_menu()
    task_page.click_edit_task()
    if new_description is not None:
        task_page.fill_description(new_description)
    if new_task_name is not None:
        task_page.fill_task_name(new_task_name)
    task_page.click_save_task()

def edit_task_as_done(
        task_name: str, # todo when multiple task are created to edit the right one
        page: Page,
) -> None:
    task_page = TaskPage(page)
    task_page.click_task_3dot_menu()
    task_page.click_mark_as_done_button()
    task_page.click_task_3dot_menu()
    task_page.click_task_details_button()