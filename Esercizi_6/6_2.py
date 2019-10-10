def bin(num: int)-> str:
    ris = ""
    if num == 0:
        return ""
    elif num % 2 != 0:
        ris += "1"
    else:
        ris += "0"

    ris += bin(num//2)
    return ris

def main():
    numero = int(input("Inserisci un numero: "))
    print(numero," in binario e': ",bin(numero)[::-1])


if __name__ == "__main__":
     main()
