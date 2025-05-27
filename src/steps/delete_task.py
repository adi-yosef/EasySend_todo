from playwright.sync_api import Page
from src.pom.task_page import TaskPage


def delete_existing_task(
        task_name: str, # todo when multiple task are created to delete the right one
        page: Page,

) -> None:
    task_page = TaskPage(page)
    task_page.click_task_3dot_menu()
    task_page.click_delete_button()
    task_page.click_confirm_delete_button()
