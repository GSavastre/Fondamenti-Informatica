def change_string(text: str)->str:
    attivo = False
    new_text = ""
    
    for n in range(len(text)):
        if text[n] == "*" and not attivo :
            attivo = True
        elif text[n] == "*" and attivo:
            attivo = False
        elif attivo:
            new_text += text[n].upper()
        elif not attivo:
            new_text += text[n]
    return new_text
            

def main():
    new_str = str(input("Inserisci una stringa: "))
    new_str = change_string(new_str)
    print(new_str)

if __name__ == "__main__":
    main()
