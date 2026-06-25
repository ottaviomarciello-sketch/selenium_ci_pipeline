from datetime import datetime


class Cittadino
        self.nome = ""
        self.cognome = ""
        self.age = 0
        self.diritto_voto = False

    def dati(self):
        oggi = datetime.now()
        anno_attuale = oggi.year
        name = input("inserisci nome: ")
        surname = input("nserisci cognome: ")
        anno_nascita = int(input("inserisci anno di nascita:"))
        self.nome = name
        self.cognome = surname
        self.age = anno_attuale - anno_nascita
        if self.age >= 18:
            self.diritto_voto = True
        else:
            self.diritto_voto = False

    def puoi_votare(self):
        if self.diritto_voto:
            return "ho il diritto al voto"
        else:
            return "non puoi votare"

    def stampa_scheda(self):
        print(f"nome: {self.nome}")
        print(f"cognome: {self.cognome}")
        print(f"anni: {self.age}")
        print(f"direitto al voto  {self.puoi_votare()}")


luca = Cittadino()
print(luca.nome)
luca.dati()
print(luca.nome)
luca.stampa_scheda()

elide = Cittadino()
elide.dati()
elide.stampa_scheda()