numero = int(input("Inserisci un numero per vedere il suo codice UNICODE corrispondente, inserisci 0 per terminare"))


if numero >= 0:
    while numero != 0:
        print (str(chr(numero)))
        numero = int(input("Inserisci un numero per vedere il suo codice UNICODE corrispondente, inserisci 0 per terminare"))
    print("K, bye")
else:
    print("Input non valido")
