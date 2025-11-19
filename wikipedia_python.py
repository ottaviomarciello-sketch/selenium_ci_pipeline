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
    options.add_argument("--headless")  # modalità invisibile
    options.add_argument("--no-sandbox")  # necessario in container Linux
    options.add_argument("--disable-dev-shm-usage")  # evita errori di memoria
    options.add_argument("--disable-gpu")
    options.add_argument("--log-level=3")  # riduce log verbose
    options.add_argument("--window-size=1920,1080")  # headless ha spesso risoluzioni basse

    # Inizializza ChromeDriver con WebDriverManager
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    try:
        # Vai su Wikipedia
        driver.get("https://www.wikipedia.org/")

        # Clic su lingua italiana
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

        # Trova link al sito ufficiale Python e clicca
        python_link = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//table[contains(@class,'infobox')]/tbody//tr[th[a[text()='Sito web']]]/td//a")
            )
        )

        try:
            python_link.click()
        except:
            # fallback in headless per click JS
            ActionChains(driver).move_to_element(python_link).perform()
            driver.execute_script("arguments[0].click();", python_link)

        print("Click su www.python.org eseguito!")
        time.sleep(2)

    finally:
        print("Test completato, chiudo il browser.")
        driver.quit()


if __name__ == "__main__":
    run_selenium_test()
