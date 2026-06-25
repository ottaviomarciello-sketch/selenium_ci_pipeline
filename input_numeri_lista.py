def main():
    numeri = []

    # 1. Inserimento di 6 numeri
    for i in range(6):
        n = int(input(f"Inserisci il numero {i+1}: "))
        numeri.append(n)

    print("\nLista numeri:", numeri)


    num_cercato = int(input("\nInserisci un numero da cercare: "))
    conteggio = numeri.count(num_cercato)
    print(f"Il numero {num_cercato} compare {conteggio} volte")


    print("\nNumeri pari nella lista:")
    for n in numeri:
        if n % 2 == 0:
            print(n)


    somma = sum(numeri)
    print(f"\nSomma totale: {somma}")


# Entry point
if __name__ == "__main__":
    main()