numero = int(input("Inserisci un numero, inserisci un numero negativo per uscire:"))

massimo = numero
minimo = numero

while numero >= 0:
    
    if numero > massimo:
        massimo = numero
    elif numero < minimo:
        minimo = numero
    
    numero = int(input("Inserisci un numero, inserisci un numero negativo per uscire:"))

print("Numero massimo inserito:",massimo,"Numero minimo inserito",minimo)
print("K, bye")
