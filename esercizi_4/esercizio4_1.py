def MCD(a,b):
    if a == b:
        return a
    elif a == 0:
        return b
    elif b == 0:
        return a
    else:
        return MCD(b, a % b)
    

    

def main():
    a = int(input("Inserisci il primo numero: "))
    b = int(input("Inserisci il secondo numero: "))

    mcd = MCD(a,b)

    print("Il massimo comune divisore e': ",mcd)

if __name__ == "__main__":
    main()
