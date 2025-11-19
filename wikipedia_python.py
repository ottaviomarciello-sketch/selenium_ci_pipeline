from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime_t me import datetime

def safe_click(driver, locator, retries=3):
    for _ in range(retries):
        try:
            elem = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(locator)
            )
            elem.click()
            return
        except:
            pass
    raise Exception("Impossibile cliccare l’elemento")

def run_selenium_test():
    print(f"Esecuzione test Selenium: {datetime.now()}")

    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(
        service=Service("/usr/bin/chromedriver"),
        options=options
    )

    try:
        driver.get("https://www.google.com")

        # Accetta i cookie (Google potrebbe chiederlo)
        try:
            safe_click(driver, (By.ID, "L2AGLb"))
        except:
            pass  # Se non c'è, va bene lo stesso

        search_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "q"))
        )
        search_input.send_keys("Selenium WebDriver Python\n")

        # Verifica che il titolo sia corretto
        WebDriverWait(driver, 10).until(
            EC.title_contains("Selenium WebDriver Python")
        )

        print("Test OK — pagina caricata!")

    finally:
        print("Test completato, chiudo il browser.")
        driver.quit()

if __name__ == "__main__":
    run_selenium_test()
