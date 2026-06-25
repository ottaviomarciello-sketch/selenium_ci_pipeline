from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()

    # Vai alla pagina di login
    page.goto("https://demoqa.com/login")

    # pausa per debug (apre Playwright Inspector)
    page.pause()

    # inserisci username
    page.fill("#userName", "testuser")

    # inserisci password
    page.fill("#password", "Password123!")

    # click login
    page.click("#login")

    # stampa il titolo della pagina
    print(page.title())

    # tieni il browser aperto qualche secondo
    page.wait_for_timeout(5000)

    browser.close()