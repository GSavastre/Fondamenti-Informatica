def comb(s: str):
    combinazioni = []

    for prima_lettera in s:
        for seconda_lettera in s:
            for terza_lettera in s:
                combinazioni.append(prima_lettera + seconda_lettera + terza_lettera)

    return combinazioni
    

def main():
    string = str(input("Inserisci i parametri per le combinazioni: "))
    print(comb(string))

if __name__ == "__main__":
    main()
