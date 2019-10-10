def main():
    contatore_cifre = [0]*10

    testo = input("Inserisci una stringa di testo")
    
    for cont in range(len(testo)):
        if testo[cont] <= "9" and testo[cont] >= "0":
            contatore_cifre[int(testo[cont])] += 1
    print(contatore_cifre)
    
if __name__ == "__main__":
    main()
