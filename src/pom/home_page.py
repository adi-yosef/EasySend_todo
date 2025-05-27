

class HomePage:
    def __init__(self, page) -> None:
        self.page = page

        """mapping all elements in page"""
        self.sidebar_button = page.get_by_role("button", name="Sidebar")
        self.plus_button = page.locator("button[aria-label='Add Task']")
        self.new_task_sidebar = page.get_by_role("link", name="Add Task")
        self.search_task_box = page.locator("input[type='text']").first

        # todo complete all elements for future tests

        """actions on the page"""
    def click_new_task(self):
        self.page.wait_for_selector("button[aria-label='Add Task']", state="visible")
        self.plus_button.click(force=True)

    def click_sidebar(self):
        self.sidebar_button.click()

    def click_new_task_sidebar(self):
        self.new_task_sidebar.click()

    def search_task(self, task_name: str):
        self.search_task_box.clear()
        self.search_task_box.fill(task_name)
        print(f"searching for {task_name} task")
        # todo complete all actions on page





