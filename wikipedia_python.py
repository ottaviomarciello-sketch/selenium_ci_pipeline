from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
import time

def run_selenium_test():
    print(f"Esecuzione test Selenium: {datetime.now()}")

    # Opzioni Chrome headless ottimizzate per container
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--remote-debugging-port=9222")
    options.add_argument("--log-level=3")
    options.add_argument("--window-size=1920,1080")

    # Inizializza ChromeDriver con WebDriverManager
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    try:
        # Vai su Wikipedia
        driver.get("https://www.wikipedia.org/")

        # Clic lingua italiana
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "js-link-box-it"))
        ).click()

        # Prova a cliccare opzione font-size se presente
        try:
            WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, "label[for='skin-client-pref-vector-feature-custom-font-size-value-0']")
                )
            ).click()
        except Exception as e:
            print("Opzione font-size non cliccabile:", e)

        # Input ricerca
        search_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "search"))
        )
        search_input.send_keys("Python")

        # Clic pulsante ricerca
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.cdx-search-input__end-button"))
        ).click()

        # Attendi titolo pagina
        page_title = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "firstHeading"))
        )
        print("Pagina caricata:", page_title.text)

        # Trova link sito ufficiale Python
        python_link = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//table[contains(@class,'infobox')]/tbody//tr[th[a[text()='Sito web']]]/td//a")
            )
        )

        try:
            python_link.click()
        except:
            driver.execute_script("arguments[0].click();", python_link)

        print("Click su www.python.org eseguito!")
        time.sleep(2)

    finally:
        print("Test completato, chiudo il browser.")
        driver.quit()


if __name__ == "__main__":
    run_selenium_test()
