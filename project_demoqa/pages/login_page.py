# Importa la variabile BASE_URL dal file di configurazione
# Serve per evitare di hardcodare l'URL nel codice
from project_demoqa.utils.config import BASE_URL

# Importa "expect" di Playwright
# Serve per fare assertion con wait automatiche (molto importante)
from playwright.sync_api import expect


# Definizione della classe LoginPage (Page Object Model)
# Rappresenta la pagina di login dell'applicazione
class LoginPage:

    # Costruttore della classe
    # Viene eseguito quando crei l'oggetto LoginPage(page)
    def __init__(self, page):

        # Salva l'oggetto Playwright "page" dentro la classe
        # Così possiamo usarlo in tutti i metodi senza ripassarlo
        self.page = page

        # ========================
        # Locator centralizzati
        # ========================

        # Selettore CSS per il campo username (id="userName")
        self.username_input = "#userName"

        # Selettore CSS per il campo password (id="password")
        self.password_input = "#password"

        # Selettore CSS per il bottone login (id="login")
        self.login_button = "#login"

        # Selettore dell'elemento che appare dopo login riuscito
        # Contiene il nome utente loggato
        self.profile_name = "#userName-value"

        # Selettore del messaggio di errore login
        self.error_message = "#name"


    # Metodo per aprire la pagina di login
    def go_to_login(self):

        # Naviga verso l'URL di login costruito con BASE_URL
        # Esempio: https://demoqa.com/login
        self.page.goto(f"{BASE_URL}/login")


    # Metodo per eseguire il login
    def login(self, username, password):

        # Inserisce il valore "username" nel campo username
        self.page.fill(self.username_input, username)

        # Inserisce il valore "password" nel campo password
        self.page.fill(self.password_input, password)

        # Clicca sul bottone di login
        self.page.click(self.login_button)


    # Metodo per verificare se il login è andato a buon fine
    def is_login_successful(self):

        # Crea un locator per l'elemento che indica login riuscito
        locator = self.page.locator(self.profile_name)

        # Aspetta (max 5 secondi) che l'elemento sia visibile
        # Se non appare → test fallisce automaticamente
        expect(locator).to_be_visible(timeout=5000)

        # Se arriva qui significa che il login è riuscito
        return True


    # Metodo per ottenere il messaggio di errore del login
    def get_error_message(self):

        # Crea un locator per il messaggio di errore
        locator = self.page.locator(self.error_message)

        # Aspetta che il messaggio sia visibile (max 5 secondi)
        # Serve per evitare errori di timing
        expect(locator).to_be_visible(timeout=5000)

        # Restituisce il testo del messaggio di errore
        return locator.inner_text()

