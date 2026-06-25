class Cuffie:
    def __init__(self, marca, modello, prezzo, tipologia, wireless):
        self.marca = marca
        self.modello = modello
        self.prezzo = prezzo
        self.tipologia = tipologia
        self.wireless = wireless


    def stampa_scheda(self):
        print(f"Scheda tecnica marca: {self.marca} modello:{self.modello} prezzo: {self.prezzo} tipologia {self.tipologia} wireless: {self.wireless}")


marca = input("Inserisci la marca: ")
modello = input("Inserisci la modello: ")
prezzo = input("Inserisci la prezzo: ")
tipologia = input("Inserisci la tipologia: ")
wireless = input("Inserisci la wireless: ")

m = Cuffie(marca, modello, prezzo, tipologia, wireless)
m.stampa_scheda()
