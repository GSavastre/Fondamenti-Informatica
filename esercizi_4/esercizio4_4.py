def comb(ruote: int, simboli: str)-> str:

    combinazioni = ['']

    if ruote <= 0:
        return ''
    else:
        for r in range(ruote):
            for s in simboli:
                combinazioni[r] = s + comb(ruote - 1,simboli)
                combinazioni.append('')
        return combinazioni

def main():
    ruote = int(input("Quanti spazi? "))
    simboli = str(input("Quali simboli? "))

    print(comb(ruote,simboli))
if __name__ == "__main__":
    main()
