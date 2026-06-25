class Visita:
    def __init__(self, data, tipo, descrizione):
        self.data = data
        self.tipo = tipo
        self.descrizione = descrizione

    def stampa_visita(self):
        print(f"{self.data} | {self.tipo}\n{self.descrizione}")


class Paziente:
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome
        self.visite = []

    def aggiungi_visita(self, visita):
        self.visite.append(visita)

    def stampa_scheda_paziente(self):
        print(f"PAZIENTE: {self.nome} {self.cognome}")
        for visita in self.visite:
            visita.stampa_visita()


def main():
    lu = Paziente("Luca", "Olivato")
    while True:
        opz = input('''
        1.aggiungi visita
        2.mistra scheda Paziente
        0.esci
        la tua scelta: 
        ''')
        if opz == "1":
            data = input("inserisci data visita: ")
            tipo = input("inserisci tipologia visita: ")
            descrizione = input("inserisci referto visita: ")
            lu.aggiungi_visita(Visita(data, tipo, descrizione))
        elif opz == "2":
            lu.stampa_scheda_paziente()
        elif opz == "0":
            break


if __name__ == "__main__":
    main()