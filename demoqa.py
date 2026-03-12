# ============================================================
# IMPORT DELLE LIBRERIE NECESSARIE PER L'AUTOMAZIONE SELENIUM
# ============================================================

from selenium import webdriver                          # Modulo principale per avviare e controllare il browser
from selenium.webdriver.common.by import By              # Classe per localizzare elementi nel DOM (ID, XPATH, CSS, ecc.)
from selenium.webdriver.chrome.service import Service    # Gestisce il servizio del ChromeDriver
from selenium.webdriver.support.ui import WebDriverWait  # Gestisce le attese esplicite
from selenium.webdriver.support import expected_conditions as EC  # Condizioni per i WebDriverWait
from selenium.webdriver import ActionChains              # Azioni avanzate (hover, drag&drop, click complessi)
from selenium.common.exceptions import TimeoutException  # Eccezione per timeout dei WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager # Scarica automaticamente la versione corretta del ChromeDriver

# ============================================================
# SETUP DEL DRIVER
# ============================================================

# Inizializza Chrome utilizzando ChromeDriverManager (evita problemi di compatibilità)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Massimizza la finestra per evitare problemi di elementi non visibili
driver.maximize_window()

try:
    # ============================================================
    # APERTURA DELLA PAGINA DI LOGIN
    # ============================================================
    driver.get("https://demoqa.com/login/")  # Naviga alla pagina di login del sito demo

    # ============================================================
    # INSERIMENTO USERNAME
    # ============================================================

    # Attende che il campo username sia visibile (max 10 secondi)
    user_name = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "userName"))
    )
    user_name.send_keys("ottymrc")  # Inserisce lo username

    # ============================================================
    # INSERIMENTO PASSWORD (con scroll e click sicuro)
    # ============================================================

    # Attende che il campo password sia visibile
    password = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "password"))
    )

    # Usa ActionChains per evitare problemi di click non registrati
    ActionChains(driver)\
        .move_to_element(password)\
        .click(password)\
        .send_keys("Password.82!")\
        .perform()

    # ============================================================
    # CLICK SUL PULSANTE LOGIN
    # ============================================================

    # Attende che il pulsante login sia cliccabile
    login = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "login"))
    )

    # Click tramite ActionChains per maggiore affidabilità
    ActionChains(driver)\
        .move_to_element(login)\
        .click(login)\
        .perform()

    # ============================================================
    # CONTROLLO EVENTUALE MESSAGGIO DI ERRORE
    # ============================================================

    try:
        # Attende fino a 3 secondi un eventuale messaggio di errore
        error = WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located((By.ID, "name"))  # ID del messaggio di errore su demoqa
        )
        print("Login fallito:", error.text)

    except TimeoutException:
        # Nessun errore trovato → login riuscito
        print("Login riuscito!")

# ============================================================
# CHIUSURA DEL BROWSER
# ============================================================

finally:
    driver.quit()  # Chiude il browser in ogni caso (successo o errore)