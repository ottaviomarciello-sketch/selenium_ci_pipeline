from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from datetime import datetime
import time

def safe_click(driver, locator, retries=3):
    """Clicca in sicurezza evitando StaleElementReferenceException."""
    for _ in range(retries):
        try:
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(locator)
            ).click()
            return
        except StaleElementReferenceException:
            time.sleep(1)
    raise Exception(f"Elemento sempre stale: {locator}")

def run_selenium_test():
    print(f"Esecuzione test Selenium: {datetime.now()}")

    # Chrome options headless compatibili Docker/ARM
    options = webdriver.ChromeOptions()
    options.binary_location = "/usr/bin/chromium"  # percorso di Chromium su Linux
    options.add_argument("--headless=new")  # usa il nuovo headless mode
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--log-level=3")

    # Avvia Chromium con ChromeDriver
    driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver", options=options)

    try:
        # Vai su Wikipedia
        driver.get("https://www.wikipedia.org/")

        # Clic lingua italiana
        safe_click(driver, (By.ID, "js-link-box-it"))

        # Campo ricerca
        search_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "search"))
        )
        search_input.send_keys("Python")

        # Click sul pulsante di ricerca
        safe_click(driver, (By.CSS_SELECTOR, "button.cdx-search-input__end-button"))

        # Attendi il titolo della pagina
        page_title = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "firstHeading"))
        )
        print("Pagina caricata:", page_title.text)

    finally:
        print("Test completato, chiudo il browser.")
        driver.quit()


if __name__ == "__main__":
    run_selenium_test()
