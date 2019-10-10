new_text = ""

attivo = False

with open("5_1_text.txt", "r") as f3:
    for line in f3:
        for n in range(len(line)):
            if line[n] == "<" and not attivo:
                attivo = not attivo
            elif line[n] == ">" and attivo:
                attivo = not attivo
                new_text += "|"
            elif attivo:
                new_text += line[n]


            #Se l'ultimo carattere è un end of line cancello l'ultimo "|" inserito

            if line[n] == "\n":
                if not new_text[-1] == line[n]:
                    new_text = new_text[:-1]
                #Aggiungo end of line al new_text
                new_text += line[n]

    #Cancello l'ultimo | aggiunto alla fine del testo (non c'è carattere per eof?)
    if new_text[-1] == "|":
        new_text = new_text[:-1]

print(new_text)
