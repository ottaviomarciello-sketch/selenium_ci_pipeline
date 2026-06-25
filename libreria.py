# ====== DATABASE ======
catalogo_libri = [
    {"isbn": "1", "titolo": "le avvebture della classe 69976", "autore": "luca olivato", "casa_editrice": "mondadori", "qt": 10, "prezzo": 25.5, "genere": "Narrativa"},
    {"isbn": "2", "titolo": "Il nome della rosa", "autore": "Umberto Eco", "casa_editrice": "Bompiani", "qt": 5, "prezzo": 14.0, "genere": "Storico"},
    {"isbn": "3", "titolo": "1984", "autore": "George Orwell", "casa_editrice": "Mondadori", "qt": 12, "prezzo": 12.5, "genere": "Distopico"},
    {"isbn": "4", "titolo": "Il colibrì", "autore": "Sandro Veronesi", "casa_editrice": "La nave di Teseo", "qt": 8, "prezzo": 18.0, "genere": "Narrativa"},
    {"isbn": "5", "titolo": "Il signore degli anelli", "autore": "J.R.R. Tolkien", "casa_editrice": "Bompiani", "qt": 3, "prezzo": 30.0, "genere": "Fantasy"},
]

# ====== FUNZIONI UTILI ======
def stampa_libro(libro):
    print("------ LIBRO ------")
    print(f"isbn: {libro['isbn']}")
    print(f"titolo: {libro['titolo']}")
    print(f"autore: {libro['autore']}")
    print(f"genere: {libro['genere']}")
    print(f"casa editrice: {libro['casa_editrice']}")
    print(f"qt: {libro['qt']}")
    print(f"prezzo: {libro['prezzo']:.2f} €")
    print("--------------------------------")


# ====== RICERCHE ======
def ricerca_per_isbn(isbn):
    for libro in catalogo_libri:
        if libro["isbn"] == isbn:
            stampa_libro(libro)
            return
    print("Libro non trovato")


def ricerca_per_autore(autore):
    trovato = False
    for libro in catalogo_libri:
        if autore.lower() in libro["autore"].lower():
            stampa_libro(libro)
            trovato = True
    if not trovato:
        print("Nessun libro trovato per questo autore")


def catolo_ricerca_genere(genere):
    trovato = False
    for libro in catalogo_libri:
        if libro['genere'].lower() == genere.lower():
            stampa_libro(libro)
            trovato = True
    if not trovato:
        print("Genere non disponibile")


# ====== CRUD ======
def aggiungi_libro():
    isbn = input("Inserisci ISBN: ")
    for libro in catalogo_libri:
        if libro["isbn"] == isbn:
            print("Libro già presente")
            scelta = input("Vuoi modificarlo? (y/n): ").lower()
            if scelta == "y":
                modifica_libro(isbn)
            return

    titolo = input("Titolo: ")
    autore = input("Autore: ")
    casa_editrice = input("Casa editrice: ")
    genere = input("Genere: ")
    qt = int(input("Quantità: "))
    prezzo = float(input("Prezzo: "))

    catalogo_libri.append({
        "isbn": isbn,
        "titolo": titolo,
        "autore": autore,
        "casa_editrice": casa_editrice,
        "qt": qt,
        "prezzo": prezzo,
        "genere": genere
    })

    print("Libro aggiunto!")


def modifica_libro(isbn):
    for libro in catalogo_libri:
        if libro["isbn"] == isbn:
            while True:
                scelta = input("1.prezzo 2.quantità 0.esci: ")
                if scelta == "1":
                    libro["prezzo"] = float(input("Nuovo prezzo: "))
                elif scelta == "2":
                    libro["qt"] = int(input("Nuova quantità: "))
                elif scelta == "0":
                    break
            return
    print("Libro non trovato")


# ====== VENDITA ======
def vendita():
    scontrino = []
    while True:
        opz = input("1.aggiungi 2.chiudi: ")
        if opz == "1":
            inserisci_voce(scontrino)
        elif opz == "2":
            chiusura_scontrino(scontrino)
            break


def inserisci_voce(scontrino):
    isbn = input("ISBN: ")
    for libro in catalogo_libri:
        if libro['isbn'] == isbn:
            qt = int(input("Quantità: "))
            if libro['qt'] >= qt:
                libro['qt'] -= qt
                scontrino.append({
                    "titolo": libro['titolo'],
                    "qt": qt,
                    "prezzo_unitario": libro['prezzo'],
                    "totale": libro['prezzo'] * qt
                })
            else:
                print("Quantità insufficiente")
            return
    print("Libro non trovato")


def chiusura_scontrino(scontrino):
    totale = 0
    print("----- SCONTRINO -----")
    for voce in scontrino:
        print(f"{voce['titolo']} x{voce['qt']} = {voce['totale']}€")
        totale += voce['totale']
    print("Totale:", totale, "€")


# ====== MAIN ======
def main():
    while True:
        print("\n--- MENU ---")
        print("1. Mostra catalogo")
        print("2. Cerca per ISBN")
        print("3. Cerca per autore")
        print("4. Cerca per genere")
        print("5. Aggiungi libro")
        print("6. Vendita")
        print("0. Esci")

        scelta = input("Scelta: ")

        if scelta == "1":
            for libro in catalogo_libri:
                stampa_libro(libro)

        elif scelta == "2":
            ricerca_per_isbn(input("ISBN: "))

        elif scelta == "3":
            ricerca_per_autore(input("Autore: "))

        elif scelta == "4":
            catolo_ricerca_genere(input("Genere: "))

        elif scelta == "5":
            aggiungi_libro()

        elif scelta == "6":
            vendita()

        elif scelta == "0":
            print("Uscita...")
            break

        else:
            print("Scelta non valida")


# ====== ENTRY POINT ======
if __name__ == "__main__":
    main()