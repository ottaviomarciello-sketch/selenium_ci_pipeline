import random  # serve per generare valori casuali
import string  # contiene lettere e caratteri (a-z, A-Z, ecc.)
from playwright.sync_api import expect  # funzione di Playwright per fare assert (qui non usata)


class RegisterPage:  # classe che rappresenta la pagina di registrazione
    def __init__(self, page):  # costruttore: viene chiamato quando crei l'oggetto
        self.page = page  # salva la pagina Playwright per usarla nei metodi

        # qui definiamo i "locator" (selettori) degli elementi della pagina
        self.firstname = "#firstname"  # campo nome
        self.lastname = "#lastname"  # campo cognome
        self.username = "#userName"  # campo username
        self.password = "#password"  # campo password
        self.register_btn = "#register"  # bottone Register

    def go(self, base_url):
        # apre la pagina di registrazione usando l'URL base
        self.page.goto(f"{base_url}/register")

    def generate_user(self):
        # crea una stringa casuale di 5 lettere (es: abcde)
        rand = ''.join(random.choices(string.ascii_lowercase, k=5))

        # restituisce username e password
        # esempio: user_abcdx, Password123!
        return f"user_{rand}", "Password123!"

    def register(self, user, pwd):
        # intercetta eventuali popup (alert) e clicca automaticamente "OK"
        self.page.on("dialog", lambda dialog: dialog.accept())

        # inserisce "Test" nel campo nome
        self.page.fill(self.firstname, "Test")

        # inserisce "User" nel campo cognome
        self.page.fill(self.lastname, "User")

        # inserisce lo username passato al metodo
        self.page.fill(self.username, user)

        # inserisce la password passata al metodo
        self.page.fill(self.password, pwd)

        # DemoQA ha CAPTCHA → non registrerà davvero l’utente
        # quindi questo click è solo simulato (non crea un vero utente)
        self.page.click(self.register_btn)