valori_maggiori = 0
lista_numeri = []

numero = int(input("Inserisci un numero, inserisci un numero negativo per uscire:"))

if numero >= 0:
    lista_numeri.append(numero)


while numero >= 0:
    
    numero = int((input("Inserisci un numero, inserisci un numero negativo per uscire:")))
    if numero >= 0:
        lista_numeri.append(numero)  

for cont in range(len(lista_numeri)-1):
    if lista_numeri[cont] > lista_numeri[len(lista_numeri)-1]:
        valori_maggiori += 1

print("Ci sono ",valori_maggiori,"elementi che sono maggiori dell'ultimo elemento valido inserito")
