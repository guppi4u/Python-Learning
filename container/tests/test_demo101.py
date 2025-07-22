# tests/test_example.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os

# Define a fixture for the WebDriver
@pytest.fixture(scope="module")
def driver():
    """
    Sets up a Chrome WebDriver instance for tests.
    """
    print("\nSetting up Chrome WebDriver...")
    chrome_options = Options()
    # Run Chrome in headless mode (no visible browser UI) - essential for Codespaces
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox") # Required for running in container environments
    chrome_options.add_argument("--disable-dev-shm-usage") # Overcomes limited resource problems

    # Path to ChromeDriver - it's automatically added to PATH by the dev container feature
    # service = Service(executable_path="/usr/local/bin/chromedriver") # Explicit path if needed, but feature handles it

    # Initialize WebDriver
    try:
        # The Dev Container feature ensures chromedriver is in PATH, so no explicit path needed
        driver_instance = webdriver.Chrome(options=chrome_options)
        print("Chrome WebDriver initialized successfully.")
    except Exception as e:
        print(f"Error initializing Chrome WebDriver: {e}")
        pytest.fail(f"Could not initialize Chrome WebDriver: {e}")

    # Set an implicit wait for elements to appear
    driver_instance.implicitly_wait(10)

    yield driver_instance # Provide the driver to the test functions

    # Teardown: Close the browser after all tests in the module are done
    print("Closing Chrome WebDriver...")
    driver_instance.quit()
    print("Chrome WebDriver closed.")

# A simple test using the driver fixture
def test_google_search(driver):
    """
    Tests searching on Google.
    """
    print("Navigating to Google...")
    driver.get("https://www.google.com")
    assert "Google" in driver.title
    print(f"Page title: {driver.title}")

    # Find the search box and enter text
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Dev Containers VS Code")
    search_box.submit()

    # Verify results page title
    assert "Dev Containers VS Code" in driver.title
    print(f"Search results title: {driver.title}")

    # Take a screenshot (optional, but good for debugging headless tests)
    screenshot_path = os.path.join(os.getcwd(), "google_search_results.png")
    driver.save_screenshot(screenshot_path)
    print(f"Screenshot saved to: {screenshot_path}")

    print("Google search test passed.")

def test_duckduckgo_search(driver):
    """
    Tests searching on DuckDuckGo.
    """
    print("Navigating to DuckDuckGo...")
    driver.get("https://duckduckgo.com")
    assert "DuckDuckGo" in driver.title
    print(f"Page title: {driver.title}")

    # Find the search box and enter text
    search_box = driver.find_element(By.ID, "search_form_input_homepage")
    search_box.send_keys("Selenium Pytest Dev Container")
    search_box.submit()

    # Verify results page title
    assert "Selenium Pytest Dev Container at DuckDuckGo" in driver.title
    print(f"Search results title: {driver.title}")
    print("DuckDuckGo search test passed.")
