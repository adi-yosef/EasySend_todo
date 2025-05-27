import datetime
from playwright.sync_api import sync_playwright, Page
from src.config.config import TestData

import pytest
import warnings
warnings.filterwarnings("ignore", category=pytest.PytestUnknownMarkWarning)
from src.pom.home_page import HomePage
from src.pom.login_page import LoginPage


@pytest.fixture(scope="function")
def set_up_tear_down():
    start_time = datetime.datetime.now()
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--start-maximized"], slow_mo=200)
        context = browser.new_context(no_viewport=True)
        page = context.new_page()
        print("Run Started at : " + str(start_time))
        print("Chrome Environment Set Up")
        print("--------------------------------------------------------")
        page.goto(TestData.BASE_URL)
        page.wait_for_load_state("networkidle")
        print("Load Page Pass")
        yield page
        context.close()
        browser.close()
    end_time = datetime.datetime.now()
    elapsed_time = end_time - start_time
    print(f"\nTest duration: {elapsed_time.total_seconds():.2f} seconds")


@pytest.fixture
def page(set_up_tear_down) -> Page:
    return set_up_tear_down

@pytest.fixture
def login_page(page: Page) -> LoginPage:
    return LoginPage(page)

@pytest.fixture
def home_page(page: Page) -> HomePage:
    return HomePage(page)
