numero = int(input("Inserisci un numero, inserisci un numero negativo per uscire:"))

massimo = numero
variazione_numero_massimo = 0

while numero >= 0:
    
    if numero > massimo:
        massimo = numero
        variazione_numero_massimo += 1
    
    numero = int(input("Inserisci un numero, inserisci un numero negativo per uscire:"))

print("Numero massimo inserito:",massimo,"Il numero massimo e' variato",variazione_numero_massimo,"volte")
print("K, bye")
