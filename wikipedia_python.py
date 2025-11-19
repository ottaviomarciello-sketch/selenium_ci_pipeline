from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from datetime import datetime
import time

def run_selenium_test():
    print(f"Esecuzione test Selenium: {datetime.now()}")

    # Opzioni Chromium headless
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--remote-debugging-port=9222")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--log-level=3")

    # Percorso Chromedriver installato da apt
    driver = webdriver.Chrome(
        service=Service("/usr/bin/chromedriver"),
        options=options
    )

    try:
        # Vai su Wikipedia
        driver.get("https://www.wikipedia.org/")

        # Clic su lingua italiana
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "js-link-box-it"))
        ).click()

        # Input di ricerca
        search_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "search"))
        )
        search_input.send_keys("Python")

        # Clic sul pulsante di ricerca
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.cdx-search-input__end-button"))
        ).click()

        # Attendi caricamento titolo pagina
        page_title = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "firstHeading"))
        )
        print("Pagina caricata:", page_title.text)

    finally:
        print("Test completato, chiudo il browser.")
        driver.quit()


if __name__ == "__main__":
    run_selenium_test()

