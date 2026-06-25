class Brano:
    def __init__(self, nome, autore, genere, lunghezza):
        self.nome = nome
        self.autore = autore
        self.genere = genere
        self.lunghezza = lunghezza

    def mostra_scheda(self):
        print(f"nome: {self.nome} | autore: {self.autore} | genere: {self.genere} | lunghezza: {self.lunghezza}")


class Playlist:
    def __init__(self, nome):
        self.nome = nome
        self.brani = []

    def aggiungi_brano(self):
        n = input("nome canzone: ")
        a = input("autore canzone: ")
        g = input("genere canzone: ")
        t = int(input("tempo in secondi della canzone: "))
        self.brani.append(Brano(n, a, g, t))

    def stampa_lista(self):
        for traccia in self.brani:
            traccia.mostra_scheda()
        print(f"durata play list: {self.durata_playList()}")

    def durata_playList(self):
        somma = 0
        for traccia in self.brani:
            somma += traccia.lunghezza
        return somma

    def rimuovi_brano(self):
        titolo = input("inserisci tittolo da rimuovere: ")
        for traccia in self.brani:
            if titolo == traccia.nome:
                self.brani.pop(self.brani.index(traccia))

        print("canzone elimanata")


def main():
    nome_play = input("dai nome alla tua play list: ")
    p = Playlist(nome_play)
    menu = '''
    1.aggiungi canzone alla play list
    2.mostra play list
    3.rimuovi dalla play list
    0.esci
    '''
    while True:
        print(menu)
        opz = input("scelta: ")
        match opz:
            case "1":
                p.aggiungi_brano()
            case "2":
                p.stampa_lista()
            case "3":
                p.rimuovi_brano()
            case "0":
                break


if __name__ == "__main__":
    main()