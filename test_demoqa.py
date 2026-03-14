from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
import os


# ===== Impostazioni
options = Options()
#options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.maximize_window()
driver.implicitly_wait(5)

# ===== Credenziali da variabili ambiente (più sicuro)
USERNAME = os.environ.get("DEMOQA_USER", "ottymrc")
PASSWORD = os.environ.get("DEMOQA_PASS", "Password.82!")

try:
    driver.get("https://demoqa.com/login/")

    user_name = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "userName")))
    user_name.send_keys(USERNAME)

    password = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "password")))
    ActionChains(driver).move_to_element(password).click(password).send_keys(PASSWORD).perform()

    login = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "login")))

    ActionChains(driver).move_to_element(login).click(login).perform()

    try:
        error = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.ID, "name")))
        print("Login fallito:", error.text)
    except TimeoutException:
        print("Login riuscito!")

finally:
    driver.quit()