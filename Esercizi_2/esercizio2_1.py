def contacifre (stringa: str):
    somma = 0
    conta = 0
    
    for cont in range(len(stringa)):
        somma += 1
        if stringa[cont] >="0"  and stringa[cont] <= "9":
            conta += 1
    print("Ci sono ",conta / somma * 100,"% cifre presenti")

def main():
    stringa = input("inserisci una riga di testo:")
    contacifre(stringa)

if __name__ == "__main__":
    main()
