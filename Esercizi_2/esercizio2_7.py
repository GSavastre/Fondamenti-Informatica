def len_common_prefix(a: str, b: str) -> int:

    lettere_uguali = cont = 0
    
    if len(a) < len(b):
        while cont <= len(a) -1 and a[cont] == b[cont]:
            lettere_uguali += 1
            cont += 1
    elif len(b) < len(a):
         while cont <= len(b)-1 and b[cont] == a[cont]:
            lettere_uguali += 1
            cont += 1
    else:
        while cont <= len(a)-1 and a[cont] == b[cont]:
            lettere_uguali += 1
            cont += 1
    return lettere_uguali
    
def main():
    stringa_1 = input("Inserisci la prima stringa")
    stringa_2 = input("Inserisci la seconda stringa")

    print("Ci sono ",len_common_prefix(stringa_1, stringa_2),"lettere iniziali uguali")

if __name__ == "__main__":
    main()
