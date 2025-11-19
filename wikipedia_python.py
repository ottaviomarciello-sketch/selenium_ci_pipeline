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

    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")  # modalità invisibile per Jenkins
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--log-level=3")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        driver.get("https://www.wikipedia.org/")
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "js-link-box-it"))
        ).click()

        try:
            WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, "label[for='skin-client-pref-vector-feature-custom-font-size-value-0']")
                )
            ).click()
        except:
            pass

        search_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "search"))
        )
        search_input.send_keys("Python")
        driver.find_element(By.CSS_SELECTOR, "button.cdx-search-input__end-button").click()

        page_title = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "firstHeading"))
        )
        print("Pagina caricata:", page_title.text)

        python_link = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//table[contains(@class,'infobox')]/tbody//tr[th[a[text()='Sito web']]]/td//a")
            )
        )
        ActionChains(driver).move_to_element(python_link).perform()
        driver.execute_script("arguments[0].click();", python_link)
        print("Click su www.python.org eseguito!")
        time.sleep(2)

    finally:
        print("Test completato, chiudo il browser.")
        driver.quit()

if __name__ == "__main__":
    run_selenium_test()