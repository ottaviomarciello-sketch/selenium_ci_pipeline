class Contatto:
    def __init__(self, nome, cognome, telefono):
        self.nome = nome
        self.cognome = cognome
        self.telefono = telefono

    def mostra_dettagli(self):
        print(f"Nome: {self.nome}, Cognome: {self.cognome}, Telefono: {self.telefono}")


class AgendaTelefonica:
    def __init__(self):
        self.lista_contatti = []

    def aggiungi_contatto(self, nome, cognome, telefono):
        nuovo = Contatto(nome, cognome, telefono)
        self.lista_contatti.append(nuovo)
        print("Contatto aggiunto!")

    def cerca_contatto(self, nome_cercato):
        trovato = False
        for contatto in self.lista_contatti:
            if contatto.nome.lower() == nome_cercato.lower():
                contatto.mostra_dettagli()
                trovato = True
        if not trovato:
            print("Contatto non trovato.")

    def mostra_tutti_i_contatti(self):
        if not self.lista_contatti:
            print("Agenda vuota.")
        else:
            for contatto in self.lista_contatti:
                contatto.mostra_dettagli()



def main():
    agenda = AgendaTelefonica()

    while True:
        scelta = input("""
1. Aggiungi contatto
2. Mostra tutti i contatti
3. Cerca contatto
0. Esci
Scelta: """)

        if scelta == "1":
            nome = input("Nome: ")
            cognome = input("Cognome: ")
            telefono = input("Telefono: ")
            agenda.aggiungi_contatto(nome, cognome, telefono)

        elif scelta == "2":
            agenda.mostra_tutti_i_contatti()

        elif scelta == "3":
            nome = input("Nome da cercare: ")
            agenda.cerca_contatto(nome)

        elif scelta == "0":
            print("Uscita...")
            break

        else:
            print("Scelta non valida!")


if __name__ == "__main__":
    main()